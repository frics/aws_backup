<?php

$conn = new mysqli("recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com","root","recipe123", "MEMBER_DB");


// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$response = array();


if(isset($_GET['apicall'])){

    switch($_GET['apicall']){
        case 'signup':
            if(isTheseParametersAvailable(array('id', 'password', 'nickname'))){

                $id = $_POST['id'];
                $password = md5($_POST['password']);
                $nickname = $_POST['nickname'];


                $stmt = $conn->prepare("SELECT mem_idx FROM members WHERE id = ?");
                $stmt -> bind_param("s", $id);
                $stmt->execute();
                $stmt ->store_result();

                if($stmt->num_rows > 0){
                    $response['error'] = true;
                    $response['message'] = '이미 등록된 이메일입니다';
                    $stmt->close();
                }else{
                    $stmt = $conn -> prepare("INSERT INTO members (id, password, nickname) VALUES(?, ?, ?)");
                    $stmt->bind_param("sss", $id, $password, $nickname);

                    if($stmt->execute()){
                        //해당 사용자의 냉장고 table 생성을 위해  select문을 사용하여 mem_idx를 받아온다
                        //냉장고 table 이름 = mem_idx + nickname
                        $stmt = $conn->prepare("SELECT mem_idx FROM members WHERE id = ?");
                        $stmt->bind_param("s", $id);
                        $stmt->execute();
                        $stmt->bind_result($mem_idx);
                        $stmt->fetch();

                        $stmt->close();

                        $sql = "CREATE TABLE REF_DB.$mem_idx$nickname (
                                    ref_idx INT(12), 
                                    category VARCHAR(20) NOT NULL, 
                                    tag VARCHAR(20) NOT NULL, 
                                    name VARCHAR(30) NOT NULL,
                                    tagNumber INT(5) NOT NULL,
                                    PRIMARY KEY(ref_idx), 
                                    UNIQUE(name)
                                );";
                        if(mysqli_query($conn, $sql)){
                            $ref['error'] = false;
                            $ref['message'] = "REF_DB table name :$mem_idx$nickname 냉장고 DB 생성 완료";
                        }else{
                            $ref['error'] = true;
                            $ref['message'] = $id.mysqli_error($conn);
                        }
                        $response['error'] = false;
                        $response['message'] = '회원가입 완료';
                    
                    }
                }

            }else{
                $response['error'] = true;
                $response['message'] = '값을 전부 입력해주세요';
            }
            break;

        case 'signin':

            //for login we need the username and password 

            if(isTheseParametersAvailable(array('id', 'password'))){
                //getting values 
                $id = $_POST['id'];
                $password = md5($_POST['password']);

                //creating the query 
                $stmt = $conn->prepare("SELECT mem_idx, id, nickname FROM members WHERE id = ? AND password = ?");
                $stmt->bind_param("ss",$id, $password);

                $stmt->execute();

                $stmt->store_result();


                //if the user exist with given credentials 
                if($stmt->num_rows > 0){

                    $stmt->bind_result($mem_idx, $id, $nickname);
                    $stmt->fetch();

                    $user = array(
                        'mem_idx'=>$mem_idx,
                        'id'=>$id,
                        'nickname'=>$nickname
                    );

                    $response['error'] = false;
                    $response['message'] = '로그인 성공';
                    $out['user'] = $user;

                    //냉장고 디비 백업 시작
                    $sql = "SELECT * FROM REF_DB.$mem_idx$nickname";
                    $refResponse = array();

                    if($result = mysqli_query($conn, $sql)){
                        $refResponse['error'] = false;
                        $refResponse['message'] = "냉장고 복원 성공";

                        $data = array();
                        while($row = mysqli_fetch_array($result)) {
                            array_push($data,
                                array('ref_idx'=>$row['ref_idx'],
                                    'category'=>$row['category'],
                                    'tag'=>$row['tag'],
                                    'name'=>$row['name'],
                                    'tagNumber'=>$row['tagNumber']
                                ));
                        }
                        $out['refrigerator'] = $data;
                    }else{
                        $refResponse['error'] = true;
                        $refResponse['message'] = '냉장고 DB 연동 실패';
                    }

                    $sql = "SELECT serial_num FROM RECIPE_DB.scrap WHERE user_id =  '$id'";
                    $scrapResponse = array();

                    if($result = mysqli_query($conn, $sql)){
                        $scrapResponse['error'] = false;
                        $scrapResponse['message'] = "스크랩 리스트 복원 성공";
                            
                        $scrap_data = array();
                        while($row = mysqli_fetch_array($result)) {
                            array_push($scrap_data,
                                array('serial_num'=>$row['serial_num']));
                        }
                        $out['scrap'] = $scrap_data;
                    }else{
                        $scrapResponse['error'] = true;
                        $scrapResponse['message'] = "스크랩 리스트 복원 실패";
                    }

                }else{
                    //if the user not found 
                    $response['error'] = false;
                    $response['message'] = '아이디 혹은 비밀번호가 맞지 않습니다.';
                }
            }
            break;
        default:
            $response['error'] = true;
            $response['message'] = "없는 기능 입니다.";
    }
}else{
    $response['error'] = true;
    $response['message'] = 'No API CALL';
}

$out['response'] = $response;
$out['refResponse'] = $refResponse;
$out['scrapResponse'] = $scrapResponse;

echo json_encode($out,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);


function isTheseParametersAvailable($params){
    foreach($params as $param){
        if(!isset($_POST[$param])){
            return false;
        }
    }
    return true;
}

?>
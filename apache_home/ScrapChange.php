<?php


$conn = new mysqli("recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com","root","recipe123", "RECIPE_DB");


// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}




if(isset($_GET['apicall'])) {

    switch ($_GET['apicall']) {
        case 'scrapChange':
            if ($_POST['isScraped'] && $_POST['serial_num'] && $_POST['id']) {

                //filter_var이 받아온 string을 boolean변수로 변환해줌
                $isScraped = filter_var($_POST['isScraped'], FILTER_VALIDATE_BOOLEAN);
                $serial_num = $_POST['serial_num'];
                $id = $_POST['id'];


                //UPDATE scrapCount SET scrap_cnt = (scrap_cnt+1) WHERE serial_num = 1160;
                //$isScraped == true면 이제 좋아요 누른거임

                if ($isScraped == true) {
                    $stmt = $conn->prepare("INSERT INTO scrap (serial_num, user_id) VALUES(?, ?)");
                } else {//좋아요 취소했을때 테이블에서 제거
                    $stmt = $conn->prepare("DELETE FROM scrap WHERE serial_num = ? AND user_id = ?");
                }

                $stmt->bind_param("ss", $serial_num, $id);

                if ($stmt->execute()) {
                    
                    //isScraped에 따라서 UPDATE 쿼리문 증감 설정
                    //true면 +1 false면 -1
                    if ($isScraped == true) {
                        $sql = "UPDATE scrapCount SET scrap_cnt = (scrap_cnt+1) WHERE serial_num = $serial_num";
                        $response['error'] = false;
                        $response['message'] = "$serial_num : 좋아요 갱신 성공!";
                    } else {
                        $sql = "UPDATE scrapCount SET scrap_cnt = (scrap_cnt-1) WHERE serial_num = $serial_num";
                        $response['error'] = false;
                        $response['message'] = "$serial_num : 좋아요 취소 성공!";
                    }
                    //앞서 설정한 UPDATE 쿼리 실행
                    
                    if($result = mysqli_query($conn, $sql)) {
                        $response['cntChangeError'] = false;
                        $response['cntChangeMessage'] = "$serial_num : 좋아요 카운트 갱신 성공";
                    }else{
                        $response['cntChangeError'] = true;
                        $response['cntChangeMessage'] = "$serial_num : 좋아요 카운트 갱신 실패";
                    }
                } else {
                    $response['error'] = true;
                    $response['message'] = "$serial_num : 좋아요 갱신 실패!";
                }
            }
            break;
            
        case 'getScrapCount':
            
            //좋아요 갯수 상위 30개 가져옴
            $sql = "SELECT * FROM scrapCount ORDER BY scrap_cnt DESC, serial_num LIMIT 30";

            if($result = mysqli_query($conn, $sql)){
                $data = array();
                while($row = mysqli_fetch_array($result)){
                    //쿼리 결과 배열에 저장
                    array_push($data,
                        array('serial_num'=>$row['serial_num'],
                            'scrap_cnt'=>$row['scrap_cnt']));
                }
                $response['error'] = false;
                $response['message'] = "scrap_cnt 획득 성공";
                $response['scrap_data'] = $data;
            }else{
                $response['error'] = true;
                $response['message'] = "scrap_cnt 획득 실패";
                $response['scrap_data'] = null;
            }
            break;

    }
}

//데이터를 JSON 형식으로 출력
echo json_encode($response, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);

?>
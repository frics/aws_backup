<?php


$conn = new mysqli("recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com","root","recipe123", "REF_DB");


// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}



if($_POST['dbname']){

    $dbname = $_POST['dbname'];

    $sql = "TRUNCATE TABLE $dbname";

    if(mysqli_query($conn, $sql)){
        if($_POST['refJson']){

            $response['truncate'] = "초기화 성공";
            $json = $_POST['refJson'];
            $arr = json_decode($json);
            
            $stmt = $conn -> prepare("INSERT INTO $dbname VALUES(?, ?, ?, ?, ?)");
            foreach($arr as $row){
                $stmt->bind_param("sssss", $row -> ref_idx, $row -> category, $row -> tag, $row -> name, $row ->tagNumber);
                $stmt->execute();
            }
            $stmt->close();
            
            $response['error'] = false;
            $response['message'] = "DB 백업 성공";
            
        }
        else{
            $response['error'] = false;
            $response['message'] = "삽입할 데이터가 없습니다.";
        }
    }
    else{
        $response['error'] = true;
        $response['message'] = "DB 초기화 실패";
    }
}


//데이터를 JSON 형식으로 출력
echo json_encode($response, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);

?>
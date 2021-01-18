<?php

$conn = new mysqli("localhost","admin","recipe123", "RECIPE_DB");


// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

for($serial_num = 1 ; $serial_num <=1160 ; $serial_num++){
    $user_id = 'test_user10';

    $stmt = $conn->prepare("INSERT INTO scrap (serial_num, user_id) VALUES(?, ?)");
    $stmt->bind_param("ss", $serial_num, $user_id);
    if($stmt->execute()){
        $stmt->fetch();
        $stmt->close();
        $response['error'] = false;
        $response['message'] = "추가 성공";
    }else{
        $response['error'] = true;
        $response['message'] = "추가 실패";
    }
}

echo json_encode($response,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);

?>
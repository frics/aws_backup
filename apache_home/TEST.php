<?php

$conn = new mysqli("recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com","root","recipe123", "RECIPE_DB");


// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
/*
//현재 좋아요가 되있는 게시글 전부 스크랩
$sql = "SELECT DISTINCT serial_num FROM scrap";

if($result = mysqli_query($conn, $sql)){

    $serial_num = array();
    while($row = mysqli_fetch_array($result)) {

        $stmt = $conn->prepare("SELECT COUNT(CASE WHEN serial_num = ? THEN 1 END) FROM scrap");
        $stmt->bind_param("s", $row['serial_num']);

        if ($stmt->execute()) {
            $stmt->bind_result($scrap_cnt);
            $stmt->fetch();
            $stmt->close();

            $response['scrap_cnt'] = $scrap_cnt;
            $response['error'] = false;
            $response['message'] = "Scrap 카운트 획득 성공";
        }
        array_push($serial_num,
            array('serial_num'=>$row['serial_num'],
                 'scrap_cnt'=>$scrap_cnt));
    }
    $response['scrap'] = $serial_num;
}
*/

$sql = "SELECT * FROM scrapCount ORDER BY scrap_cnt DESC, serial_num LIMIT 30";

if($result = mysqli_query($conn, $sql)){   
    $data = array();
    while($row = mysqli_fetch_array($result)){
        array_push($data,
            array('serial_num'=>$row['serial_num'],
                 'scrap_cnt'=>$row['scrap_cnt']));
    }
    $response['error'] = false;
    $response['messsage'] = "scrap_cnt 획득 성공";
    $response['scrap_data'] = $data;
}else{
    $response['error'] = true;
    $response['messsage'] = "scrap_cnt 획득 실패";
    $response['scrap_data'] = null;
}


echo json_encode($response,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);

?>
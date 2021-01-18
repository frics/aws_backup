<?php
    
$conn = new mysqli("recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com","root","recipe123", "RECIPE_DB");


// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM numbering";
if($result = mysqli_query($conn, $sql)){
   
    $data = array();
    while($row = mysqli_fetch_array($result)) {
        array_push($data,
                   array('category'=>$row['category'],
                         'tag'=>$row['tag'],
                         'tagNumber'=>$row['tagNumber']
                    ));
    }
    $response['error'] = false;
    $response['message'] = '태그 받아오기 성공';
    $out['tag'] = $data;
}else{
    $response['error'] = true;
    $response['message'] = '태그 받아오기 실패';
}
$out['response'] = $response;


//데이터를 JSON 형식으로 출력
echo json_encode($out, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE); 

?>
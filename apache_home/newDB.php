<?php
    $id = "test";
$nickname = "fuck";
    
    
$conn = new mysqli("recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com","root","recipe123", "RECIPE_DB");

// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "연결 성공";
$id = "liked";
$nickname = "fuck";
echo $id."<br>";

$sql = "CREATE TABLE $id (
        serial_num INT(12), 
        liked INT(12) NOT NULL,
        PRIMARY KEY(serial_num)
        );";

if (mysqli_query($conn, $sql)) {
    echo "Table test created successfully";
}
 else {
    echo "Error creating table: " . mysqli_error($conn);
}

mysqli_close($conn);

?>
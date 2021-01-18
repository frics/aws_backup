<?php
    //mysql서버 connect;
    include 'con_mysql.php';

if(isset($_POST['Id']) && isset($_POST['Pw'])){
    
    //변수 초기화
    $result='';
    $userID = $_POST["Id"];
    $userPassword = $_POST["Pw"];
    //MYSQL QUERY문
    $statement = mysqli_prepare($con,"SELECT * FROM members WHERE id =: s AND password =: s";
mysqli_stmt_bind_param($statement, "ss", $userID,$userPassword);
mysqli_stmt_excute($statement);

$response = array();
$response["success"] = true;

if($response["erro"] == true){
    echo json_encode($response);
}
?>

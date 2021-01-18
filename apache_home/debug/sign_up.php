<?php
 
       //mysql서버 connect;
        include 'con_mysql.php';
 
        $userID = $_POST["Id"];
        $userPassword = $_POST["Pw"];
        $userNickname=$_GET["Nickname"];
echo "변수 초기화 완료";
 
    /***
 
        //입력받은 데이터를 DB에 저장
        $query = "insert into member (id, password, nickname) values ('$userID', '$userPassword', '$userNickname')";
 
 
        $result = $conn->query($query);
 
        //저장이 됬다면 (result = true) 가입 완료
        if($result) {
        ?>      <script>
                alert('가입 되었습니다.');
                location.replace("./login.php");
                </script>
 
<?php   }
        else{
?>              <script>
                        
                        alert("fail");
                </script>
<?php   }
 
        mysqli_close($conn);
?>

***/
      //입력 받은 id와 password
        $id=$_GET[Id];
        $pw=$_GET[Pw];
        $nickname=$_GET[Nickname];
 
        $date = date('Y-m-d H:i:s');
 
        //입력받은 데이터를 DB에 저장
        $query = "insert into member (id, password, nickname) values ('$id', '$pw', '$nickname')";
 
 
        $result = $connect->query($query);
 
        //저장이 됬다면 (result = true) 가입 완료
        if($result) {
        ?>      <script>
                alert('가입 되었습니다.');
                location.replace("./login.php");
                </script>
 
<?php   }
        else{
?>              <script>
                        
                        alert("fail");
                </script>
<?php   }
 
        mysqli_close($connect);
?>
 

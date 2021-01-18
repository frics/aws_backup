<?php
echo "file Upload Program<br/>";
echo "select the file<br/>";
?>

<form method="post" action="upload_act.php" enctype="multipart/form-data">
	<input type="file" size=100 name="uploaded_file"><hr>
	<input type="submit" value="sent">
</form>

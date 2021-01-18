<?php

//파일 저장 경로
$dir = '../OCR/resource/OriImgPath/';

//전송 받은 파일 임시 저장소에 저장, 임시 저장소 경로 -> ".$_FILES['uploaded_file']['tmp_name']."<br>"
$uploadfile= $dir.basename($_FILES['uploaded_file']['name']);

//해당 파일 저장에 성공했으면 설정한 경로로 이동
if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'],$uploadfile)){
    $response['error'] = false;
    $response['message'] = "파일 업로드 성공\n파일 이름 : {$_FILES['uploaded_file']['name']}\n파일 크기 : {$_FILES['uploaded_file']['size']}bytes";
    
    $resultOCR = false;
    if($resultOCR){
        $response['OCRerror'] = false;
        $response['OCRmessage'] = "OCR 인식 성공";
    }else{
        $response['OCRerror'] = true;
        $response['OCRmessage'] = "OCR 인식 실패";
    }
        
} else{
    $response['error'] = true;
    switch ($_FILES['uploaded_file']['error']){
        case 1:
            $response['message'] = 'upload_max_filesize 초과';
            break;
        case 2:
            $response['message'] = 'max_file_size 초과';
            break;
        case 3:
            $response['message'] =  'file Buffer 손상';
            break;
        case 4:
            $response['message'] =  '파일이 없음';
            break;
        case 6: 
            $response['message'] =  '임시 폴더를 찾을 수 없음';
            break;
        case 7:
            $response['message'] =  '임시 폴더 접근 권한이 없음';
            break;
        case 8:
            $response['message'] =  '확장에 의한 파일 업로드 중지';
            break;
    }
}

//0912
sleep(3);

echo json_encode($response,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);


?>


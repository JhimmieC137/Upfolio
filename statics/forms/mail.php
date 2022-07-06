<?php
//get data from form  
$name = $_POST['name'];
$email= $_POST['email'];
$message= $_POST['message'];
$to = "toluwalope.david@gmail.com";
$subject = $_POST['message'];;
$txt ="Name = ". $name . "\r\n  Email = " . $email . "\r\n Subject = " . $subject. "\r\n Message = ".$message ;
$headers = "From: noreply@theupfolio.com" . "\r\n" .
"CC: somebodyelse@example.com";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("Location:thankyou.html");
?>
<?php
// required headers
$json = file_get_contents('php://input');
$_POST = json_decode($json,1);
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
 
// include database and object files
include_once '../config/database.php';
include_once '../objects/student.php';
 
// instantiate database and product object
$database = new Database();
$db = $database->getConnection();
 
// initialize object
$student = new Student($db);
 

$student_id = ($_POST["student_id"]);
$fingerPrint = ($_POST["fingerprint_template"]);

 
if($student->add_finger($student_id,$fingerPrint)){

    echo json_encode( array("message" => "finger Print was recorded."));
}
 
// if unable to add finger, tell the user
else{
    
        echo json_encode( array("message" => "Unable to finger print."));
    
}


?>
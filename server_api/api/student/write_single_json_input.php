<?php
// required headers
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");
 
// get database connection
include_once '../config/database.php';
 
// instantiate Student object
include_once '../objects/student.php';
 
$database = new Database();
$db = $database->getConnection();
 
$student = new Student($db);
 
// get posted data
$data = json_decode(file_get_contents("php://input"));
 
// set student property values
$student_id = $data->Sid;
$course_id = $data->Cid;
$attended = $data->att;
$time = $data->t;
$date = $data->d;

// create the student
if($student->record_single($student_id,$course_id,$attended,$time,$date)){
    echo '{';
        echo '"message": "student was recorded."';
    echo '}';
}
 
// if unable to create the student, tell the user
else{
    echo '{';
        echo '"message": "Unable to record student."';
    echo '}';
}
?>
write_single_json_input.php
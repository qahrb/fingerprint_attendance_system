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
$data = json_decode(file_get_contents("php://input"),1);
// var_dump($data['records']);die;
$input_arr=array();
$arr=$data['records'];
$arr_size = count($arr);

for($x = 0 ; $x < $arr_size ;$x++){
	$student_id = ($arr[$x]['Sid']);
	$course_id = ($arr[$x]['Cid']);
	$attended = ($arr[$x]['att']);
	$time = ($arr[$x]['t']);
	$date = ($arr[$x]['d']);

	if($student->record_single($student_id,$course_id,$attended,$time,$date)){

	}	else {
		echo "Cannot record";	die();
	}
}
 echo '{';
        echo '"message": "students were recorded."';
    echo '}';
die; ?>
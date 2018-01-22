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
$stmt = $student->find_by_id($student_id);
$num = $stmt->rowCount();
 
// check if more than 0 record found

if($num>0){
 
    // Students array
    $students_arr=array();
    $students_arr["records"]=array();
 
    // retrieve our table contents
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    extract($row);
 
    $student_info=array(
        "student_id" => $id,
        "name" => $name,
        "fingerprint_template" => $fingerPrint,
        "message"=> null

    );
 
    // array_push($students_arr["records"], $student_info);
    
 
    echo json_encode($student_info, JSON_PRETTY_PRINT);
}
 
else{
    echo json_encode(
        array("message" => "No student found.")
    );
}
?>
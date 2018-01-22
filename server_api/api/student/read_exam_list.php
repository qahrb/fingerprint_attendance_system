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
 
$course = ($_POST["course"]);



//read admins-------------------------------------------------
$student_info = $student->read_exam($course);
$student_list=array();
$num=$student_info->rowCount();
if($num>0){
while ($element= $student_info->fetch(PDO::FETCH_ASSOC)){
// print_r( $element);die;
 $loop_info=array(
            "id" => $element["id"],
            "name" => $element["name"],
            "fingerPrint" => $element["fingerPrint"]
        );
            // $student_list[((string)$loop_info["time"])] = array();
             array_push($student_list, $loop_info);

}
$result=array();
$result["records"]=array();
$result["records"] = $student_list;
  echo json_encode($result);
  die;
//---------------------------------------------------------

}

else{
    echo json_encode(
        array("message" => "No student found.")
    );
}
?>
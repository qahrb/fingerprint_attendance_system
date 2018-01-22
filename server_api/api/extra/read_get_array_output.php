<?php
// required headers
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
 
$day = ($_GET["day"]);
$location = ($_GET["location"]);

$stmt = $student->read($day,$location);
$num = $stmt->rowCount();
// check if more than 0 record found
if($num>0){
 
    // Students array
    $students_arr=array();
    $students_arr["records"]=array();
 
    // retrieve our table contents

    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
        
        extract($row);
 
        $student_info=array(
            "id" => $id,
            "name" => $name,
            "fingerPrint" => $fingerPrint,
             "time" => $time

        );
 
        array_push($students_arr["records"], $student_info);
    }
 
    echo '<pre>'; print_r($students_arr); echo '</pre>';

}
 
else{
    echo json_encode(
        array("message" => "No student found.")
    );
}
?>
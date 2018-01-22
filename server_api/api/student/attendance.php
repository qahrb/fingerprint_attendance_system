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
 
$day = ($_POST["day"]);
$location = ($_POST["location"]);



//read admins-------------------------------------------------
$admin_info = $student->read_admin();
 $admin_list=array();
while ($element= $admin_info->fetch(PDO::FETCH_ASSOC)){

 $loop_info=array(
            "id" => $element["admin_id"],
            "name" => $element["admin_name"],
            "fingerPrint" => $element["admin_fingerPrint"]
        );
            // $admin_list[((string)$loop_info["time"])] = array();
             array_push($admin_list, $loop_info);

}
 // echo json_encode($admin_list);
 // die;
//---------------------------------------------------------

//read instrucdors of the day-----------------------------------
$instructor_info = $student->read_instructor($day,$location);
 $instructor_list=array();
while ($element= $instructor_info->fetch(PDO::FETCH_ASSOC)){

 $loop_info=array(
            "id" => $element["instructor_id"],
            "name" => $element["instructor_name"],
            "fingerPrint" => $element["instructor_fingerPrint"],
            "time" => $element["time"]
        );
            $instructor_list[((string)$loop_info["time"])] = array();
             array_push($instructor_list[((string)$loop_info["time"])], $loop_info);

}
// echo json_encode($instructor_list["08:00"]);
// die;
//---------------------------------------------------------

$stmt = $student->read($day,$location);
$temp = $stmt;
$num = $stmt->rowCount();
$stmt2 = $student->read_time($day,$location);
$num2 = $stmt2->rowCount();
// check if more than 0 record found
if($num>0 && $num2>0){

    $students_arr=array();
    $students_arr["records"]=array();
    $time_arr = $students_arr["records"];

    // retrieve our table contents
    while ($row2 = $stmt2->fetch(PDO::FETCH_ASSOC)){ 
       
        $stmt = $student->read($day,$location);
        $arr_time[((string)$row2["time"])]=array();

        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
 
        $student_info=array(
            "id" => $row["id"],
            "name" => $row["name"],
            "fingerPrint" => $row["fingerPrint"],
            "time" => $row["time"],
            "course_id" => $row["course_id"]
        );

        if ($row["time"] == $row2["time"]) {
            array_push($arr_time[((string)$row2["time"])], $student_info);

//------------------------------------------------------------------------------------***********
        }
        }  
        array_push($students_arr["records"], $arr_time);
    }
    $temp = $students_arr["records"][count($students_arr["records"])-1];
    // echo  json_encode($students_arr["records"][0]);
        // echo  json_encode($temp["08:00"]);
    // $t=array();
    // $t["08:00"]=array();
    $t2=array();
    $t2["records"]=array();
    $t2["admins"]=array();
    $t2["admins"]=$admin_list;
    // array_push($t["08:00"],$temp["08:00"]);
    // array_push($t2["records"],$t);
    // echo  json_encode($t2);

    $stmt2 = $student->read_time($day,$location);
    while ($row2 = $stmt2->fetch(PDO::FETCH_ASSOC)){
        $t=array();
        $t[((string)$row2["time"])]=array();
        $t["instrcutors"]=array();
        $t[((string)$row2["time"])] = $temp[((string)$row2["time"])];
        $t["instrcutors"]=$instructor_list[((string)$row2["time"])];
        array_push($t2["records"],$t);

      // echo  json_encode($temp[((string)$row2["time"])]);
    }
    
     echo  json_encode($t2);

        die;
}

else{
    echo json_encode(
        array("message" => "No student found.")
    );
}
?>
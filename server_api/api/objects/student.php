<?php
class Student{
 
    // database connection and table name
    private $conn;
    private $table_name = "students";
 
    // object properties
    public $id;
    public $name;
    public $fingerPrint;
    
    
    // constructor with $db as database connection
    public function __construct($db){
        $this->conn = $db;
    }
    // read Students
function read($day,$location){
        //////////////////////////////////////////////////////
        $query = " SELECT s.id , s.name, s.fingerPrint, t.time,e.course_id  FROM students s 
            JOIN enrolment e on s.id = e.student_Id
            JOIN time_table t on e.course_id = t.course_id
                  WHERE t.day = '" . $day . "' AND t.class ='" . $location ."'ORDER BY t.time DESC";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
    // read time
function read_time($day,$location){
        //////////////////////////////////////////////////////
        $query = "SELECT time from time_table WHERE day = '". $day ."' AND class = '". $location ."'  GROUP BY time ORDER BY time";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
//read instructor
function read_instructor($day,$location){
        //////////////////////////////////////////////////////
        $query = " SELECT instructor.instructor_id , instructor.instructor_name, instructor.instructor_fingerPrint, time_table.time FROM instructor
            JOIN instructor_courses on instructor.instructor_id = instructor_courses.instructor_id
            JOIN time_table on instructor_courses.course_id = time_table.course_id
            WHERE time_table.day = '". $day ."' AND time_table.class ='". $location ."'ORDER BY time_table.time ";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
//read admins
function read_admin(){
        //////////////////////////////////////////////////////
        $query = " SELECT * FROM admins";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
//read student list for exam
function read_exam($course_id){
        //////////////////////////////////////////////////////
        $query = " SELECT s.id , s.name, s.fingerPrint FROM students s 
JOIN enrolment e on s.id = e.student_Id
where e.course_id='". $course_id ."'";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
// record attendace
function record_single($student_id,$course_id,$attended,$time,$date){
 
    // query to insert record
    $query = "INSERT INTO att_record VALUES (".$student_id.",".$course_id.",'".$date."','".$time."',".$attended.")";
 
 
    // prepare query
    $stmt = $this->conn->prepare($query);
 
    // execute query
    if($stmt->execute()){
        return true;
    }else{
        return false;
    }
}
//find student by id
function find_by_id($id){
        //////////////////////////////////////////////////////
        $query = " SELECT s.id , s.name, s.fingerPrint FROM students s 
                  WHERE s.id = '" . $id ."'";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
// add finger print to student
function add_finger($student_id,$finger){
 
    // query to insert record
    $query = "UPDATE students SET fingerprint = '".$finger."'  WHERE id = " . $student_id ."";

    // prepare query
    $stmt = $this->conn->prepare($query);
 
    // execute query
    if($stmt->execute()){
        return true;
    }else{
        return false;
    }
}

//web application functions :-----------------------------------------------------
function web_find_student_courses($id){
        //////////////////////////////////////////////////////
        $query = " SELECT courses.course_code FROM `enrolment` 
        RIGHT JOIN courses on enrolment.course_id = courses.id
        WHERE `student_Id`='" . $id ."'";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
function web_find_students_list_attendance_by_course($course_id){
        //////////////////////////////////////////////////////
        $query = " SELECT students.name, students.id,SUM(att_record.attend) as attendance FROM students
        JOIN att_record on students.id = att_record.student_id
        JOIN enrolment on students.id = enrolment.student_Id
        JOIN courses on enrolment.course_id = courses.id
        WHERE courses.course_code = '". $course_id ."'
        GROUP BY students.id ";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
function web_individual_attendance_in_course($student_id,$course_code){
        //////////////////////////////////////////////////////
        $query = " SELECT date,attend FROM att_record
        JOIN    courses on courses.id = att_record.course_id
        WHERE courses.course_code = '".$course_code."' AND att_record.student_id = '". $student_id ."'";
        /////////////////////////////////////////////////////

    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    return $stmt;
}
function log_in($user,$pass){
    return true;
}

}
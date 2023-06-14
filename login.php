<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "charityorganizer";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (isset($_POST['email']) && isset($_POST['password'])) {

$email = $_POST['email'];
$password = $_POST['password'];

}else{
	
	$email = "";
	$password = "";
}


// Execute the query
$mysql_qry= "select login_id from login where password= '$password' and email='$email';";
$result = mysqli_query($conn, $mysql_qry);

// Check if query was successful
if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}

// Pass the result to JSON if it contains at least one row
if (mysqli_num_rows($result) > 0) {
    $row = mysqli_fetch_assoc($result);
    $value = $row["login_id"];
    $output = array('status' => 'Sign In Successful', 'id' => $value);
    echo json_encode($output);
} else {
	$data=['status'=>'Sign In Not Successful'];
	echo json_encode($data); 
}

// Close the connection
mysqli_close($conn);
?>



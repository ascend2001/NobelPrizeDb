<?php
// get the id parameter from the request
$id = intval($_GET['id']);

// connect to the database 
$db = new mysqli('localhost', 'cs143', '', 'class_db');
if ($db->connect_errno > 0) { 
    die('Unable to connect to database [' . $db->connect_error . ']'); 
}
// do the query and get the result for each table since easier then joining them all
$query_PersonName = " SELECT * FROM PersonName WHERE id = $id ";
$result_PersonName = $db->query($query_PersonName);
// error handeling 
if (!$result_PersonName) {
    $errmsg = $db->error; 
    print "Query PersonName failed: $errmsg <br>"; 
    exit(1); 
}
$row_PersonName = $result_PersonName->fetch_assoc(); 

$query_NobelPrize = " SELECT * FROM NobelPrize WHERE id = $id ";
$result_NobelPrize = $db->query($query_NobelPrize);
// error handeling 
if (!$result_NobelPrize) {
    $errmsg = $db->error; 
    print "Query NobelPrize failed: $errmsg <br>"; 
    exit(1); 
}
$row_NobelPrize = $result_NobelPrize->fetch_assoc(); 

$query_Affiliations = " SELECT * FROM Affiliations WHERE id = $id ";
$result_Affiliations = $db->query($query_Affiliations);
// error handeling 
if (!$result_Affiliations) {
    $errmsg = $db->error; 
    print "Query Affiliations failed: $errmsg <br>"; 
    exit(1); 
}
$row_Affiliations = $result_Affiliations->fetch_assoc(); 

// set the Content-Type header to JSON, 
// so that the client knows that we are returning JSON data
header('Content-Type: application/json');

// $output = ["id" => strval($id)] + ($row_PersonName['givenName'] ? [5 => 'two'] : []) + (false ? [10 => 'three'] : []);

$output = (object) [
    "id" => strval($id),
    "givenName" => (object) [
        "en" => strval($row_PersonName['givenName'])
    ] ,
    "familyName" => (object) [
        "en" => strval($row_PersonName['familyName'])
    ],
    "gender" => (object) [
        strval($row_PersonName['gender'])
    ], 
    "birth" => array(
        "date" => (object) [
            strval($row_PersonName['DOB'])
        ],
        "place" => array(
            // ($row_PersonName['city'] ? ["en" => strval($row_PersonName['city'])] : []] )
            "city" =>  (object) [
                "en" => strval($row_PersonName['city'])
            ],
            "country"=> (object) [
                "en" => strval($row_PersonName['country'])
            ]
        )
    ),
    "nobelPrizes" => array(
        "awardYear" => (object) [
            strval($row_NobelPrize['awardYear'])
        ],
        "category" => (object) [
            "en" => strval($row_NobelPrize['category'])
        ],
        "sortOrder" => (object) [
            strval($row_NobelPrize['sortOrder'])
        ],
        "affiliations" => array(
            "name" => (object) [
                strval($row_Affiliations['name'])
            ],
            "city" => (object) [
                "en" => strval($row_Affiliations['city'])
            ],
            "country " => (object) [
                "en" => strval($row_Affiliations['country'])
            ]
        )
    )
];
echo json_encode($output, JSON_PRETTY_PRINT);
?>
<?php
$videoFolderPath = "F:\BaiduSyncdisk\300投资资料\2.看盘复盘记录\牛股回顾"; // Specify the path to your videos folder

$videoFiles = [];
$files = scandir($videoFolderPath);
foreach ($files as $file) {
    if ($file !== '.' && $file !== '..') {
        $videoFiles[] = $file;
    }
}

header('Content-Type: application/json');
echo json_encode($videoFiles);
?>
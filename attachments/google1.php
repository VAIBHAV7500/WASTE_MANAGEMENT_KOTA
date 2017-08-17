 <?php
$myfile = fopen("f.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("f.txt"));
fclose($myfile);
?> 

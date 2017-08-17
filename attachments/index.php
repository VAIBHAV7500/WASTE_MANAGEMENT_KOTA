<?php
$fh = fopen('f.txt','r');
while ($line = fgets($fh))
{
  // <... Do your work with the line ...>
  $m =fgets($fh);

include('google.html');
    
}
fclose($fh);
?>

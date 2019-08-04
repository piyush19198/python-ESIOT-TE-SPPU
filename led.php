<?php
   if (isset($_POST['on']))
   {
                 exec("sudo killall python");
                 exec("sudo python /var/www/motor_anti.py");
   }
   else if (isset($_POST['off']))
   {
                 exec("sudo killall python");
                 exec("sudo python /var/www/motor_stop.py");
   }
   else if (isset($_POST['blink']))
   {
                 exec("sudo killall python");
                 exec("sudo python /var/www/ledBLINK.py");
   }
?>
<html>
        <style type="text/css">
/Button colour is now yellow and size has been changed
                 #form{font: bold 30px/30px Georgia, serif;}
                 button{background: rgba(255, 255, 0, 0.99); width:200px; height: 100px;border: none;border: 3px solid black;border-
adius:20px;}
                 #container{margin0px; auto;width:80%;min-width:40%;}
        </style>
        <body>
        <div id="container">
                 <form id="form" method="post">
                         <center>
      <br><br>                  <button name="on"><h1>Led ON</h1></button>
      		                <button name="off"><h1>Led OFF</h1></button>
                	        <button name="blink"><h1>Led BLINK</h1></button>
                 </form>
                 </div>
        </body>
</html>

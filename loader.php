<?php
 if(is_uploaded_file($_FILES["filename"]["tmp_name"]))
   {
     // Если файл загружен успешно, перемещаем его
     // из временной директории в конечную
     move_uploaded_file($_FILES["filename"]["tmp_name"], "".$_FILES["filename"]["name"]);
   } else {
      echo("Ошибка загрузки файла");
   }
?>
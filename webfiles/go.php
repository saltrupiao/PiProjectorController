<?php
/**
 * Created by PhpStorm.
 * User: saltrupiano
 * Date: 2/6/20
 * Time: 11:16 AM
 */

# file upload code sourced from: https://www.w3schools.com/php/php_file_create.asp

    $action = $_GET('goAction');
    switch($action)
    {
        case 'goCmdPOn':
            $powerOnValue = $_GET('cmdPOn');

            $powerOnFile = fopen('powerOnCmd','w') or die('Failed to open file.');

            fwrite($powerOnFile, $powerOnValue);

            fclose($powerOnFile);

            break;

        case 'goCmdPOff':
            $powerOffValue = $_GET('cmdPOff');

            $powerOffFile = fopen('powerOffCmd','w') or die('Failed to open file.');

            fwrite($powerOffFile, $powerOffValue);

            fclose($powerOffFile);

            break;

        default:
            echo "File not valid.";

    }

?>
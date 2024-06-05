# automatic puppet fix

exec { 'Fix_wordpress':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}

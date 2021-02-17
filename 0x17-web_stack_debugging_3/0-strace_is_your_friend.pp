# Using strace, find out why Apache is returning a 500 error

exec { 'callMeDebugged':
  command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  provider => 'shell',
}

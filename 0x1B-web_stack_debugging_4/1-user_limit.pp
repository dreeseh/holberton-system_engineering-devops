# Change the OS configuration so that it is
# possible to login with the holberton user
# and open a file without any error message

exec {'increase OS Limits':
     command => 'sudo sed -i "s/5/3000/g; s/4/3000/g" /etc/security/limits.conf',
     path    => '/bin:/usr/bin:/usr/sbin:/sbin',
}
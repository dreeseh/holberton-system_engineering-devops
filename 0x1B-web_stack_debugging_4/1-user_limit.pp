# Change the OS configuration so that it is

exec {'increase OS limits':
     command => "sed -i 's/worker_processes 4;/worker_processes 8;/g'
     /etc/security/limits.conf; sudo service nginx restart",
     path    => ['/bin', '/usr/bin']
}
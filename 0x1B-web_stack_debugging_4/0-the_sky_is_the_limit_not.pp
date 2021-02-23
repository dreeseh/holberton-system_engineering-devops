# the number of requests is too small, we need to up
# the ability to something like 2000.

exec {'upTheReqAbility':
  command => "sed -i 's/-n 15/-n 2000/g' /etc/default/nginx; service nginx restart",
  path    => ['/usr/bin', '/bin'],
}

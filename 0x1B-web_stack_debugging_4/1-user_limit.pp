# Change the holberton's user limit of open files.

$upper_limit='holberton hard nofile [0-9]*'
$lower_limit='holberton soft nofile [0-9]*'
$desired_upper_limit='holberton hard nofile 50000'
$desired_lower_limit='holberton soft nofile 30000'
$set_upper="'s/${upper_limit}/${desired_upper_limit}/g'"
$set_lower="'s/${lower_limit}/${desired_lower_limit}/g'"
$conf_file='limits.conf'
$change_limits="sudo sed -i -e ${set_upper} -e ${set_lower} ${conf_file}"

exec {'Increase holberton user limit of open files':
    command => $change_limits,
    path    => '/usr/bin',
    cwd     => '/etc/security'
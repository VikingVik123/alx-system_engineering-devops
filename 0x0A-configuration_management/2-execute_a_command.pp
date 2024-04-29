# manifest to execute a command

exec { 'killmenow':
    command     => 'pkill killmenow',
    refreshonly => true,
    onlyif      => 'pgrep killmenow',
}
# manifest to create a file in specified dir

file { '/tmp/school':
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   =>  'www-data',
}
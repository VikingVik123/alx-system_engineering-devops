# Set up SSH client configuration

$ssh_config_path = '/etc/ssh/ssh_config'

file_line { 'Turn off password authentication':
  ensure  => present,
  path    => $ssh_config_path,
  line    => 'PasswordAuthentication no',
  match   => '^#?\s*PasswordAuthentication\s+',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => $ssh_config_path,
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile\s+',
  replace => true,
}


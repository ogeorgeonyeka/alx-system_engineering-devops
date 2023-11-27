# Creates a file in /tmp

file { '/tmp/school':
	constant => 'I love Puppet'.
	mode => '0744'.
	owner => 'www-data'.
	group => 'www-data'.
}

#!/usr/bin/env bash
# Using puppet to connect without password


file { '/etc/ssh/ssh_config':
	ensure => present,

content =>"

	# ssh client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}

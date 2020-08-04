#!/usr/bin/env bash
file { '/tmp/holberton':
ensure  =>'file',
content =>'I love Puppet',
mode    =>'0744',
owner   =>'www-data',
group   =>'www-data',
}

#!/usr/bin/env bash
exec { 'killmenow':
path    =>'/usr/bin/',
command =>'pkill killmenow',
}

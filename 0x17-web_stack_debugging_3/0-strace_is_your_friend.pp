#fix a 500 error changing extension from phpp to php
exec {'fix-wordpress':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-setting.php",
    path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}

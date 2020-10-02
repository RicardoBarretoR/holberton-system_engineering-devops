#fix a 500 error changing extension from phpp to php
exec {'fixing_500':
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}

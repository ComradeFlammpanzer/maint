/bin/certbot certonly --webroot -w /var/www/static/ -d example.com
/bin/systemctl restart nginx

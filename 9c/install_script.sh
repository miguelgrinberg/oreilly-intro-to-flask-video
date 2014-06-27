#!/bin/bash

# install web server dependencies
sudo apt-get update
sudo apt-get -y install python python-virtualenv nginx supervisor

# install application (source location in $1)
mkdir /home/vagrant/weather
cp -R $1/weather/* /home/vagrant/weather/

# create a virtualenv and install dependencies
virtualenv /home/vagrant/weather/venv
/home/vagrant/weather/venv/bin/pip install -r /home/vagrant/weather/requirements.txt

# configure supervisor
sudo cp /vagrant/weather.conf /etc/supervisor/conf.d/
sudo mkdir /var/log/weather
sudo supervisorctl reread
sudo supervisorctl update

# configure nginx
sudo cp /vagrant/weather.nginx /etc/nginx/sites-available/weather
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/weather /etc/nginx/sites-enabled/
sudo service nginx restart

echo Application deployed to http://192.168.33.10/

#!/bin/bash

#WHATAP_HOME="/var/app/staging"
WHATAP_HOME=$(/opt/elasticbeanstalk/bin/get-config environment -k WHATAP_HOME)

#WHATAP_LICENSE_KEY="x41pl22ek7jhv-z43cebasdv4il7-z62p3l35fj5502"
WHATAP_LICENSE_KEY=$(/opt/elasticbeanstalk/bin/get-config environment -k WHATAP_LICENSE_KEY)

#WHATAP_HOST="15.165.146.117"
WHATAP_HOST=$(/opt/elasticbeanstalk/bin/get-config environment -k WHATAP_HOST)

#WHATAP_APP_NAME="python-elb-django"
WHATAP_APP_NAME=$(/opt/elasticbeanstalk/bin/get-config environment -k WHATAP_APP_NAME)

source /var/app/venv/*/bin/activate

export WHATAP_HOME=$WHATAP_HOME

echo `sudo mkdir -p $WHATAP_HOME`

echo `sudo chown -R webapp:webapp $WHATAP_HOME`

echo `sudo chmod -R 777 $WHATAP_HOME`
sudo -u webapp WHATAP_HOME=$WHATAP_HOME $VIRTUAL_ENV/bin/whatap-setting-config --host $WHATAP_HOST --license $WHATAP_LICENSE_KEY --app_name $WHATAP_APP_NAME --app_process_name gunicorn

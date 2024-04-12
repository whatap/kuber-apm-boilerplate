#!/bin/bash
#!/bin/bash

#export WHATAP_HOME=${PWD}
#export app_name=python-demo
#export app_process_name=gunicorn
#export whatap_server_host=13.124.11.223/13.209.172.35
#export license=x604kdg82hlpd-z7ifh4na92dtp2-x7hkehn5dti9sc

export WHATAP_HOME=${PWD}
whatap-setting-config \
--host $whatap_server_host \
--license $license \
--app_name $app_name \
--app_process_name $app_process_name

echo "whatap.okind=DEMO" >> whatap.conf
echo "whatap.onode=KUBE" >> whatap.conf
echo "logsink_enabled=true" >> whatap.conf
echo "logsink_trace_enabled=true" >> whatap.conf
echo "trace_logging_enabled=true" >> whatap.conf
echo "log_unhandled_exception=true" >> whatap.conf
#whatap-start-agent uvicorn server:app --host 0.0.0.0 --port 8000
whatap-start-agent gunicorn --config config/gunicorn.py server:app
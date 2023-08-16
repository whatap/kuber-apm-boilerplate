#!/bin/bash
export WHATAP_HOME=${PWD}
chmod -R 777 $WHATAP_HOME
whatap-setting-config \
--host 15.165.146.117 \
--license $WHATAP_LICENSE \
--app_name myapp \
--app_process_name flask

echo "trace_logging_enabled=${WHATAP_LOGGING_ENABLED}" >> whatap.conf

whatap-start-agent gunicorn -b 0.0.0.0:8000 --workers=2 app_flask:app
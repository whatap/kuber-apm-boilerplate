#!/bin/bash
export WHATAP_HOME=${PWD}
chmod -R 777 $WHATAP_HOME
whatap-setting-config \
--host $WHATAP_SERVER_HOST \
--license $WHATAP_LICENSE \
--app_name $WHATAP_APP_NAME \
--app_process_name uvicorn

echo "trace_logging_enabled=${WHATAP_LOGGING_ENABLED}" >> whatap.conf
echo "log_unhandled_exception=${WHATAP_LOGGING_ENABLED}" >> whatap.conf
echo "profile_basetime=0" >> whatap.conf
whatap-start-agent uvicorn server:app --host 0.0.0.0 --port 8000

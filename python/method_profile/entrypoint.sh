#!/bin/bash
export WHATAP_HOME=${PWD}
chmod -R 777 $WHATAP_HOME
whatap-setting-config \
--host $WHATAP_SERVER_HOST \
--license $WHATAP_LICENSE \
--app_name method_profiling \
--app_process_name python

echo "trace_logging_enabled=${WHATAP_LOGGING_ENABLED}" >> whatap.conf
echo "log_unhandled_exception=${WHATAP_LOGGING_ENABLED}" >> whatap.conf
echo "profile_basetime=0" >> whatap.conf
whatap-start-agent python main.py
#!/bin/bash
export WHATAP_HOME=${PWD}
chmod -R 777 $WHATAP_HOME
whatap-setting-config \
--host 15.165.146.117 \
--license $WHATAP_LICENSE \
--app_name myapp \
--app_process_name uvicorn

whatap-start-agent uvicorn server:app --host 0.0.0.0 --port 8000

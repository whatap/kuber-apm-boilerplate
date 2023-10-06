#!/bin/bash

#컨테이너의 작업 디렉토리를 와탭 경로로 설정됩니다. 해당 경로에 에이전트 로그 및 설정파일이 생성됩니다.
export WHATAP_HOME=${PWD}

#권한으로 인해 오류가 나는 경우 아래의 주석을 제거하고 진행
#chmod -R 777 $WHATAP_HOME

# 에이전트 구성에 필수적인 설정값으로 어플리케이션 배포 yaml 파일을 통해 주입해 설정합니다.
# yaml 작성 예제는 다음 섹션의 kubernetes 환경변수를 참고해 주세요
# license 는 와탭의 사용자 인증정보로 외부에 노출되면 안됩니다.
whatap-setting-config \
--host $whatap_server_host \
--license $license \
--app_name $app_name \
--app_process_name $app_process_name

# 아래 주석처리된 부분은 Optional 설정으로 필요한 경우에만 사용합니다.
# 이 외에도 로그, 트랜젝션 등의 설정을 할 수 있습니다.
# https://docs.whatap.io/python/introduction 해당 문서를 참고해 주세요

# 로그 수집 활성화
echo "logsink_enabled=true" >> whatap.conf
echo "logsink_trace_enabled=true" >> whatap.conf
echo "trace_logging_enabled=true" >> whatap.conf

## fastapi 에서는 사용자가 처리하지 못한 에러에 대한 코드추적이 가능 합니다. 에러 포인트를 트랜젝션 로그 탭에서 확인 할 수 있습니다.
echo "log_unhandled_exception=true" >> whatap.conf

# 어플리케이션과 함께 와탭 에이전트 실행
whatap-start-agent uvicorn server:app --host 0.0.0.0 --port 8000
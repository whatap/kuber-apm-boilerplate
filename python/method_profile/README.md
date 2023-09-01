## 소개
쿠버네티스 에이전트와 python-apm 연동
 
파이썬 method-profile application 을 쿠버네티스에 배포하고

와탭의 쿠버네티스 에이전트와 연동하는 샘플 코드

* 쿠버네티스 에이전트가 설치되어 있지 않은 경우 [와탭-쿠버네티스-설치](https://github.com/whatap/kuber-apm-boilerplate/blob/main/README.md) 를 참고 


### 설치 

## case 1(권장)
python-sample 이미지 사용
해당 이미지는 sns 의 데이터를 수집하고 Mount 된 경로에 데이터를 저장하는 서비스를 제공합니다.
따라서 검색하고자 하는 키워드를 yaml 에 입력해야합니다.

1. app_deployment.yaml 파일 {WHATAP_LICENSE}에 자신의 라이센스 키값 입력
2. app_deployment.yaml 파일 {WHATAP_SERVER_HOST}에 와탭 수집서버 IP 입력
3. {HASHTAG}에 어플리케이션을 통해 검색할 값을 입력하고 {HOST_MOUNT_PATH} 에 공유 디렉토리 경로 입력 
4. app 배포하기 

   ```
   kubectl apply -f app_deployment.yaml
   ```

## case 2
도커에 직접 생성한 이미지 사용하는 경우

1. app_deployment.yaml 파일 {WHATAP_LICENSE}에 자신의 라이센스 키값 입력
2. method profile 어플리케이션 도커 이미지 생성
    
    - entrypoint.sh 에 {WHATAP LICENSE} 에 자신의 라이센스 키 입력해야함.
   
    ```
    ##e.g) docker build -t whatap/whatap_method_profile:0.1.0 .
    docker build -t {docker_username}/{image_name}:{tag} .
    docker push {docker_username}/{image_name}:{tag}
    ```
   
3. method-profile 어플리케이션에 대한 yaml 파일 설정

   `아래 명령어에서 YOUR-IMAGE-NAME 을 위에서 생성한 이미지 이름 {docker_username}/{image_name}:{tag} 으로 변경하고 실행`

   - mac
     ```
     #e.g) sed -i '' 's/{APP-IMAGE-NAME}/whatap\/whatap_method_profile:0.1.0/g' app_deployment.yaml 
     
     sed -i '' 's/{APP-IMAGE-NAME}/YOUR-IMAGE-NAME/g' app_deployment.yaml
     
     ```

   - linux
     ```
     #e.g) sed -i 's/{APP-IMAGE-NAME}/whatap\/whatap_method_profile:0.1.0/g' app_deployment.yaml
     
     sed -i 's/{APP-IMAGE-NAME}/YOUR-IMAGE-NAME/g' app_deployment.yaml
     ``` 
   
4. app 배포하기

   ```
   kubectl apply -f app_deployment.yaml
   ```

   



  

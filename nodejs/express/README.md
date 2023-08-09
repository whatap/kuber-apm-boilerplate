## 소개
쿠버네티스 에이전트와 node-apm 연동
 
노드 application 을 쿠버네티스에 배포하고

와탭의 쿠버네티스 에이전트와 연동하는 샘플 코드

* 쿠버네티스 에이전트가 설치되어 있지 않은 경우 [와탭-쿠버네티스-설치](https://github.com/whatap/kuber-apm-boilerplate/blob/main/README.md) 를 참고 


### 설치 

## case 1(권장)
node-sample 이미지 사용

1. app_deployment.yaml 파일의 {WHATAP_LICENSE}에 자신의 라이센스 키값 입력하고, {WHATAP_SERVER_HOST}에 호스트 입력
2. app 배포하기 

   ```
   kubectl apply -f app_deployment.yaml
   ```

## case 2
도커에 직접 생성한 이미지 사용하는 경우

1. app_deployment.yaml 파일의 {WHATAP_LICENSE}에 자신의 라이센스 키값 입력하고, {WHATAP_SERVER_HOST}에 호스트 입력
2. express 어플리케이션 도커 이미지 생성
   
    ```
    ##e.g) docker build -t whatap/whatap_express:0.1.0 .
    docker build -t {docker_username}/{image_name}:{tag} .
    docker push {docker_username}/{image_name}:{tag}
    ```
   
3. express 어플리케이션에 대한 yaml 파일 설정

   `아래 명령어에서 YOUR-IMAGE-NAME 을 위에서 생성한 이미지 이름 {docker_username}/{image_name}:{tag} 으로 변경하고 실행`

   - mac
     ```
     #e.g) sed -i '' 's/{APP-IMAGE-NAME}/whatap\/whatap_express:0.1.0/g' app_deployment.yaml 
     
     sed -i '' 's/{APP-IMAGE-NAME}/YOUR-IMAGE-NAME/g' app_deployment.yaml
     
     ```

   - linux
     ```
     #e.g) sed -i 's/{APP-IMAGE-NAME}/whatap\/whatap_express:0.1.0/g' app_deployment.yaml
     
     sed -i 's/{APP-IMAGE-NAME}/YOUR-IMAGE-NAME/g' app_deployment.yaml
     ``` 
   
4. app 배포하기

   ```
   kubectl apply -f app_deployment.yaml
   ```

   



  

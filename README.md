## 소개
쿠버네티스와 apm 연동을 위한 샘플 어플리케이션 runtime 은 containerd 를 기준으로함

### 파일 구조
언어와 프레임워크 별로 구성됨

    language
        framework
    
    e.g)
    
    python
        fastapi
        django
    
    nodejs
        express
    
    java
        spring

### 쿠버네티스 에이전트 설치
WORK_DIR : ~/kuber-apm-boilerplate 

1.  라이센스 키 입력
    
    whatap_kube_containerd_1.16.yaml 파일의 {WHATAP_LICENSE}에 발급받은 라이센스 키 입력


2. yaml 파일 적용

    ```
    kubectl apply -f whatap_kube_containerd_1.16.yaml
    ```

### 쿠버 에이전트와 APM 에이전트 연동
APM 에이전트 설치, 연동은 각 언어별 README.md 를 참고


 

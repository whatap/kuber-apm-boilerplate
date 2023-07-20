## 소개
쿠버네티스와 apm 연동을 위한 샘플 어플리케이션

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

1. 아래 명령어 실행을 통해 yaml 파일에 발급받은 라이센스 키를 입력

    YOUR-LICENSE-KEY 를 발급받은 라이센스 키로 변경하고 아래의 명령어 실행

    - mac
       ```
       sed -i '' 's/{WHATAP_LICENSE}/YOUR-LICENSE-KEY/g' whatap_kube_containerd_1.16.yaml
       ```

    - 리눅스 
       ```
       sed -i 's/{WHATAP_LICENSE}/YOUR-LICENSE-KEY/g' whatap_kube_containerd_1.16.yaml
       ```

2. yaml 파일 적용

    ```
    kubectl apply -f whatap_kube_containerd_1.16.yaml
    ```

### 쿠버 에이전트와 APM 에이전트 연동
APM 에이전트 설치, 연동은 각 언어별 README.md 를 참고


 
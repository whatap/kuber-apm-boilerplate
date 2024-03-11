## 빌드
docker build -t whatap/kube_python_django:0.0.1 

## 실행
docker run -d -p 8000:8000 \
  -e license=x41pl22ek7jhv-z43cebasdv4il7-z62p3l35fj5502 \
  -e whatap_server_host=15.165.146.117 \
  -e app_name=test-django \
  -e app_process_name=python \
  whatap/kube_python_django:0.0.1

docker ps | grep whatap/kube_python_django:0.0.1

docker exec -it {container id} /bin/bash

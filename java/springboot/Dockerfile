FROM openjdk:8-jdk-slim
RUN mkdir -p /app && mkdir /whatap
WORKDIR /app
COPY --from=whatap/kube_mon /data/agent/micro/whatap.agent-*.jar /whatap
COPY whatap.conf /whatap/
COPY target/demo-0.0.1-SNAPSHOT.jar /app/
CMD ["java","-javaagent:/whatap/whatap.agent-2.2.9.jar","-Dwhatap.micro.enabled=true","-jar","/app/demo-0.0.1-SNAPSHOT.jar"]

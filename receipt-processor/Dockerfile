FROM openjdk:17-jdk
WORKDIR /app
COPY target/receipt-processor-0.0.1-SNAPSHOT.jar receipt-processor.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "receipt-processor.jar"]

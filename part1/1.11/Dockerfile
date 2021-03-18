FROM openjdk:8
WORKDIR /spring
COPY . .
RUN chmod 777 ./mvnw
RUN ./mvnw package
EXPOSE 8080
CMD [ "java", "-jar", "./target/docker-example-1.1.3.jar" ]
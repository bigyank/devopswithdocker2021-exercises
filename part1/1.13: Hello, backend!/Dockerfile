FROM golang:1.15
WORKDIR /backend
COPY . .
RUN go build
RUN go test ./...
ENV PORT=8080
EXPOSE 8080
CMD [ "./server" ]
FROM golang:alpine as build-stage
WORKDIR /backend
COPY . .
RUN apk add build-base && \
    go build && \
    go test ./...

FROM alpine
COPY --from=build-stage /backend/server ./server
RUN adduser -D appuser
USER appuser
CMD [ "./server" ]

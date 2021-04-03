FROM alpine
RUN apk add docker git

WORKDIR /auto
COPY builder.sh ./
RUN chmod u+x builder.sh

ENTRYPOINT [ "./builder.sh" ]

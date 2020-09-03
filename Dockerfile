FROM alpine:latest
ENV PYTHON_VERSION=3.7.3

RUN apk add --update python3 py-pip
RUN pip3 install boto3 \
        && ln -sv /usr/bin/python3 /usr/bin/python

COPY ./*lcp.py /

CMD ["python","./getlcp.py"]

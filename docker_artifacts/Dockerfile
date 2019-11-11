FROM python:3
LABEL maintainer=bensalemtaher@gmail.com
ARG DOCKER_ARTIFACT_DIR=./docker_artifacts

COPY ./code /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY $DOCKER_ARTIFACT_DIR/run.sh /bin
RUN  chmod +x /bin/run.sh

CMD ["/bin/run.sh"]

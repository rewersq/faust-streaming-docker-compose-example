FROM python:3.7.4-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get install -y netcat && apt-get autoremove -y

# Create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

WORKDIR /faust-project

COPY setup.py /faust-project/setup.py
RUN pip3 install -e .

COPY run.sh /faust-project/run.sh
COPY wait_for_services.sh /faust-project/wait_for_services.sh
COPY settings.py /faust-project/settings.py
COPY . /faust-project/faust_streaming




ENTRYPOINT ["./wait_for_services.sh"]

CMD ["./run.sh", "${WORKER}", "${WORKER_PORT}", "${CONFIG_CLASS}"]

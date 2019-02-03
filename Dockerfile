FROM python:3.6

WORKDIR /build

COPY ./docker/requirements_os.txt /build
RUN apt-get -y update && \
    apt-get -y --no-install-recommends install $(grep -vE "^\s*#" 'requirements_os.txt' | tr "\n" " ") && \
    apt-get -y install locales && \
    apt-get -y --purge autoremove && \
    apt-get -y autoclean

RUN pip install --no-cache-dir --upgrade pip
COPY ./reporter/requirements.txt /build
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /exec

COPY ./docker/*bootstrap*.sh /exec/

VOLUME '/static'

WORKDIR /code

COPY ./reporter /code

CMD ["/exec/bootstrap.sh"]

EXPOSE 8000
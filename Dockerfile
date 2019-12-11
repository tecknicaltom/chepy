FROM python:3.8.0

WORKDIR /chepy
COPY requirements.txt /chepy
RUN pip install -r /chepy/requirements.txt \
    && pip install python-magic virtualenv \
    && virtualenv -p python3 /chepy/venv \
    && /chepy/venv/bin/pip3 install -r requirements.txt \
    && pip install sphinx recommonmark pytest pytest-cov bandit

COPY . /chepy/
RUN cd /chepy && venv/bin/pip3 install .

RUN cd /chepy/ && pytest --disable-pytest-warnings --cov=chepy --cov-config=.coveragerc tests/
RUN cd /chepy/ && make -C docs/ clean html
RUN cd /chepy/ && bandit --recursive chepy/ --ignore-nosec --skip B101,B413,B303,B310,B112,B304,B320,B410,B404
RUN /chepy/venv/bin/pip3 uninstall -y pytest pytest-cov bandit


FROM python:3.8.0-slim
RUN apt update && apt install exiftool libmagic-dev -y
COPY --from=0 /chepy /chepy
WORKDIR /data
VOLUME ["/data"]

ENTRYPOINT ["/chepy/venv/bin/chepy"]

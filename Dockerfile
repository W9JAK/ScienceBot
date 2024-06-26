FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Etc/UTC

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-dev libpq-dev build-essential && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . /code

CMD ["python3", "titles/addtitlestobd.py"]

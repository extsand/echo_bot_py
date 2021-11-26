#Dockerfile example
FROM alpine:3.11

WORKDIR /usr/src/app
ARG telegram_bot_token
ENV TELEGRAM_bot_token=$telegram_bot_token

#file to .
COPY requirements.txt .
#all files to .
COPY . .


RUN apk add --no-cache python3 py3-pip \
		&& pip3 install --upgrade pip \
		&& pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 5000
CMD ["python3", "main.py"]


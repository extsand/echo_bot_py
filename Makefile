# More about Makefile
# https://guides.hexlet.io/makefile-as-task-runner/
# https://makefiletutorial.com/
# 
# Run example:
# export TELEGRAM_bot_token="sample:sample1234567890"
# make local-build TELEGRAM_bot_token=$TELEGRAM_bot_token


#VAR = value - required variable
#VAR ?= value - optional variable
# you can set optional var like arg 
## example: 
## make build-app APP_NAME=example

#app variables
APP_NAME ?= echo_bot
ENV_NAME ?= dev
APP_TAG ?= init
APP_IMAGE = $(AWS_REPOSITORY_NAME):$(APP_TAG)

#local var
LOCAL_PORT ?= 80
TELEGRAM_bot_token ?= 'xxxxxxxxxxxxxxxxxxxx'

#aws variables 
AWS_REGISTRY_ID ?= 530117518858
AWS_REPOSITORY_REGION ?= eu-central-1
AWS_PROFILE ?= academy
AWS_REPOSITORY_NAME = $(AWS_REGISTRY_ID).dkr.ecr.$(AWS_REPOSITORY_REGION).amazonaws.com/$(APP_NAME)-$(ENV_NAME)


#Set tasks:
#Using .PHONY for cover collision with Task names and File/folder names
#Task name: build-app
# - create docker image 
# - push docker image to aws elastic container registry
.PHONY:build-app
build-app:
	echo "Login aws ecr"
	$(MAKE) aws-ecr-login

	echo "Build task started"
	docker build -t $(APP_IMAGE) ./app/.
	docker push $(APP_IMAGE)
	echo "------ All task is done -------"

#Task name: aws-ecr-login 
# - log in to aws elastic container registry
# - for more about - read AWS CLI info
.PHONY:aws-ecr-login 
aws-ecr-login: 
	aws ecr get-login-password --region=$(AWS_REPOSITORY_REGION) | docker login --username AWS --password-stdin $(AWS_REGISTRY_ID).dkr.ecr.$(AWS_REPOSITORY_REGION).amazonaws.com





# local build docker image
.PHONY: local-build
local-build:
	$(MAKE) set_telegram_token
	echo "Create local build"
	docker build --build-arg telegram_bot_token=$(TELEGRAM_bot_token) -t $(APP_IMAGE) ./.
	$(MAKE) local-run 

# local run docker container
.PHONY: local-run
local-run:
	echo "local run for docker container"
	# for env variables
	# docker run -e $(TELEGRAM_bot_token) -it -p $(LOCAL_PORT):5000 $(APP_IMAGE)
	docker run -it -p $(LOCAL_PORT):5000 $(APP_IMAGE)

# work now
.PHONY: local-entrance
local-entrance:
	echo "local run and enter for docker container"
	docker exec -it $(shell docker ps | awk 'FNR == 2 {print $$1}') /bin/ash

#fix auto env
.PHONY:set_telegram_token
set_telegram_token:
	bash ./set_telegram_bot_token.sh
	$(shell ./set_telegram_bot_token.sh)

#debug mode for testing
.PHONY:debug-mode
debug-mode:
	echo "Debug mode!"
	env | grep 'bot'
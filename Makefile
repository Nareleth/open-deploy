# Target
VERSION		:= 0.01
TARGET		:= open-deploy
TAG			:= $(TARGET):$(VERSION)

# Conf
VMROOT		:= $(shell echo ~/vms)
BIN			:= bin
DEPLOY		:= $(bin)/opendeploy-cli.py
SERVER		:= server/server.py
ISO			:= resources/iso/*.iso

# Params
HOSTNAME	:= 127.0.0.1:8080
GUESTNAME 	:= test-vm

# Commands
CURL		:= curl
PYTHON		:= python3
DOCKER		:= docker

.PHONY: boot build clean create run

all: run

build:
	$(DOCKER) build -t $(TAG) .

run:
#	$(DOCKER) run -it -d -p 8080:8080 --name $(TARGET) $(TAG)
	$(PYTHON) $(SERVER)


api:
	$(CURL) -X GET $(HOSTNAME)/api

create:
	$(CURL) -X POST $(HOSTNAME)/api/createguest \
	-H "Content-Type: application/json" \
	-d '{"name": "test-vm", "memory": "1024", "cores": "2", "cdrom": "resources/iso/alpine-standard-3.22.2-x86_64.iso", "volume": "20G" }'

boot:
	$(CURL) -X POST $(HOSTNAME)/api/bootguest \
	-H "Content-Type: application/json" \
	-d '{"name": "test-vm"}'


clean:
	rm -rf $(VMROOT)
	$(DOCKER) stop $(TARGET)
	$(DOCKER) rm $(TARGET)
	$(DOCKER) image rm $(TAG)
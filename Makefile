VERSION		:= 0.01
TARGET		:= open-deploy
TAG			:= $(TARGET):$(VERSION)

VMROOT		:= $(shell echo ~/vms)
BIN			:= bin
DEPLOY		:= $(bin)/opendeploy-cli.py
SERVER		:= server/server.py
ISO			:= resources/iso/*.iso

GUESTNAME 	:= test
HOSTNAME	:= 127.0.0.1:8080

CURL		:= curl
PYTHON		:= python3
DOCKER		:= docker

.PHONY: boot build clean deploy run

all: run

build:
	$(DOCKER) build -t $(TAG) .

run:
#	$(DOCKER) run -it -d -p 8080:8080 --name $(TARGET) $(TAG)
	$(PYTHON) $(SERVER)


deploy:
#	$(PYTHON) $(DEPLOY) -c -n $(GUESTNAME) -m 1024 -cpu 2 -i $(ISO) -v 20G
	$(CURL) $(HOSTNAME)/newguest

boot:
	$(PYTHON) $(DEPLOY) -b $(GUESTNAME)

clean:
	rm -rf $(VMROOT)
	$(DOCKER) stop $(TARGET)
	$(DOCKER) rm $(TARGET)
	$(DOCKER) image rm $(TAG)
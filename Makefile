VERSION		:= 0.01
TARGET		:= open-deploy
TAG			:= $(TARGET):$(VERSION)
VMROOT		:= $(shell echo ~/vms)
GUESTNAME 	:= test
DEPLOY		:= deploy/opendeploy-cli.py
SERVER		:= server/server.py
ISO			:= ~/Downloads/ISO/alpine-standard-3.22.2-x86_64.iso

PYTHON		:= python3
DOCKER		:= docker

.PHONY: boot build clean deploy run

all: build run

build:
	$(DOCKER) build -t $(TAG) .

run:
	$(DOCKER) run -it -d -p 8080:8080 --name $(TARGET) $(TAG)


deploy:
	$(PYTHON) $(DEPLOY) -c -n $(GUESTNAME) -m 1024 -cpu 2 -i $(ISO) -v 20G

boot:
	$(PYTHON) $(DEPLOY) -b $(GUESTNAME)

clean:
	rm -rf $(VMROOT)
	$(DOCKER) stop $(TARGET)
	$(DOCKER) rm $(TARGET)
	$(DOCKER) image rm $(TAG)
VMROOT		:= $(shell echo ~/vms)
GUESTNAME 	:= test
DEPLOY		:= deploy/opendeploy-cli.py
SERVER		:= server/server.py


ISO			:= ~/Downloads/ISO/alpine-standard-3.22.2-x86_64.iso
PYTHON		:= python3

.PHONY: clean deploy run

all: deploy boot

deploy:
	$(PYTHON) $(DEPLOY) -c -n $(GUESTNAME) -m 1024 -cpu 2 -i $(ISO) -v 20G

boot:
	$(PYTHON) $(DEPLOY) -b $(GUESTNAME)


run:
	$(PYTHON) $(SERVER)

clean:
	rm -rf $(VMROOT)
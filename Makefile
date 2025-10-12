DEPLOY		:= deploy/opendeploy-cli.py
GUESTNAME 	:= test
ISO			:= ~/Downloads/ISO/alpine-standard-3.22.2-x86_64.iso
PYTHON		:= python3

.PHONY: clean deploy

all: deploy boot

deploy:
	$(PYTHON) $(DEPLOY) -c -n $(GUESTNAME) -m 1024 -cpu 2 -i $(ISO) -v 20G

boot:
	$(PYTHON) $(DEPLOY) -b $(GUESTNAME)

clean:
	rm *.qcow2
	rm *.json
DEPLOY	:= deploy/deploy-qemu.py
PYTHON	:= python3

.PHONY: clean deploy

deploy:
	$(PYTHON) $(DEPLOY) -n test -v 20


clean:
	rm *.qcow2
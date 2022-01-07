
.PHONY: install update test

install:
	pipenv run pip install -e .[all]

update:
	@ echo "TODO!"
	# pipenv run invenio-subjects-ddc-german

test:
	pipenv run ./run-tests.sh

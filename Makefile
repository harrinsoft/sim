clean:
	find . -name '*.py[co]' -delete
	rm -rf doc/build

virtualenv:
	virtualenv --prompt '|> sim <| ' venv
	venv/bin/pip install -r requirements-dev.txt
	venv/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete."
	@echo
	@echo "now type source venv/bin/activate"

test:
	pytest --cov=sim tests/

docs:
	python setup.py build_sphinx
	@echo
	@echo DOC: "file://"$$(echo `pwd`/docs/build/html/index.html)
	@echo

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

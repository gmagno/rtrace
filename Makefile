
# -- Setup ----------------------------#

.PHONY: clean
clean:
	rm -rf dist/ build/ nb_py.egg* && \
	find . \( -name __pycache__ \
		-o -name "*.pyc" \
		-o -name .pytest_cache \
		-o -name .eggs \
		-o -name rtrace.egg-info \
		-o -name dist \
		\) -exec rm -rf {} +\


build: clean
	python setup.py sdist

upload-dev:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload: build
	twine upload dist/*

# -- Development ----------------------#

.PHONY: test
test:
	pytest test

.PHONY: run
run:
	python rtrace/rtrace.py

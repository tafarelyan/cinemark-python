init:
	pip install -r requirements.txt -r requirements-dev.txt

publish:
	pip install 'twine>=1.5.0' wheel
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf build dist cinemark_python.egg-info

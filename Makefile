.SILENT:

clean:
	@echo "Cleaning up build and *.pyc files..."
	@find . -name '*.pyc' -exec rm -rf {} \;
	@rm -rf build
	
functional: clean
	@echo "Running simplexml functional tests..."
	@export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/simplexml  &&  \
		nosetests -s --verbose --with-coverage --cover-package=simplexml tests/functional/*

ci_functional: clean
	PYTHONPATH=`pwd`:`pwd`/simplexml PATH="/home/quatix/virtualenv/simplexml/bin:$PATH" \
		nosetests -s --verbose tests/functional/*

clean:
	@echo "Cleaning up build and *.pyc files..."
	@find . -name '*.pyc' -exec rm -rf {} \;
	@rm -rf build
	
unit: 
	@echo "Running simplexml unit tests..."
	@nosetests -s --verbose --with-coverage --cover-package=simplexml tests/unit/*

functional: 
	@echo "Running simplexml functional tests..."
	@nosetests -s --verbose --with-coverage --cover-package=simplexml tests/functional/*

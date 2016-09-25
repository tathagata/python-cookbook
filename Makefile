test:
	nosetests --with-coverage --cover-erase --cover-package=src --cover-html

debug:
	nosetests --pdb

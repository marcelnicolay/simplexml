SimpleXML - encoder/decoder
======================

SimpleXML is a simple and fast XML encoder/decoder for Python.
He use xml.dom.minidom present in python 2.6 or later

Installing
==========

On unix-based systems::
   sudo python setup.py install

On windows::
   python setup.py install

Basic usage
==========

	dictionary to XML

	>>> import simplexml
	>>> person = {'person':{'name':'joaquim','age':15,'cars':[{'id':1},{'id':2}]}}
	>>> simplexml.dumps(person)
	>>> '<?xml version="1.0" ?><person><cars><car><id>1</id></car><car><id>2</id></car></cars><age>15</age><name><![CDATA[joaquim]]></name></person>'

~~~~~~~~~~~~~

	XML to dictionary
	
	>>> import simplexml
	>>> person = simplexml.loads('<?xml version="1.0" ?><person><cars><car><id>1</id></car><car><id>2</id></car></cars><age>15</age><name>joaquim</name></person>')
	>>> person['person']['name']
	>>> u'joaquim'
	

Contributing
============

With new features
^^^^^^^^^^^^^^^^^

 1. Create both unit and functional tests for your new feature
 2. Do not let the coverage go down, 100% is the minimum.
 3. Write properly documentation
 4. Send-me a patch with: ``git format-patch``

E-mail: marcel.nicolay at gmail com

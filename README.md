SimpleXML - encoder/decoder
======================

![Travis CI](https://api.travis-ci.org/marcelnicolay/simplexml.png)

SimpleXML is a simple and fast XML encoder/decoder for Python.

# Basic usage

# dictionary to XML

```python
import simplexml
person = {'person':{'name':'joaquim','age':15,'cars':[{'id':1},{'id':2}]}}
simplexml.dumps(person)
'<?xml version="1.0" ?><person><cars><car><id>1</id></car><car><id>2</id></car></cars><age>15</age><name>joaquim></name></person>'
```

# XML to dictionary

```python
import simplexml
person = simplexml.loads('<?xml version="1.0" ?><person><cars><car><id>1</id></car><car><id>2</id></car></cars><age>15</age><name>joaquim</name></person>')
person['person']['name']
u'joaquim'
```
	
# Installing

```bash
$pip install python-simplexml
```

# Contributing

Fell free to contribute and send me a pull request.

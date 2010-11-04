import simplexml

def test_can_load_xml_string_with_cdata():
    docxml = "<someTag><name><![CDATA[Should be name]]></name></someTag>"
    response = simplexml.loads(docxml)

    assert response['someTag']['name'] == 'Should be name'

def test_can_loads():

    docxml = "<someTag><name>Should be name</name><itens><item><type>Should Be Type item1</type></item><item><type>Should Be Type item2</type></item></itens></someTag>"

    response = simplexml.loads(docxml)

    assert response['someTag']['name'] == 'Should be name'
    assert type(response['someTag']['itens']) == list
    assert response['someTag']['itens'][0]['type'] == 'Should Be Type item1'

def test_can_dumps():

    sometag = {'someTag':{'name':'Should be name', 'child':{'id':90},'itens':[{'type':'Should Be Type item1'},{'type':'Should Be Type item2'}]}}
    response = simplexml.dumps(sometag)

    assert response == '<?xml version="1.0" ?><someTag><itens><iten><type>Should Be Type item1</type></iten><iten><type>Should Be Type item2</type></iten></itens><name>Should be name</name><child><id>90</id></child></someTag>'

def test_can_dumps_diff_cdata():

    sometag = {'someTag':{'value':'hello world', 'scaped':'Should Be <b>bold</b>'}}
    response = simplexml.dumps(sometag)

    assert response == '<?xml version="1.0" ?><someTag><scaped><![CDATA[Should Be <b>bold</b>]]></scaped><value>hello world</value></someTag>'
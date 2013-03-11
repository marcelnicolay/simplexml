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


def test_can_loads_list_plural():

    docxml = "<someTag><name>Should be name</name><itens><item><type>Should Be Type item1</type></item><item><type>Should Be Type item2</type></item></itens></someTag>"

    response = simplexml.loads(docxml)

    assert response['someTag']['name'] == 'Should be name'
    assert type(response['someTag']['itens']) == list
    assert response['someTag']['itens'][0]['type'] == 'Should Be Type item1'


def test_can_loads_list_same_name():

    docxml = "<someTag><name>Should be name</name><item><type>Should Be Type item1</type></item><item><type>Should Be Type item2</type></item></someTag>"

    response = simplexml.loads(docxml)

    assert response['someTag']['name'] == 'Should be name'
    assert type(response['someTag']['item']) == list
    assert response['someTag']['item'][0]['type'] == 'Should Be Type item1'


def test_can_dumps():

    sometag = {'someTag': {'name': 'Should be name', 'child': {'id': 90}, 'itens': [{'type': 'Should Be Type item1'}, {'type': 'Should Be Type item2'}]}}
    response = simplexml.dumps(sometag)

    assert '<someTag><' in response
    assert '></someTag>' in response
    assert '<itens><iten><type>Should Be Type item1</type></iten><iten><type>Should Be Type item2</type></iten></itens>' in response
    assert '<name>Should be name</name>' in response
    assert '<child><id>90</id></child>' in response


def test_can_dumps_diff_cdata():

    sometag = {'someTag': {'value': 'hello world', 'scaped': 'Should Be <b>bold</b>'}}
    response = simplexml.dumps(sometag)

    assert '<someTag><' in response
    assert '></someTag>' in response
    assert '<scaped><![CDATA[Should Be <b>bold</b>]]></scaped>' in response
    assert '<value>hello world</value>' in response


def test_can_dumps_node_with_root_attr():

    sometag = {'someTag': {'_attrs': {'attr': 'value'}, 'name': 'Should be name', 'child': {'id': 90}, 'itens': [{'type': 'Should Be Type item1'}, {'type': 'Should Be Type item2'}]}}
    response = simplexml.dumps(sometag)

    assert '<someTag attr="value">' in response
    assert '<child><id>90</id></child>' in response
    assert '<itens><iten><type>Should Be Type item1</type></iten><iten><type>Should Be Type item2</type></iten></itens>' in response
    assert '<name>Should be name</name>' in response
    assert '</someTag>' in response


def test_can_dumps_with_list_non_plural():

    sometag = {'someTag': {'name': 'Should be name', 'child': {'id': 90}, 'item': [{'type': 'Should Be Type item1'}, {'type': 'Should Be Type item2'}]}}
    response = simplexml.dumps(sometag)

    assert '<item><type>Should Be Type item1</type></item><item><type>Should Be Type item2</type></item>' in response


def test_can_dumps_with_list_non_plural_with_attrs():

    sometag = {'someTag': {'name': 'Should be name', 'child': {'id': 90}, 'item': [{'_attrs': {'attr': 'value'}, 'type': 'Should Be Type item1'}, {'type': 'Should Be Type item2'}]}}
    response = simplexml.dumps(sometag)

    assert '<item attr="value"><type>Should Be Type item1</type></item><item><type>Should Be Type item2</type></item>' in response


def test_can_dumps_with_node_value():

    sometag = {'someTag': {'name': 'Should be name', 'child': {'id': 90}, 'item': [{'type': {'_attrs': {'id': 1}, '_value': 'Should Be Type item1'}}, {'type': 'Should Be Type item2'}]}}
    response = simplexml.dumps(sometag)

    assert '<item><type id="1">Should Be Type item1</type></item><item><type>Should Be Type item2</type></item>' in response
    assert '<name>Should be name</name>' in response
    assert '<child><id>90</id></child>' in response


def test_can_dumps_with_first_node_list():

    sometag = {'someTags': [{'someTag': {'nome': 'Should Be Nome'}}, {'someTag': {'nome': 'Should Be Nome'}}]}
    response = simplexml.dumps(sometag)

    assert '<someTags><someTag><nome>Should Be Nome</nome></someTag><someTag><nome>Should Be Nome</nome></someTag></someTags>' in response

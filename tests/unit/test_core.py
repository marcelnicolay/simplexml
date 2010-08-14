from mox import Mox
import simplexml

def test_can_loads():

    docxml = "<someTag><name>Should be name</name><itens><item><type>Should Be Type item1</type></item><item><type>Should Be Type item2</type></item></itens></someTag>"
    import pdb;pdb.set_trace()
    response = simplexml.loads(docxml)

    
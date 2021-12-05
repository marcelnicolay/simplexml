# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import re
from xml.dom.minidom import getDOMImplementation, parseString

def exclude_attrs_nodes_from_dict(data):
    if type(data) == dict:
        return {x: data[x] for x in data if x != '_attrs'}
    return data

def element_from_dict(document, elRoot, data):
    
    if type(data) == list:
        for item in data:
            element_from_dict(document, elRoot, item)
            
        return
        
    for k, v in data.items():
        
        if isinstance(v, dict):
            elem = document.createElement(k)

            if '_attrs' in v:
                for name,value in v["_attrs"].items():
                    elem.setAttribute(name, str(value))
           
            if '_value' in v:
                value = v.get('_value')
                textNode = document.createCDATASection(value) if isinstance(value, str) and re.search("[\<\>\&]", value) else document.createTextNode(str(value))
                elem.appendChild(textNode)

            else:
                element_from_dict(document, elem, exclude_attrs_nodes_from_dict(v))
                
            elRoot.appendChild(elem)

        elif isinstance(v, list):
            if k.endswith("s"):
                elem = document.createElement(k)
                for item in v:
                        elItem = document.createElement(k[0:len(k)-1])
                        element_from_dict(document, elItem, exclude_attrs_nodes_from_dict(item))
                        elem.appendChild(elItem)
                elRoot.appendChild(elem)
            else:
                for item in v:
                    elItem = document.createElement(k)
                    if '_attrs' in item:
                        for name,value in item["_attrs"].items():
                            elItem.setAttribute(name, str(value))

                    if '_value' in item:
                        value = item.get('_value')
                        textNode = document.createCDATASection(value) if isinstance(value, str) and re.search("[\<\>\&]", value) else document.createTextNode(str(value))
                        elItem.appendChild(textNode)
                    else:
                        element_from_dict(document, elItem, exclude_attrs_nodes_from_dict(item))

                    elRoot.appendChild(elItem)
                    
        elif isinstance(v, str) and re.search("[\<\>\&]", v):
            elem = document.createElement(k)
            elem.appendChild(document.createCDATASection(v))
            elRoot.appendChild(elem)
        else:
            elem = document.createElement(k)
            elem.appendChild(document.createTextNode(str(v)))
            elRoot.appendChild(elem)

def isNodeList(elem):

    if not elem.hasChildNodes() or len(elem.childNodes) < 2:
        return False

    # identify nodelists
    nodeListPattern = elem.childNodes[0].nodeName
    for node in elem.childNodes:
        if node.nodeName != nodeListPattern:
            return False
    return True

def dict_from_element(element, dic):

    if element.hasChildNodes():

        if isNodeList(element):
            nodeList = []
            for node in element.childNodes:
                nodeList.append(dict_from_element(node, {}))

            return nodeList
        else:
            for node in element.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    dic[element.nodeName] = node.nodeValue
                elif node.nodeType == node.CDATA_SECTION_NODE:
                    dic = node.nodeValue
                else:
                    if node.hasChildNodes and len(node.childNodes) == 1 and node.childNodes[0].nodeType == node.TEXT_NODE:
                        dic[node.nodeName] = node.childNodes[0].nodeValue
                    else:
                        if node.nodeName in dic:
                            if type(dic[node.nodeName]) != type([]):
                                dic[node.nodeName] = [dic[node.nodeName]]
                            dic[node.nodeName].append(dict_from_element(node, {}))
                        else:
                            dic[node.nodeName] = dict_from_element(node, {})

    return dic

def dumps(data):
    
    data_items = [(key, values) for key, values in data.items()]
    rootName, rootValue = data_items[0]
    implementation = getDOMImplementation()
    document = implementation.createDocument(None, rootName, None)

    rootNode = document.documentElement
    if type(rootValue) == dict and '_attrs' in rootValue:
        for name,value in rootValue["_attrs"].items():
            rootNode.setAttribute(name, value)      

    if type(rootValue) == dict and '_value' in rootValue:
        # Handles case where root node contains single text node - allowing for attribute definition and CDATA handling
        value = rootValue.get('_value')
        textNode = document.createCDATASection(value) if isinstance(value, str) and re.search("[\<\>\&]", value) else document.createTextNode(str(value))
        rootNode.appendChild(textNode)
        # Text  or CDATA node cannot have children
        return document.toxml()


    if type(rootValue) == str:
        # Handles case where root node contains single text node - simple case not allowing for attribute definition
        text = document.createTextNode(rootValue)
        rootNode.appendChild(text)
        return document.toxml()
    
    element_from_dict(document, rootNode,  exclude_attrs_nodes_from_dict(rootValue))

    return document.toxml()

def loads(data):

    document = parseString(data)
    rootNode = document.documentElement

    dictionary = {}
    dictionary[rootNode.nodeName] = dict_from_element(rootNode, {})

    return dictionary

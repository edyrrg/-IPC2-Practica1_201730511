import xml.etree.ElementTree as elementTree


def lector_xml_file(path):
    tree = elementTree.parse(path)
    root = tree.getroot()
    data = {}
    for el in root:
        data[el.tag] = "\t    " + str(el.text).strip()
    return data

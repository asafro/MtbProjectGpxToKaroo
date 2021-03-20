#!/usr/bin/python

import xml.etree.ElementTree as ET
import argparse

def printTree(child, indent=""):
    print indent + "tag: " + child.tag

    for c in child.getchildren():
        printTree(c, indent+"  ")


def removeTime(child):
    if child is None:
        return

    for c in child.getchildren():
        if c.tag == '{http://www.topografix.com/GPX/1/1}time':
            child.remove(c)
    for c in child.getchildren():
        removeTime(c)

def targetFileName(filename):
    if not filename:
        return
    return filename[:-4] + "_mtbproject" + filename[-4:]



parser = argparse.ArgumentParser(description='Transform for GPX files from MTB Project to Karoo2')
parser.add_argument('--mtbp', type=argparse.FileType('r'), required=True)
args = parser.parse_args()

print "Loading GPX from MTB project: " + args.mtbp.name

tree = ET.parse(args.mtbp)
root = tree.getroot()

print "Fixing GPX..."
removeTime(root)

print "Storing happy GPX to: ", targetFileName(args.mtbp.name)
with open(targetFileName(args.mtbp.name), 'wb') as f:
    tree.write(f)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
def unique_list(l):
    ulist = []
    [ulist.append(x.lower()) for x in l.split() if x not in ulist]
    return ulist
class Item():
	"""
	Item class has methodes allowing adding an attribute and modifying an attribute
	"""
	def __init__(self, name, price):
		self._attributes = {'price':price,
							'name': name}
	
	def addAttr(self, attrName, attrValue):
		if not attrName in self._attributes.keys():
			self._attributes[attrName] = attrValue
			print 'True'
			return True
		else:
			print 'Attribute already exists'
			return False
	def changeAttr(self, attrName, attrValue):
		if not attrName in self._attributes.keys():
			print 'Attribute doesn\'t exist'
			return False
		else:
			self._attributes[attrName] = attrValue	
			print 'True'
			return True
	def tokenizeDescription(self):
		if 'description' in self._attributes.keys():
			return unique_list(self._attributes['description'])
		
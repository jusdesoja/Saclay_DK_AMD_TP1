#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
			print 'Trues'
			return True
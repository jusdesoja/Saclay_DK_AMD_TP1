#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Item():
	def __init__(self, name, price):
		self._attribute = {'Price':price,
							'Name': name}
	
	def addAttr(self, attrName, attrValue):
		if attrName in self._attribute.keys():
			self._attribute[attrName] = attrValue
			print 'True'
			return True
		else:
			print 'Attribute already exists'
			return False
	def changeAttr(self, attrName, attrValue):
		if not attrName in self._attribute.keys():
			print 'Attribute doesn\'t exist'
			return False
		else:
			self._attribute[attrName] = attrValue	
			print 'Trues'
			return True
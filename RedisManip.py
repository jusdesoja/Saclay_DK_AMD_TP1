#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from Item import Item
class Redis:
	def __init__(self, host = 'localhost', port = 6379 , db = 0):
		self.redisServer = redis.StrictRedis(host = host, port = port, db = db )
		
	def hashAddItem(self, instanceItem):
		for attribute in instanceItem._attributes.keys():
			if attribute != 'name':
				result = self.redisServer.hset(instanceItem._attributes['name'],attribute,instanceItem._attributes[attribute])
				print attribute +' '+str(instanceItem._attributes[attribute])+ ' '+ str(result)
		if 'category' in instanceItem._attributes.keys():
			self.redisServer.publish(instanceItem._attributes['category'],'New Item'+instanceItem._attributes['name']+' added!')
		self.redisServer.expire(instanceItem._attributes['name'], 360)
		
	def hashGetItem(self, itemName):
		attribute = {}
		try:
			for key in self.redisServer.hkeys(itemName):
				attribute[key] = self.redisServer.hget(itemName,key)
				print '%s : %s' % (key, attribute[key])
			return attribute
		except:
			print 'No such name'
			return False
'''
r = Redis()
ITEM = Item('bike1', 75)
ITEM.addAttr('category','bike')
r.hashAddItem(ITEM)	
'''
	
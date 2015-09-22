#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import RedisManip
from Item import Item
class GUInterface():
	def __init__(self, parent):
		self.Redis = RedisManip.Redis()
		
		self.parent = parent
		self.parent.wm_title('RedisServer')
		self.parent.grid()
		
		self.MainFrame = tk.Frame(self.parent, height = 500, width = 300)
		self.MainFrame.pack(side = tk.BOTTOM)
		self.NameLabel = tk.Label(self.MainFrame, text ='Name')
		self.NameLabel.grid(column = 0, row = 0)		
		self.NameEntry = tk.Entry(self.MainFrame, width = 15)
		self.NameEntry.grid(column = 1, row = 0)
		
		self.PriceLabel = tk.Label(self.MainFrame, text ='Price')
		self.PriceLabel.grid(column = 0, row = 1)
		self.PriceEntry = tk.Entry(self.MainFrame, width = 15)
		self.PriceEntry.grid(column = 1, row = 1)
		self.CategoryLabel = tk.Label(self.MainFrame, text ='Category')
		self.CategoryLabel.grid(column = 0, row = 2)
		self.CategoryEntry = tk.Entry(self.MainFrame, width = 15)
		self.CategoryEntry.grid(column = 1, row = 2)
		self.CityLabel = tk.Label(self.MainFrame, text ='City')
		self.CityLabel.grid(column = 0, row = 3)
		self.CityEntry = tk.Entry(self.MainFrame, width = 15)
		self.CityEntry.grid(column = 1, row = 3)
		self.MiscAttrLabel = tk.Label(self.MainFrame, text ='Misc Attr:')
		self.MiscAttrLabel.grid(column = 0, row = 4)
		self.MiscValueLabel = tk.Label(self.MainFrame, text ='Misc Value:')
		self.MiscValueLabel.grid(column = 1, row = 4)
		self.MiscAttrEntry = tk.Entry(self.MainFrame, width = 15)
		self.MiscAttrEntry.grid(column = 0, row = 5)
		self.MiscValueEntry = tk.Entry(self.MainFrame, width = 15)
		self.MiscValueEntry.grid(column = 1, row = 5)
		
		self.EntryDict = {	'price':self.PriceEntry,
			 				'category':self.CategoryEntry, 
							'city':self.CityEntry}
		
		self.SubmitButton = tk.Button(self.MainFrame, text = 'submit',width = 10, command = self.SubmitClicked)
		self.SubmitButton.grid(column = 0, columnspan = 2, row = 6)
		
		self.InfoMsg = tk.Label(self.MainFrame, text = "Info", width = 30 )
		self.InfoMsg.grid(column = 0, row = 7, columnspan = 2)
	
	
	def SubmitClicked(self):
		
		if self.NameEntry.get() != '' and self.PriceEntry.get() != '':
			newItem = Item(self.NameEntry.get(), self.PriceEntry.get())
			print self.NameEntry.get() + self.PriceEntry.get()
			for entryElement in self.EntryDict.keys():
				if self.EntryDict[entryElement].get() != '':
					print self.EntryDict[entryElement].get()
					newItem.addAttr(entryElement.lower(), self.EntryDict[entryElement].get())
			if self.MiscAttrEntry.get() != '':
				newItem.addAttr(self.MiscAttrEntry.get().lower(), self.MiscValueEntry.get())
				if 'description' == self.MiscAttrEntry.get().lower():
					self.Redis.setAddAllDescriptionKeywords(newItem.tokenizeDescription(),newItem._attributes['name'])
		self.Redis.hashAddItem(newItem)
		
			 
	
if __name__ == '__main__':
	try:
		root = tk.Tk()
		app = GUInterface(root)
		root.mainloop()
	except Exception, e:
		print e
	finally:
		pass		
		
	
		
		
		

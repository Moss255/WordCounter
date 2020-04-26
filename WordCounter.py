import tkinter as tk
from tkinter import filedialog
import sys
import csv

root = tk.Tk()
root.withdraw()

frequencyTable = {}

def findFile():
	filepath = ''
	print('Please point to file')
	while filepath == '':
		filepath = filedialog.askopenfilename()
		if filepath != '':
			print('Please select a file - press Ctrl-C to quit')
	print('Opening file')
	return filepath

def calcFrequency(file):
	with open(file, 'r', encoding='utf-8-sig') as f:
		for line in f.readlines():
			words = line.split()
			if words:
				for word in words:
					if word in frequencyTable:
						frequencyTable[word] += 1
					else:
						frequencyTable[word] = 1

def outputToFile():
	file = filedialog.asksaveasfile(initialdir = '/', title='select file', filetypes = (('CSV files', '*.csv'),))
	print('outputting to:', file.name)
	with open(file.name, 'w', newline='', encoding='utf-8-sig') as f:
		fields = ['Word Used', 'Frequency']
		writer = csv.DictWriter(f, fieldnames=fields)
		writer.writeheader()
		for key, value in frequencyTable.items():
			writer.writerow({'Word Used':key,'Frequency':value})
				
if __name__ == '__main__':
	calcFrequency(findFile())
	outputToFile()


        





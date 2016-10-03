import urllib
#import requests
import bs4
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib import request
l = raw_input("Enter a URL")
connection = request.urlopen(l)
source = connection.read()
soup = BeautifulSoup(source, "html.parser")
anchor = 0
for i in soup.findAll('a'):
	anchor += 1
totcount,divcount,spancount = 0
for k in soup.findAll():
	totcount += 1
for i in soup.findAll('div'):
	divcount += 1 
for j in soup.findAll('span'):
	spancount += 1
objects = {'div', 'span', 'total', 'anchor'}
y_pos = np.arrange(len(objects))
performance = [divcount, spancount, totcount,anchor]
plt.bar(y_pos, performance, align = 'center', alpha = 0.5)
plt.xticks(y_pos, objects)
plt.ylabel("Number of tags")
plt.title("Comparison of number of different tags wrt to total")
plt.show()


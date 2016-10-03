from urllib import request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

url = str(input("Enter the url to be scraped"))
connection = request.urlopen(url)
source = connection.read()
soup = BeautifulSoup(source, "html.parser")
div_count = 0
span_count = 0
total = 0
anchor = 0
for anch in soup.findAll('a'):
    # print(div)
    anchor += 1

for tot in soup.findAll():
    # print(div)
    total += 1

for div in soup.findAll('div'):
    # print(div)
    div_count += 1

for span in soup.findAll('span'):
    # print(span)
    span_count += 1

print('anchor tags = ', anchor)
print('span tags = ', span_count)
print('div tags = ', div_count)
print('total tags = ', total)


objects = ('total', 'div', 'span', 'anchors')
# values in vertical axis
y_pos = np.arange(len(objects))
# Return evenly spaced values within a given interval.
performance = [total, div_count, span_count, anchor]

plt.bar(y_pos, performance, align='center', alpha=0.5)
# bar graph with performance and y_pos
plt.xticks(y_pos, objects)
plt.ylabel('Number of tags')
# name of y axis
plt.title('Individual tags vs Total tags')
# title of the graph

plt.show()




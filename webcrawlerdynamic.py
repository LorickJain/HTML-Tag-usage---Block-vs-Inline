#Starting same as normal static WEB CRAWLER
from urllib import request
from bs4 import BeautifulSoup

def spider(max_pages):
    page=1
    while page <= max_pages:
        Url= 'https://thenewboston.com/search.php?type=1&sort=pop&page=' + str(page)
        response= request.urlopen(Url)
        source = response.read()
        soup = BeautifulSoup(source, "html.parser")
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = 'https://thenewboston.com/' + link.get('href')
            # print(href)
            title = link.string
            print(title)
            gather_data_from_link(href)

        page += 1

#As we get the link(above)..we can go to that link and gather all the links from there!!!

def gather_data_from_link(username_url):
    url = username_url
    response = request.urlopen(url)
    Source = response.read()
    Soup= BeautifulSoup(Source, "html.parser")
    for item in Soup.findAll('a'):#All links,no particular class
        href = "https://thenewboston.com/" + item.get('href')
        print(href)


pgs = raw_input("Enter number of pages")
spider(pgs)

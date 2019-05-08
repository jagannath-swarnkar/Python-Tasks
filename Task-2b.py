# importing modules required for this task
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# requesting the homepage of imdb and finding the divs 
page = requests.get('https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht')
soup = BeautifulSoup(page.text, 'html.parser')
main_div = soup.find('table',class_="chart full-width")
tbody = main_div.find('tbody')
trs = tbody.findAll('tr')

# storing the movie name and url in separate lists
movie_list = []
url_list = []
index=1
for tr in trs:
    td = tr.find('td',class_='titleColumn')
    name = td.text.strip()
    movie_list.append(name)
    url_list.append('https://imdb.com'+td.a['href'])
    print(index, name)
    index+=1
print()
# input from user and use loop in user range and request one by on url 
user1 = int(input('Enter the numbers of movie to see Cast list : '))
print()

# request url using selenium and open on browser to find the url of cast page and add with homepage url
for link in range(user1):
    driver = webdriver.Chrome()
    driver.get(url_list[link])
    page = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(page,'html.parser')
    driver.close()

    main_div = soup.find('div',attrs={'class':'article','id':'titleCast'})
    div2 = main_div.find('div',class_='see-more').a['href']
    url = url_list[link]+'/'+div2

    # again request the cast page url and find the name of actiors
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    main_div = soup.find('table',class_='cast_list')

    trs = main_div.findAll('tr',class_=True)
    index1 = 1
    print()
    print('Movie Name :',movie_list[link])
    print('--------------------------')
    print('Actors Name----')
    print('--------------------------')
    
    for i in range(len(trs)):
        td = trs[i].find('td',class_='')
        print(' '+(str(index1)+'      ')[:5]+td.text.strip())
        index1+=1
    print()
    
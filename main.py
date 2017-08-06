import requests
from lxml import html
from bs4 import BeautifulSoup

payload = {
	"username":	"f2016504",
	"password":	"Shanu05%",
	"rememberusername":	"1",
	"anchor":	""
	}

session_requests=requests.session()
login_url= "http://id.bits-hyderabad.ac.in/moodle/login/index.php"
result= session_requests.get(login_url)
result=session_requests.get("http://id.bits-hyderabad.ac.in/moodle/my/index.php?mynumber=-2")

result = session_requests.post(
	login_url,
	data= payload,
	headers= dict(referer=login_url)
	)

#print(result.content)
soup= BeautifulSoup(result.content, 'html.parser')
#print(soup.prettify())

content_soup=soup.find('div',class_='content')

list_=content_soup.find_all('h2',class_='title', recursive= True)
for item in list_:
	print(item.a['title'])

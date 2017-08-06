import requests
from bs4 import BeautifulSoup
from getpass import getpass
#fetching username and password form user
username=input("Enter username:")
password=getpass("Enter password:")
#creating payload for login
payload = {
	"username":	username,
	"password":	password,
	"rememberusername":	"1",
	"anchor":	""
	}
#creating a session
session_requests=requests.session()
#url of CMS@BPHC
login_url= "http://id.bits-hyderabad.ac.in/moodle/login/index.php"
result= session_requests.get(login_url)
#url for showing hidden courses
result=session_requests.get("http://id.bits-hyderabad.ac.in/moodle/my/index.php?mynumber=-2")
#using the payload for logging in
result = session_requests.post(
	login_url,
	data= payload,
	headers= dict(referer=login_url)
	)
#parsing the webpage
soup= BeautifulSoup(result.content, 'html.parser')

#login check
if soup.head.title.get_text()=='Dashboard':
#if login successful
	print('Login Successful \n \n')
#searching for all course titles and printing them
	content_soup=soup.find('div',class_='content')
	list_=content_soup.find_all('h2',class_='title', recursive= True)
	for item in list_:
		print(item.a['title'])
		
#if login failed
else:
	print("Error logging in. Please retry")


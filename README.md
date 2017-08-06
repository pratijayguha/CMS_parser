This is a program to print the courses enrolled in CMS.

It uses requests and BeautifulSoup for scraping the Webpage and getpass to get password input.

The program takes username and password as input from the user and creates a payload to be used later on. Then the web page is accessed through requests and payload is used to login. BeautifulSoup is used to scrape the webpage. There is a log in verification that checks for the title 'Dashboard' in header text. Once successful login has been confirmed, it searches for the course titles and prints them.

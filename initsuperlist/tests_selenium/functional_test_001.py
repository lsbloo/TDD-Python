from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://localhost:8000")

#result = 'Django' in browser.title
#print(result)
assert 'To-Do' in browser.title
from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.PhantomJS()
	browser.implicitly_wait(10)
	browser.get('https://h-o-r-n-g-r-y.tumblr.com/')
	time.sleep(5) 
	print ("crawling")

	
	imgs=browser.find_elements_by_tag_name('img')

	print ("reading")
	for img in imgs:
		print (img.get_attribute('src'))
		a = open("news.txt", "a")
		a.write("\n"+img.get_attribute('src'))
		a.close()

	c = browser.page_source
	p = open("cat.html", "w")
	p.write(c)
	p.close()

	print ("Linkfile generated")
	os.system('sh reader.sh')
	print ("Downloading....")
	os.system('wget -i news.txt')
	os.system('rm cat.html news.txt')
	print ("READY, WAITING FOR NEW INTERVAL")


fa_login()

from selenium import webdriver

chromeBrowser = webdriver.Chrome('./chromedriver')

chromeBrowser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chromeBrowser.title



#close
chromeBrowser.close()

#chromeBrowser.quit()

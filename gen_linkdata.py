from selenium import webdriver
import time

loginurl = 'https://passport2.chaoxing.com/login?fid=22169&refer=http://i.mooc.chaoxing.com'

user="username"
password="password"

firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("plugin.state.flash", 2)
driver = webdriver.Firefox(firefoxProfile,executable_path="/home/lq/shua/geckodriver")

driver.get(loginurl)  
driver.find_element_by_id('unameId').send_keys(user)
driver.find_element_by_id('passwordId').send_keys(password)
driver.find_element_by_class_name('zl_btn_right').click()
courseurl=input()
driver.get(courseurl)
ls=driver.find_elements_by_class_name("articlename")
ls=[l.find_element_by_tag_name("a").get_attribute("href") for l in ls]
with open("linkdata","w") as f:
  for l in ls:
    f.write("%s\n"%(l,))

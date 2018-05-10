from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image
import pytesseract

from_lesson=1

loginurl = 'https://passport2.chaoxing.com/login?fid=22169&refer=http://i.mooc.chaoxing.com'

user="username"
password="password"

uni_x=480

def get_time(img):
    a=img.crop((162,513,170,532))
    b=img.crop((170,513,178,532))
    a=a.resize((50,100),Image.ANTIALIAS)
    b=b.resize((50,100),Image.ANTIALIAS)
    for i in range(a.size[0]):
        for j in range(a.size[1]):
            if(sum(a.getpixel((i,j))[:3])<200):
                a.putpixel((i,j),(255,255,255,255))
            else:
                a.putpixel((i,j),(0,0,0,255))
    for i in range(b.size[0]):
        for j in range(b.size[1]):
            if(sum(b.getpixel((i,j))[:3])<200):
                b.putpixel((i,j),(255,255,255,255))
            else:
                b.putpixel((i,j),(0,0,0,255))
    text=pytesseract.image_to_string(a, config='-psm 10 digits')
    text+=pytesseract.image_to_string(b, config='-psm 10 digits')
    print(text)
    text=6+(int(text)+1)*6
    return text if text<150 else 150

def check(img):
    p1=img.getpixel((100,5))
    p2=img.getpixel((102,7))
    if((p1[0]==0)and(p1[1]==0)and(p1[2]==0)and(p2[0]==0)and(p2[1]==0)and(p2[2]==0)):
        return False
    return True

def is_running(img):
    p=img.getpixel((21,523))
    return p==(0,0,0,255)

def find_submit(img):
    l=[img.getpixel((uni_x,i)) for i in range(200,460)]
    for ind,i in enumerate(l):
        if((i[0],i[1],i[2])==(102,102,102)):
            if((i==l[ind+1])and(i==l[ind+3])and(i==l[ind+7])):
                btn_y=ind+220
                cho_y=[i for i in range(btn_y-75,100,-50)]
                return btn_y,cho_y

firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("plugin.state.flash", 2)
driver = webdriver.Firefox(firefoxProfile,executable_path="/home/lq/shua/geckodriver")
with open("linkdata","r") as f:
  links=f.readlines()

driver.get(loginurl)  
driver.find_element_by_id('unameId').send_keys(user)
driver.find_element_by_id('passwordId').send_keys(password)
input()
driver.find_element_by_class_name('zl_btn_right').click()

for link in links[from_lesson-1:]:
    driver.get(link)
    time.sleep(2)
    driver.switch_to.frame('iframe')
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
    ele=driver.find_element_by_id("ext-gen1038")
    time.sleep(2)

    action_chains = ActionChains(driver)
    action_chains.move_to_element_with_offset(ele,50,50).click().perform()
    time.sleep(4)
    driver.save_screenshot("figure/imgtime.png")
    img=Image.open("figure/imgtime.png")
    try:
        slot=get_time(img)
        print("choose slot %d"%(slot,))
    except:
        slot=100

    time.sleep(2)
    action_chains = ActionChains(driver)
    action_chains.move_to_element_with_offset(ele,50,50).click().perform()

    for i in range(slot):
        time.sleep(10)
        driver.save_screenshot("figure/img%d.png"%(i,))
        img=Image.open("figure/img%d.png"%(i,))
        if check(img):
            print("it's a checkpoint\n")
            sbmt,chol=find_submit(img)
            print(chol)
            for cho in chol:
                print("i click %d and %d\n"%(cho,sbmt))
                action_chains = ActionChains(driver)
                action_chains.move_to_element_with_offset(ele,uni_x,cho).click()
                action_chains.move_to_element_with_offset(ele,uni_x,sbmt).click().perform()
                time.sleep(1)
            action_chains = ActionChains(driver)
            action_chains.move_to_element_with_offset(ele,uni_x,sbmt).click().perform()
            print("handle over, is it alright?")
        elif not is_running(img):
            action_chains = ActionChains(driver)
            action_chains.move_to_element_with_offset(ele,50,50).click().perform()
#driver.switch_to.default_content()
#driver.switch_to.frame('PageFrame')


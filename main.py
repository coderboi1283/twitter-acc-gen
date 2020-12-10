import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
import math
import string
import time
import random 
import string

print('DISCLAIMER: only works for gmail accounts right now')
emailAccounts = open("gmail.txt",'r')
emailCount = 0
emailNum = 0
contents = emailAccounts.read()
coList = contents.split('\n')
for i in coList:
    if i:
        emailCount += 1
print('Successfully imported', emailCount, 'Gmail accounts')
accNum = emailAccounts.readlines()

def fakeName():
    
    fTXT = open('First.txt').read().splitlines()
    fName = random.choice(fTXT)

    lTXT = open('lastnames.txt').read().splitlines()
    lName = random.choice(lTXT)
    fakeNAME = fName + ' ' + lName
    return fakeNAME

fakeNAME = fakeName()

    
def Password():
    password_length = 18
    password_characters = string.ascii_letters + string.digits + string.punctuation

    for x in range(password_length):
        password = random.choice(password_characters)
    return password
password = Password()




driver = webdriver.Chrome('./chromedriver.exe')
'''chrome_options = Options()  
chrome_options.add_argument("--headless")  '''
driver.get('https://twitter.com/i/flow/signup')
time.sleep(0.75)
name = driver.find_element_by_name('name')
name.send_keys(fakeNAME)
time.sleep(0.5)
emailSet = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div.css-18t94o4.css-901oao.r-k200y.r-1n1174f.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-19h5ruw.r-bcqeeo.r-qvutc0')
emailSet.click()
time.sleep(0.5)
emailaccount = coList[emailNum]
emailacc = emailaccount.split(':')

email = driver.find_element_by_name('email')
email.send_keys(emailacc[0])
birthMonthID = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div.css-1dbjc4n.r-6ity3w > div.css-1dbjc4n > div > div.css-1dbjc4n.r-1uaug3w.r-cyik6v.r-wgabs5.r-1jkafct.r-1yadl64.r-16xksha.r-zso239.r-utggzx > div.css-1dbjc4n.r-bnwqim > select')

bmth = Select(birthMonthID)
bmth.select_by_visible_text('June')
time.sleep(0.5)

birthDayID = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div.css-1dbjc4n.r-6ity3w > div.css-1dbjc4n > div > div.css-1dbjc4n.r-1uaug3w.r-cyik6v.r-wgabs5.r-1jkafct.r-1yadl64.r-16y2uox.r-zso239.r-utggzx > div.css-1dbjc4n.r-bnwqim > select')
bd = Select(birthDayID)
bd.select_by_value('18')

birthYearID = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div.css-1dbjc4n.r-6ity3w > div.css-1dbjc4n > div > div:nth-child(3) > div.css-1dbjc4n.r-bnwqim > select')
by = Select(birthYearID)
by.select_by_value('1988')
time.sleep(1)
buttonOne = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-1h3ijdo.r-136ojw6 > div > div > div > div.css-1dbjc4n.r-obd0qt.r-1pz39u2.r-1t2qqvi.r-16y2uox.r-1wbh5a2.r-1777fci.r-1joea0r.r-1vsu8ta.r-18qmn74 > div > div > span > span')
buttonOne.click()
time.sleep(1.5)
buttonTwo = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-1h3ijdo.r-136ojw6 > div > div > div > div.css-1dbjc4n.r-obd0qt.r-1pz39u2.r-1t2qqvi.r-16y2uox.r-1wbh5a2.r-1777fci.r-1joea0r.r-1vsu8ta.r-18qmn74 > div > div > span > span')
buttonTwo.click()
time.sleep(1.5)
buttonThree = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-19h5ruw.r-1jayybb.r-17bavie.r-1ny4l3l.r-15bsvpr.r-o7ynqc.r-6416eg.r-lrvibr > div')
buttonThree.click()
print('Please check the email', emailacc[0],'for the twitter access Code')
time.sleep(3)
accountCode = int(input('please enter the account code found in gmail:  '))
verifyaccount = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1w50u8q > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')
verifyaccount.send_keys(accountCode)
time.sleep(0.5)
buttonFour = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-19h5ruw.r-1jayybb.r-17bavie.r-1ny4l3l.r-15bsvpr.r-o7ynqc.r-6416eg.r-lrvibr > div')
buttonFour.click()
time.sleep(1.5)
passWrdInput = driver.find_element_by_name('password')
passWrdInput.send_keys(password)
buttonFive = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-19h5ruw.r-1jayybb.r-17bavie.r-1ny4l3l.r-15bsvpr.r-o7ynqc.r-6416eg.r-lrvibr > div')
buttonFive.click()

accountWrite = open('twitter accounts.txt','w')
generatedAccountLine = emailacc[0]+':'+fakeNAME+':'+password
##layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-yfoy6g.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-1h3ijdo.r-136ojw6 > div > div > div > div.css-1dbjc4n.r-obd0qt.r-1pz39u2.r-1t2qqvi.r-16y2uox.r-1wbh5a2.r-1777fci.r-1joea0r.r-1vsu8ta.r-18qmn74 > div > div > span > span
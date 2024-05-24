import time

from selenium import webdriver
from selenium.webdriver.common.by import By


w=4
v="s"+str(w)+"s"
print(v)

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/InOManiak")

time.sleep(5)

reg=driver.find_element(By.CSS_SELECTOR,".x8hhl5t > div:nth-child(2) > div:nth-child(1)")
reg.click()

log=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
log.click()
a=0
while a!=7:
    driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")   #scrol down
    a+=1
    print("scroll",str(a))
    time.sleep(2)

tab=[]
b=0

while b!=10:                #pobranie z po xpath
    b+=1
    xpath="/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div["+str(b)+"]"  #ścieżka w html facebook czasem się zmienia
    #print(xpath)
    date=driver.find_element(By.XPATH,xpath)
    tab.append(date.text)
    print("pobrany post",str(b))


a=0

for x in tab:
    a+=1
    print("--------post ",str(a),"----------------------------------------------------")
    print(x)

driver.quit()

#program właściwie pobiera posty z fb
#teraz trzeba wyekstaraktować dane z posta i będzie śmiegać


#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div[1]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div[2]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div[3]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[2]/div/div[6]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div[1]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div/div[5]
#piwo
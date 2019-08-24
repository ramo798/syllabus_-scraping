from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

def Scraping(v):
    url = 'http://syllabus.center.wakayama-u.ac.jp/ext_syllabus/syllabusSearchDirect.do?nologin=on'
    driver.get(url)
    sleep(5)
    driver.find_element_by_xpath("/html/body/form/table[3]/tbody/tr/td[2]/img[1]").click()
    sleep(5)

    if v == 0:
        Scrapingmain(2,10)

    driver.quit()

def Scrapingmain(a,b):
    for num in range(a,b):
        num = str(num)

        tmp = "/html/body/table[3]/tbody/tr/td/table/tbody/tr[" + num + "]/td[1]"
        major = driver.find_element_by_xpath(tmp).text.replace('シラバス', '').replace('　', '').replace('年度', '')
        major = major[4:]
        # print(major)

        botton = "/html/body/table[3]/tbody/tr/td/table/tbody/tr[" + num + "]/td[5]/a/img"
        driver.find_element_by_xpath(botton).click()
        sleep(5)

        write = []

        title = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]").text.replace(' ', '')
        teacher = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]").text.replace('　', '').replace(' ', '')
        target = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]").text.replace(' ', '')
        day = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]").text.replace(' ', '')
        term = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[4]/td[4]").text.replace(' ', '')
        kubun = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[5]/td[4]").text.replace(' ', '')
        kazu = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[6]/td[4]").text.replace(' ', '')
        overview = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[10]/td[2]").text.replace(' ', '')
        goal = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[12]/td[2]").text.replace(' ', '')
        evaluation = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[13]/td[2]").text.replace(' ', '')
        text = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[14]/td[2]").text.replace(' ', '')
        text2 = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[15]/td[2]").text.replace(' ', '')
        message = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[16]/td[2]").text.replace(' ', '')
        learning = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[19]/td[2]").text.replace(' ', '')
        print(title)
        print(teacher)
        print(target)
        print(day)
        print(term)
        print(kubun)
        print(kazu)
        print(overview)
        print(goal)
        print(evaluation)
        print(text)
        print(text2)
        print(message)
        print(learning)

        for a in range(2,15):
            try:
                no = str(a)
                plan = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[11]/td[2]/table/tbody/tr[" + no +"]/td[2]").text.replace(' ', '')
                print(plan)
            except:
                plan = ""
            
            # write.append(plan)

        driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr/td/input").click()
        sleep(5)



    # driver.quit()

if __name__ == "__main__":
    Scraping(0)
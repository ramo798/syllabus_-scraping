from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
url = 'http://syllabus.center.wakayama-u.ac.jp/ext_syllabus/syllabusSearchDirect.do?nologin=on'
driver.get(url)
sleep(5)

driver.find_element_by_xpath("/html/body/form/table[3]/tbody/tr/td[2]/img[1]").click()
sleep(5)

with open('kkk.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')

    for b in range(1530,2100):
        b = str(b)

        tmp = "/html/body/table[3]/tbody/tr/td/table/tbody/tr[" + b + "]/td[1]"
        major = driver.find_element_by_xpath(tmp).text.replace('シラバス', '').replace('　', '').replace('年度', '')
        major = major[4:]

        botton = "/html/body/table[3]/tbody/tr/td/table/tbody/tr[" + b + "]/td[5]/a/img"
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
        # print(title)
        # print(teacher)
        # print(target)
        # print(day)
        # print(term)
        # print(kubun)
        # print(kazu)
        # print(overview)
        # print(goal)
        # print(evaluation)
        # print(text)
        # print(text2)
        # print(message)
        # print(learning)
        write.append(major)
        write.append(title)
        write.append(teacher)
        write.append(target)
        write.append(day)
        write.append(term)
        write.append(kubun)
        write.append(kazu)
        write.append(overview)
        write.append(goal)
        write.append(evaluation)
        write.append(text)
        write.append(text2)
        write.append(message)
        write.append(learning)

        for a in range(2,15):
            try:
                no = str(a)
                plan = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[11]/td[2]/table/tbody/tr[" + no +"]/td[2]").text.replace(' ', '')
                print(plan)
            except:
                plan = ""
            
            write.append(plan)
            

        print(write)
        print(b)

        writer.writerow(write)



        #↓戻るボタン押す
        driver.find_element_by_xpath("/html/body/form[1]/table/tbody/tr/td/input").click()
        sleep(5)


f.close()
driver.quit()

# /html/body/table[3]/tbody/tr/td/table/tbody/tr[2]/td[5]/a/img
# /html/body/table[3]/tbody/tr/td/table/tbody/tr[2]/td[5]/a
# /html/body/form[1]/table/tbody/tr/td/input
# /html/body/table[3]/tbody/tr/td/table/tbody/tr[3]/td[5]/a/img

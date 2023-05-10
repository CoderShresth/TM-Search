from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from os import getcwd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import warnings

os.system('cls')
warnings.filterwarnings('ignore')
searchString = input('Which keyword to search? ')

file1 = open('C:/Users/saumy/OneDrive/Desktop/search/DATA/'+str(searchString)+'.txt', "a")  # append mode


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('log-level=3')
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(getcwd() +'/chromedriver.exe', options=options)  

for classMark in range(1,46):
    driver.get("https://ipindiaonline.gov.in/tmrpublicsearch/frmmain.aspx")

    driver.find_element_by_name('ctl00$ContentPlaceHolder1$TBWordmark').send_keys(searchString)
    driver.find_element_by_name('ctl00$ContentPlaceHolder1$TBClass').send_keys(classMark)



    driver.find_element_by_name('ctl00$ContentPlaceHolder1$DDLFilter').click()
    driver.find_element_by_name('ctl00$ContentPlaceHolder1$DDLFilter').send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_name('ctl00$ContentPlaceHolder1$DDLFilter').send_keys(Keys.RETURN)

    driver.find_element_by_id('ContentPlaceHolder1_BtnSearch').click()

    totalstr = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/center/div/div[3]/div/div[1]/span/table/tbody/tr/td[1]"))).text
    totalMarks = re.findall(r'\b\d+\b',totalstr)
    totalMarks = ''.join(totalMarks)
    print('\n'+'In class: '+str(classMark)+' => '+totalstr+'\n')


    for i in range(int(totalMarks)):
        markName = driver.find_element_by_id('ContentPlaceHolder1_MGVSearchResult_lblsimiliarmark_'+str(i)).text
        markNo = driver.find_element_by_id('ContentPlaceHolder1_MGVSearchResult_lblapplicationnumber_'+str(i)).text
        file1.write(markName+' - '+markNo + ' - '+ str(classMark)+'\n')

file1.close()
driver.close()
print('Finished Searching, Output in - ' +str(searchString)+' file in DATA folder.')
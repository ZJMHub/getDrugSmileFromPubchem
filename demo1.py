# -*- coding: utf-8 -*-
# @Author  : Zhanjianming
# @Time    : 2022/9/10 1:18
# @File    : demo1.py
# @Software: PyCharm

from selenium import webdriver
import time
# 获取药物名称
from selenium.common.exceptions import InvalidSessionIdException

drug_list = []
with open('drug_smile.txt') as inf:
    for line in inf:
        drug_name = line.rstrip()
        drug_list.append(drug_name)


smile = []
for i in range(2804, 2806):
    try:
        drug_name = drug_list[i]
        # 设置Firefox浏览器
        driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
        driver.get("https://pubchem.ncbi.nlm.nih.gov/#query=" + drug_name)
        # 给浏览器打开页面的时间
        time.sleep(7)
        smile_in_div = driver.find_element_by_id("featured-results").find_elements_by_css_selector("div.f-0875")
        content = smile_in_div[3].find_element_by_class_name('breakword').text
        smile.append(content)
        print("id:" + str(i) + " smile:" + content)
    except Exception as e:
        smile.append("NotFound:" + str(i))
        print("id:" + str(i) + " NotFound!!!!")
    finally:
        # 关闭窗口
        driver.close()
# 保存内容
file = open("drug_smile4.txt", 'w')
for line in smile:
    file.write(line + "\n")
file.close()
print("smile长度为" + str(len(smile)))
print("success!!!")

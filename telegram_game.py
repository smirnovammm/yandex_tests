import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = 'https://tbot.xyz/math/#eyJ1IjoyNDYwNzM0ODcsIm4iOiJNYXJpbmEgU21pcm5vdmEiLCJnIjoiTWF0aEJhdHRsZSIsImNpIjoiLTYyMzA4ODQ0ODY0OTc3MDYyNjQiLCJpIjoiQWdBQUFCUFNBZ0NQeUtvTzdUbEdzQWFzblNRIn1hODRiMzcwMDc0MzZiOGI1MjVmNmI1YjY1ZWQ0YzMyZg==&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DqZmCzGvp1pJOzdiqM0_5Fq8QV-MEfrgi4yddC6V2J_NVAUFmzc_TuS7mTUtsp3Fe'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    start_button = browser.find_element_by_id("button_correct")
    start_button.click()
    while True:
        expected_res2 = ''
        expected_res = ''
        num1 = int(browser.find_element_by_id("task_y").text)
        num2 = int(browser.find_element_by_id("task_x").text)
        task_op = browser.find_element_by_id("task_op").text
        res = int(browser.find_element_by_id("task_res").text)
        wrong_button = browser.find_element_by_id("button_wrong")
        if task_op == 'x' or task_op == '×':
            expected_res = num1*num2
        elif task_op == '+':
            expected_res = num1 + num2
        elif task_op == '–' or task_op == '-':
            expected_res = num1-num2
            expected_res2 = num2-num1
        else:
            expected_res = num1/num2
            expected_res2 = num2/num1
        if expected_res == res or expected_res2 == res:
            start_button.click()
            time.sleep(0.2)
        else:
            wrong_button.click()
            time.sleep(0.2)

finally:
    browser.quit()

import request
import requests
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 找到要使用的浏览器
browser = webdriver.Safari()


# 如果是用Safari浏览器记得，第一个字母是大写，并且要在Safari浏览器中，的开发选项中，打开允许远程自动化

def log_on():
    # 打开页面
    browser.get("https://qzone.qq.com")

    # 找到frame的标签否则不好定义输入框
    browser.switch_to.frame("login_frame")

    # 定位到按钮“账号密码登录”
    logon = browser.find_element_by_id("switch_plogin")

    # 点击按钮并且切换到登录页面
    logon.click()

    # 定位QQ账号输入框
    username = browser.find_element_by_name("u")
    username.send_keys("账号")
    # 定位QQ密码输入框
    password = browser.find_element_by_name("p")
    password.send_keys("密码")

    # 输入换行符用以登录
    password.send_keys("Key.ENTER")

    # 等待网页加载
    time.sleep(5)

    # 刷新网页
    browser.refresh()


def get_post():
    item = browser.find_element_by_link_text("说说")
    item.click()
    username = browser.find_element_by_css_selector("qz_311_author c_tx nickname goProfile").text
    content = browser.find_element_by_css_selector("content").text
    print(username, "", content)


log_on()

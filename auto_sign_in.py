import time
from selenium import webdriver
from config import usr, pwd



def auto_sign_in(driver, usr, pwd):
	"""
	auto sign in
	driver: webdriver
	usr: 邮箱
	pwd: 密码
	"""
	# 使用xpath定位要填写的框
	email = driver.find_element('xpath', '//*[@id="email"]')
	email.send_keys(usr)
	password = driver.find_element('xpath', '//*[@id="password"]')
	password.send_keys(pwd)

	# 使用xpath定位要点击的框并调用click点击
	login_button = driver.find_element('xpath', '//*[@id="app"]/section/div/div/div/div[2]/form/div/div[5]/button')
	login_button.click()

	# 跳过弹窗
	window_read = driver.find_element('xpath', '//*[@id="popup-ann-modal"]/div/div/div[3]/button')
	window_read.click()

	# 尝试签到
	try:
		daily_sign = driver.find_element('xpath', '//*[@id="checkin-div"]')
		print('found')
		daily_sign.click()
	except Exception as e:
		print('Already done.')

	# 关闭网页
	driver.close() # close 关闭当前网页 quit() 关闭所有窗口


if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.get('https://ikuuu.ltd/auth/login')
	auto_sign_in(driver, usr, pwd)

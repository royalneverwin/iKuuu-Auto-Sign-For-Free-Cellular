### macOS Python实现登录网页并自动签到

##### Step 1：pip3 install Selenium

##### Step 2: 下载 Webdriver

a. 打开Chrome浏览器输入：Chrome://settings/help查看当前Chrome版本。

b. 下载对应的Chromedriver版本

c. 把Chromedriver放在usr/local/bin目录下

d. 测试是否完成

```python
# -*- coding:utf-8 -*-
# Author:Burro-CMD

from selenium import WebDriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
```

若出现‘Chrome正受到自动测试软件的控制’，就说明已经安装成功了。

##### Step 3: 在config_demo中填写自己的邮箱和密码

##### Step 4：python3 auto_sign_in.py





### DEBUG

 [AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'](https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath)

Selenium just removed that method in version `4.3.0`. You now need to use:

```py
driver.find_element("xpath", 'XPATH_NAME')
```

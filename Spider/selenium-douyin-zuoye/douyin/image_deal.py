from douyin.webbrowser import *
import requests
from PIL import Image

driver = DriverCreate()
driver.browser.get(driver.url)


def get_image():
    driver.wait.until(EC.presence_of_element_located((By.ID, 'captcha-verify-image')))
    image_div = driver.browser.find_element(By.ID, 'captcha-verify-image')
    image_src = image_div.get_attribute('src')
    suffix = image_src.split('.')[-1]
    print("验证图片", image_src)
    return image_src, suffix


def save_image(url, suffix):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    r = requests.get(url, headers).content
    with open("verify-image" + '.' + suffix, 'wb') as f:
        f.write(r)


def verify():
    image = Image.open('verify-image.jpeg')
    image.convert('L')
    image.show()


# image_url, suffix = get_image()
# save_image(image_url, suffix)
verify()

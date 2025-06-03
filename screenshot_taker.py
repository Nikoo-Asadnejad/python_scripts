from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = input("Enter a website URL: ")

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.set_window_size(1200, 800)
driver.get(url)
driver.save_screenshot("screenshot.png")
driver.quit()

print("📸 Screenshot saved as screenshot.png")

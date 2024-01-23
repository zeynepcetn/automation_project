from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Start browser
driver = webdriver.Chrome()

# Specify the URL of the website to log in to
url = "http://automationexercise.com"
driver.get(url)
driver.maximize_window()

# Wait for the homepage to load
login_page_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[1]/a"))
)
# Login successful
print("Login to Moneytolia Site is successful!")

# Clict to Products
products_button = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
products_button.click()

# Scroll down the page
driver.execute_script("window.scrollBy(0,500)", "")
driver.implicitly_wait(3) 
# Move mouse over button using ActionChains class
button = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
action = ActionChains(driver)
action.move_to_element(button).perform()

# Add the first product to the cart
add_cart = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a")
add_cart.click()

# Continue the shopping button
continue_button = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[1]/div/div/div[3]/button")
continue_button.click()

# Move mouse to item 2 and add to cart
button = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/img")
action = ActionChains(driver)
action.move_to_element(button).perform()

add_cart_second = driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/a")
add_cart_second.click()

# View cart button
view_cart_button = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[1]/div/div/div[2]/p[2]/a/u")
view_cart_button.click()

# Product and price information
product1 = "Men Tshirt"
price1 = 400

product2 = "Blue Top"
price2 = 500

total_expenditure = price1 + price2

# Printing and verifying information
print("1st Product: {}, Price: {} RS".format(product1, price1))
print("2nd Product: {}, Price: {} RS".format(product2, price2))
print("Total Expenditure: {} ".format(total_expenditure))
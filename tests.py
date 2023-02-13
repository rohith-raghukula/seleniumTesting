from selenium import webdriver

# Set up Chrome driver
driver = webdriver.Chrome()

# Open Google.com
driver.get("https://www.google.com")

# Find search bar and enter text
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("Selenium")
search_bar.submit()

# Assert that "Selenium" is in the title of the results page
assert "Selenium" in driver.title

# Close the browser
driver.quit()

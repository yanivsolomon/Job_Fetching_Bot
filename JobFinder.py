import time
from selenium import webdriver
import pytest
from selenium.common.exceptions import NoSuchElementException

# This bot's purpose is to find and fetch all jobs openings in Israel within Checkpoint's website.

# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")


def test_jobfind(test_setup):
# Get the website
    driver.get("https://careers.checkpoint.com/index.php?module=cpcareers&a=search&q=&fa[]=country_ss:Israel")
    time.sleep(3)


# Initialize an empty list to store div texts
    div_texts = []

# Define the number of pages (you can adjust this as needed)
    num_pages = 7

    for _ in range(num_pages):
        # Find the total number of div elements on the page
        total_divs = len(driver.find_elements_by_xpath("//*[@id='positionResults']/div"))

        # Iterate through each div and fetch its text and href link
        for i in range(1, total_divs + 1):
            div_xpath = f"//*[@id='positionResults']/div[{i}]"
            div_text = driver.find_element_by_xpath(div_xpath).text
            div_link = driver.find_element_by_xpath(f"{div_xpath}/a").get_attribute("href")
            div_texts.append(div_text)
            div_texts.append(div_link)
            time.sleep(2)

        # Move to the next page
        try:
            next_page_element = driver.find_element_by_xpath("//i[@class='nextPage fa fa-angle-right']")
            next_page_element.click()
            time.sleep(2)  
        except NoSuchElementException:
            break

    # Print the list of div texts with double spaces (line breaks)
    for text in div_texts:
        print(text + "\n\n")
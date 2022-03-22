from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

def click_agency_analysis(driver):
    locator = (By.XPATH, "//div/a[@href='/agency-analysis']")
    agency_analysis = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    agency_analysis.click()

def select_any_six_agencies(driver):

    select_agency_loc = (By.XPATH, "//a[@class='usa-select full modal-open']")

    agri_loc = (By.XPATH, "//li[@data-dept-name='department of agriculture']//input")
    commerce_loc = (By.XPATH, "//li[@data-dept-name='department of commerce']//input")
    education_loc = (By.XPATH, "//li[@data-dept-name='department of education']//input")
    energy_loc = (By.XPATH, "//li[@data-dept-name='department of energy']//input")
    health_human_loc = (By.XPATH, "//li[@data-dept-name='department of health and human services']//input")
    homeland_loc = (By.XPATH, "//li[@data-dept-name='department of homeland security']//input")

    done_loc = (By.XPATH, "//a[@class='button full done']")

    driver.find_element(*select_agency_loc).click()
    driver.find_element(*agri_loc).click()
    driver.find_element(*commerce_loc).click()
    driver.find_element(*education_loc).click()
    driver.find_element(*energy_loc).click()
    driver.find_element(*health_human_loc).click()
    driver.find_element(*homeland_loc).click()
    driver.find_element(*done_loc).click()

def click_cost_variance(driver):

    cost_variance_loc = (By.XPATH, "//a[@data-activate='cost-variance']")
    driver.find_element(*cost_variance_loc).click()

def save_graph_screenshot(driver):

    graph_loc = (By.ID, "cost-variance")
    graph = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(graph_loc)
    )
    graph.screenshot("graph.png")

def download_cost_variance_data(driver):

    download_link_loc = (By.LINK_TEXT, "Cost Variance Source Data")
    download_csv = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(download_link_loc)
    )
    download_csv.click()


if __name__ == '__main__':
    
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    
    prefs = {"download.default_directory": ROOT_DIR}
    user_agent = user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    options = Options()
    options.add_argument("headless")
    options.add_argument("start-maximized")
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    driver.get("https://itdashboard.gov")

    click_agency_analysis(driver)
    select_any_six_agencies(driver)
    click_cost_variance(driver)
    save_graph_screenshot(driver)
    download_cost_variance_data(driver)

    time.sleep(5)
    driver.quit()

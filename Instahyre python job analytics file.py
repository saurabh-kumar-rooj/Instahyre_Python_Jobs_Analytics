from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import pandas as pd
import time

driver = webdriver.Chrome()
url = 'https://www.instahyre.com/python-jobs'
time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.get(url)
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

data = []
elements = driver.find_elements(By.XPATH, '//*[@id="job-function-page"]/div[2]/div/div[1]/div[1]/div')
# //*[@id="job-function-page"]/div[2]/div/div[1]/div[1]/div[1]
# //*[@id="job-function-page"]/div[2]/div/div[1]/div[1]/div
# //*[@id="job-function-page"]/div[2]/div/div[1]/div[1]/div[21]
# //*[@id="job-function-page"]/div[2]/div/div[1]/div[1]/div[2]
idx = 1
for i in range(2, 17, 1):
    if i == 2:
        for idx, element in enumerate(elements, start=1):
            if idx > 20:
                break
            else:
                # /html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[9]/div/div/div/div/div[2]/a/div[1]/div
                x_path_name = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                              f'/div[2]/a/div[1]/div'
                x_path_loca = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                              f'/div[2]/a/div[2]/span/span'
                x_path_founded = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div' \
                                 f'/div/div[' \
                                 f'2]/a/div[3]/span[1]/span'
                x_path_no_eml = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                                f'/div[' \
                                f'2]/a/div[3]/span[3]/span'
                x_path_about = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                               f'/div[' \
                               f'2]/a/div[4]'
                x_path_skills = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                                f'/div[' \
                                f'2]/a/div[5]/ul'
                x_path_link = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                              f'/div[1]/a'
                # /html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/a
                # /html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/a

                link_element = driver.find_element(By.XPATH, value=x_path_link)
                link = link_element.get_attribute("href")
                print(f'{link}')

                name = driver.find_element(By.XPATH, value=x_path_name).text
                print(f'{name}')

                location = driver.find_element(By.XPATH, value=x_path_loca).text
                print(f'{location}')

                founded = driver.find_element(By.XPATH, value=x_path_founded).text
                print(f'{founded}')

                employees = driver.find_element(By.XPATH, value=x_path_no_eml).text
                print(f'{employees}')

                about = driver.find_element(By.XPATH, value=x_path_about).text
                print(f'{about}')

                skills = driver.find_element(By.XPATH, value=x_path_skills).text
                print(f'{skills}', end=" ")

                data.append({
                    'Name': name,
                    'Location': location,
                    'Founded': founded,
                    'Employees': employees,
                    'About': about,
                    'Skills': skills,
                    'Link': link
                })
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.XPATH,
                            value=f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[21]/li[12]').click()
        # /html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[21]/li[2]
        driver.implicitly_wait(10)
        for idx, element in enumerate(elements, start=1):
            if idx > 20:
                break
            else:
                x_path_name = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                              f'/div[2]/a/div[1]/div'
                x_path_loca = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                              f'/div[2]/a/div[2]/span/span'
                x_path_founded = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div' \
                                 f'/div/div[' \
                                 f'2]/a/div[3]/span[1]/span'
                x_path_no_eml = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                                f'/div[' \
                                f'2]/a/div[3]/span[3]/span'
                x_path_about = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                               f'/div[' \
                               f'2]/a/div[4]'
                x_path_skills = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                                f'/div[' \
                                f'2]/a/div[5]/ul'
                x_path_link = f'/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[{idx}]/div/div/div/div' \
                              f'/div[1]/a'
                # /html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/a
                # /html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/a

                link_element = driver.find_element(By.XPATH, value=x_path_link)
                link = link_element.get_attribute("href")
                print(f'{link}')

                name = driver.find_element(By.XPATH, value=x_path_name).text
                print(f'{name}')

                location = driver.find_element(By.XPATH, value=x_path_loca).text
                print(f'{location}')

                founded = driver.find_element(By.XPATH, value=x_path_founded).text
                print(f'{founded}')

                try:
                    employees = driver.find_element(By.XPATH, value=x_path_no_eml).text
                    print(f'{employees}')
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    print("No Data Found")
                try:
                    about = driver.find_element(By.XPATH, value=x_path_about).text
                    print(f'{about}')
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    print("No Data Found")
                try:
                    skills = driver.find_element(By.XPATH, value=x_path_skills).text
                    print(f'{skills}', end=" ")
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    print("No Data Found")
                data.append({
                    'Name': name,
                    'Location': location,
                    'Founded': founded,
                    'Employees': employees,
                    'About': about,
                    'Skills': skills,
                    'Link': link
                })

time.sleep(2)
driver.close()

df = pd.DataFrame(data)
df.to_csv('python_jobs_dataset_selenium.csv', index=False)

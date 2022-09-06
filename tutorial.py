import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

PATH = "bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://www.jobbank.gc.ca/home')

search = driver.find_element(By.ID, 'searchString')
search.send_keys("2114605")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
result = driver.find_element(By.CLASS_NAME, "results-jobs")
result.click()
driver.implicitly_wait(10)
job_details = driver.find_element(By.CLASS_NAME,"job-posting-details-body")
job_title = job_details.find_element(By.TAG_NAME, "span").text
job_employer = job_details.find_element(By.TAG_NAME, "strong").text
job_location = job_details.find_element(By.CLASS_NAME, "city").text
job_salary = job_details.find_element(By.CLASS_NAME, "attribute-value").text
job_period = job_details.find_element(By.XPATH, "//span[@property='workHours']").text
job_type = job_details.find_element(By.XPATH, "//span[@property='employmentType']").text
job_qualification = job_details.find_element(By.XPATH, "//ul[@property='educationRequirements']").text
job_experience = job_details.find_element(By.XPATH, "//p[@property='experienceRequirements']").text.replace(",","&comma;")
job_resp = job_details.find_elements(By.CLASS_NAME, "csvlist")[0].text
job_sup = job_details.find_elements(By.CLASS_NAME, "csvlist")[1].text
job_add_info = job_details.find_elements(By.CLASS_NAME, "csvlist")[2].text

# print(job_title)
# print(job_employer)
# print(job_location)
# print(job_salary)
# print(job_period)
# print(job_type)
# print(job_qualification)
# print(job_experience)
# print(job_resp)
# print(job_sup)
# print(job_add_info)

with open('scraped_jobs.json', mode='w') as json_file:
    # fieldnames = ['job_title', 'employer', 'location','salary','type','requirement','experience','responsibilities','supervision','add_info']
    # writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')

    # writer.writeheader()
    json.dump({'job_title': job_title, 
                     'employer': job_employer, 
                     'location': job_location,
                     'salary': job_salary +' '+job_period,
                     'type': job_type,
                     'requirement': job_qualification,
                     'experience': job_experience,
                     'responsibilities': job_resp,
                     'supervision': job_sup,
                     'add_info': job_add_info
                     }, json_file)




driver.quit()





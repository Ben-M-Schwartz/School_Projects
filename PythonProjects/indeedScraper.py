import csv
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 
from linkedin_scraper import Person, actions
from scrape_linkedin import ProfileScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException


def read_csv(filename):
	with open(filename, newline='') as f:
		reader = csv.reader(f)
		job_list = list(reader)
	for i in range(len(job_list)):
		job_list[i] = [job_list[i][0], job_list[i][1]]
	return(job_list)


def random_job_generator(job_list):
	random_int = random.randint(0, len(job_list) - 1)
	random_job = job_list[random_int]
	return(random_job)


def find_elements_in_string(str1, list1):
	result = []
	for i in list1:
		if (i in str1):
			result.append(i)
	return(result)

def make_float(str1):
	try: 
		str1 = float(str1)
		return(str1)
	except ValueError:
		return False


def get_user_agent_list():
	filename = 'updated_user_agents_chrome_100-0.csv'
	with open(filename, newline='') as f:
		reader = csv.reader(f)
		user_agent_list = list(reader)
	for i in range(len(user_agent_list)):
		user_agent_list[i] = user_agent_list[i][0]
	return(user_agent_list)

def get_random_user_agent(user_agent_list):
	random_index = random.randint(0, len(user_agent_list))
	return (user_agent_list[random_index])


def clean_salary(salary):
	if ('year' in salary):
		salary = salary.replace('$', '').replace(',', '')
		salary = salary.split()
		salary = [make_float(i) for i in salary]
		salary = list(filter(bool,salary))
		salary = [int(i) for i in salary]
		return (salary)
	elif ('hour' in salary):
		salary = salary.replace('$', '').replace(',', '')
		salary = salary.split()
		salary = [make_float(i) for i in salary]
		salary = list(filter(bool,salary))
		salary = [int(i*40*52) for i in salary]
		return(salary)
	elif ('month' in salary):
		salary = salary.replace('$', '').replace(',', '')
		salary = salary.split()
		salary = [make_float(i) for i in salary]
		salary = list(filter(bool,salary))
		salary = [int(i*12) for i in salary]
		return (salary)

	elif ('day' in salary):
		salary = salary.replace('$', '').replace(',', '')
		salary = salary.split()
		salary = [make_float(i) for i in salary]
		salary = list(filter(bool,salary))
		salary = [int(i*5*52) for i in salary]
		return (salary)

	else:
		salary = None
		return salary


def scroll(driver):
	# Scroll to bottom (not my code)

	start = time.time()
	  
	# will be used in the while loop
	initialScroll = 0
	finalScroll = 1000
	  
	while True:
	    driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
	    initialScroll = finalScroll
	    finalScroll += 1000
	    time.sleep(random.uniform(0, 3))

	    end = time.time()
	  
	    if round(end - start) > 10:
	        break

def scrollup(driver):
	# Scroll to bottom (not my code)

	start = time.time()
	  
	# will be used in the while loop
	initialScroll = 6000
	finalScroll = 5000
	  
	while True:
	    driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
	    initialScroll = finalScroll
	    finalScroll -= 1000
	    time.sleep(random.uniform(0, 3))

	    end = time.time()
	  
	    if round(end - start) > 10:
	        break


def wait_rand_interval():
	time.sleep(random.randint(1, 20) / 10)


def scan_page(driver, queried_title, industry):

	time.sleep(random.randint(5, 10))
	# Close a popup if it occurs
	if (len(driver.find_elements_by_id('popover-foreground')) != 0):
		print('POPUP!!!!!')
		popup = driver.find_elements_by_id('popover-foreground')
		if (len(popup) > 0):
			popup[0].find_element_by_class_name('icl-CloseButton').click()
		time.sleep(random.randint(2,5))
	
	print("QUERIED TITLE: " + queried_title)

	# Scroll all the way down, then up to make sure everything is loaded and visible
	scroll(driver)
	scrollup(driver)

	# See if we can get the number of jobs available for our input
	try:
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'searchCountPages')))
		num_jobs = driver.find_element_by_id('searchCountPages').text.strip()
		num_jobs = "".join([i for i in list(num_jobs) if i.isdigit()])[1:]
	except TimeoutException:
		num_jobs = 'None'

	print("NUM_JOBS: " + num_jobs)

	time.sleep(random.randint(2, 4))
	jobs = driver.find_elements_by_class_name('result')
	result = []

	state_abbreviations = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
       'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
       'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
       'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
       'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
	states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois", "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland", "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York", "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania", "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah", "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
	location_options = state_abbreviations + states + ['Remote']
	
	for job in jobs:
		actual_title = job.find_element_by_class_name('jobTitle').text
		actual_title = actual_title.replace('new', '').strip()
		location_text = job.find_element_by_class_name('companyLocation').text
		location = find_elements_in_string(location_text, location_options)
		company = job.find_element_by_class_name('companyName').text.strip()
		salary_elements = job.find_elements_by_class_name('salary-snippet-container')

		if (len(salary_elements) > 0):
			salary = salary_elements[0].text.strip()
			salary = clean_salary(salary)
		else:
			salary = 'None'

		if (len(job.find_elements_by_class_name('ratingNumber')) > 0):
			company_rating = job.find_element_by_class_name('ratingNumber').text.strip()
		else:
			company_rating = 'None'

		partial_job_desc = job.find_element_by_class_name('job-snippet').text.strip().replace('\n',' ').replace('\t',' ')

		if (len(job.find_elements_by_class_name('more_loc_container')) > 0):
			more_loc = job.find_element_by_class_name('more_loc_container').text.strip()
			more_loc = "".join([i for i in list(more_loc) if i.isdigit()])
		else:
			more_loc = 0

		print("\n")
		print(queried_title)
		print(industry)
		print(actual_title)
		print(location)
		print(company)
		print(company_rating)
		print(salary)
		print(num_jobs)
		print(more_loc)
		print(partial_job_desc)

		# Error where webdriver can't find any jobs on the page
		if ((actual_title == '') and (location == []) and (company == '') and (partial_job_desc == '')):
			print('ERROR NO DATA GATHERED')
			return ([])

		result.append([queried_title, industry, actual_title, location, company, company_rating, salary, num_jobs, more_loc, partial_job_desc])

	scroll(driver)

	return(result)


def indeed_query(driver, pages, user_agents, use_user_agents, job_titles):

	random_job = random_job_generator(job_titles)
	queried_title = random_job[1]
	industry = random_job[0]

	time.sleep(3)
	
	# Change user agent here
	if (use_user_agents):
		rand_user_agent = get_random_user_agent(user_agents)
		driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": rand_user_agent})
		print('-----------USER AGENT------------')
		print(driver.execute_script("return navigator.userAgent;"))

	time.sleep(3)

	job_box = driver.find_element_by_id('text-input-what')
	wait_rand_interval()
	job_box.send_keys(Keys.CONTROL + "a")
	wait_rand_interval()
	job_box.send_keys(Keys.DELETE)
	wait_rand_interval()
	job_box.send_keys(queried_title)
	
	where_box = driver.find_element_by_id('text-input-where')
	where_box.send_keys(Keys.CONTROL + "a")
	wait_rand_interval()
	where_box.send_keys(Keys.DELETE)
	wait_rand_interval()
	where_box.send_keys('United States')
	wait_rand_interval()
	where_box.send_keys(Keys.ENTER)
	time.sleep(5)

	all_pages = []
	for i in range(pages):
		page_result = scan_page(driver, queried_title, industry)
		all_pages = all_pages + page_result

		# We want to load the next page if the page numbers are there and if we are actually going to scan the next page
		if ((len(driver.find_elements_by_class_name('pagination-list')) > 0) and (pages != i + 1) and (len(page_result) != 0)):
			page_buttons = driver.find_element_by_class_name('pagination-list').find_elements_by_tag_name('li')
			if (len(page_buttons) > 0):
				page_buttons[-1].find_element_by_tag_name('a').click()
			else:
				break
		else:
			scrollup(driver)
			break

	return(all_pages)


def scrape_indeed(num_queries, pages_per_query, use_user_agents):

	chrome_options = Options()
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("window-size=1200x600")
	driver = webdriver.Chrome('./chromedriver', options=chrome_options)	
	driver.get('https://www.indeed.com')

	# From https://www.indeed.com/career-advice/finding-a-job/types-of-industry
	job_titles = read_csv("cleaned_soc.csv")

	user_agents = get_user_agent_list()

	with open('indeed_data.csv', 'a', newline='', encoding="utf-8") as f:
		writer = csv.writer(f)
		for i in range(num_queries):
			print("----------Query " + str(i + 1) + " out of " + str(num_queries) + "------------")
			data = indeed_query(driver, pages_per_query, user_agents, use_user_agents, job_titles)
			print(data)
			for row in data:
				writer.writerow(row)
			time.sleep(random.randint(5, 20))
		f.close()

	driver.quit()



def main():
	# indeed_query()
	scrape_indeed(1, 2, True)
	# rand_user_agent = get_random_user_agent(get_user_agent_list())

	# test_scroll()


main()

# Getting job listings and classification from https://www.onetcenter.org/taxonomy.html#listings
# https://www.bls.gov/soc/2018/major_groups.htm

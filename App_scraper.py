# The Code displayed works for static HTML content
import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.co.uk/jobs/search/?q=Software-Engineer&where=London__2C-London&client=power&cy=uk&rad=20&intcid=swoop_Hero_Search'
page = requests.get(url)

# This code performs a HTTP request to the given URL, retrieving data that the server sends back and stores that data in a python object

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

# Function search for Python Developer jobs
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
for p_jobs in python_jobs:
    link = p_jobs.find("a")["href"]
    print(p_jobs.text.strip())
    print(f'Apply Here: {link}\n')

# Function defined to print the jobs available
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    # salary_elem = job_elem.find('div', 'span', class_='name')
    # apply_link = job_elem.find('a', id_='PrimaryJobApply')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

# This section of code finds webpage elements through HTML class names
# Adding .text to a beautiful soup object returns only text HTML elements


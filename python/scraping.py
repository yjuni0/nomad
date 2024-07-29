import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jobs = []

for job in jobs:
    
    title_elem = job.find("span", class_="title")
    title = title_elem.text if title_elem else "No Title"

    
    company_elem, position_elem, region_elem = [job.find("span", class_="company") for _ in range(3)]
    
    
    if not (company_elem and position_elem and region_elem):
        print(f"Skipping job due to missing elements: Title={title}")
        continue

    company = company_elem.text if company_elem else "No Company"
    position = position_elem.text if position_elem else "No Position"
    region = region_elem.text if region_elem else "No Region"

    job_data = {
        "title": title,
        "company": company_elem.text,
        "position": position_elem.text,
        "region": region_elem.text,
    }
    all_jobs.append(job_data)
print(all_jobs)    
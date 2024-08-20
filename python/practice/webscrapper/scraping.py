import requests
from bs4 import BeautifulSoup

all_jobs = []

def job_scraping(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser",)
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

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

        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "url": f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser",)
    return len(soup.find("div", class_=".pagination").find_all("span", class_=".page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for pages in range(total_pages):
        url = f"https://weworkremotely.com/remote-full-time-jobs?page={pages+1}"
        job_scraping(url)

print(len(all_jobs))
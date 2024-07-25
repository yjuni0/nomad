import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

for job in jobs:
    # title 요소를 찾고, 텍스트를 가져옵니다
    title_elem = job.find("span", class_="title")
    title = title_elem.text if title_elem else "No Title"

    # company, position, region 요소를 찾고, 텍스트를 가져옵니다
    company_elem, position_elem, region_elem = [job.find("span", class_="company") for _ in range(3)]
    
    # 값이 존재하는지 확인하고 없을 경우 오류 메시지를 출력 후 건너뛰기
    if not (company_elem and position_elem and region_elem):
        print(f"Skipping job due to missing elements: Title={title}")
        continue

    company = company_elem.text if company_elem else "No Company"
    position = position_elem.text if position_elem else "No Position"
    region = region_elem.text if region_elem else "No Region"

    # 값을 출력합니다
    print(title, company, position, region, "-----\n")
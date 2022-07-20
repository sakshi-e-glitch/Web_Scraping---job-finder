from bs4 import BeautifulSoup  #import BeautifulSoup from bs4 library
import requests     #import requests library
import time


print('Put some skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
#variable_for_website = requests.get('url_of_website')         this will output the request code, in order to get the text add .text as well
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text,  'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
#print(jobs)

def find_jobs():
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')                 #replace(' ','') is used to remove extra spaces
            skills = job.find('span', class_ = 'srp-skills').text.replace('  ','')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open (f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More info: {more_info} \n")

                    print(f'File saved {index} ')

#######################################################################################
                    # print(f"Company Name: {company_name.strip()}")
                    # print(f"Required Skills: {skills.strip()}")
                    # print(f"More info: {more_info}")

                    #print('')
    
            # print(f'''
            # Company Name: {company_name} 
            # Required Skills: {skills}
            # ''')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait  = 10
        print(f'Waiting {time_wait} minutes... ')
        time.sleep(time_wait*60)
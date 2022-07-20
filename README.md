# FULL STACK DEVELOPMENT WITH PYTHON- TECHWAVE 
## Web_Scraping---job-finder
Hi I made this project during Full Stack development with Python Training program, conducted by <b> TechWave </b>.

## About the project :
Web scraping is an automatic method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a database so that it can be used in various applications. In this project, we’ll be scraping out the jobs from [timesjobs.com](https://www.timesjobs.com/), which revolve around the techstack we are familiar with (for e.g. python).

<br>

## Tech Stack used :
Flask


## How the program works :
#### 1. Library and modules used:
  * BeautifulSoup: A Python library used for pulling data out of HTML and XML files.
  * requests: Used for fetching out the content from the given URL.
  * time: A module used to execute a Python script after every particular instance of time.

#### 2. Working
  1. First, the user will enter the tech stack which he/she is not familiar with. 
  2. Then the scraper will be given a specific URL or a whole list, (in our project, a URL which consists of a list of jobs having Python as prerequisites) to scrape data from. 
  3. Then the scraper will either extract all the data on the page or you’d be able to select the specific data you’d want to extract. In our project, we’re extracting the jobs which have been posted a few days back and do not require the tech stack which the user has entered in the very first step.
  4. Lastly, the scarper will run and will download the results in text files. This entire piece of code will be re-run after every 10 minutes to provide us with the updated data as well.


 
</br>



Follow TechWave on: 
<li><a href="https://www.linkedin.com/company/techwave-courses/">LinkedIn</a>
<li><a href="https://www.instagram.com/techwave.courses/">Instagram</a>

Follow me on: 
<li><a href="https://www.linkedin.com/in/sakshi-pandey-72979b1ba/">LinkedIn</a>
<li><a href="https://twitter.com/1510__Sakshi32">Twitter</a>

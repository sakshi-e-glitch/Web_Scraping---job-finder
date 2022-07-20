# import BeautifulSoup from bs4 library
from bs4 import BeautifulSoup

# to read the html file we'll have to open it, specigy the file name and method (read, write, both) as well\
# with open('file name', 'method') as variable_for_file:
#     variable_that_will_store_content = variable_for_file.read()
#     print(variable_that_will_store_content)

with open('index.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    #make an instance of BeautifulSoup
    #variable_name = BeautifulSoup(variable_that_will_store_content, 'parser_method_in_form_of_string')
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())     #this will allow you to print content in a prettier way

    #Lets assume we want to grab all the content which is present in an h5 tag of html
    # courses_html = soup.find('h5')      #this will grab only the first h5 tag    
    # print(courses_html)  

    # courses_html = soup.find_all('h5')      #this will grab all the h5 tags    
    # #print(courses_html) 
    # for course in courses_html:       #this will print only the text attribute of these tags
    #     print(course.text)   
     
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}') 
          

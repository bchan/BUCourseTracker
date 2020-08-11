import requests
from bs4 import BeautifulSoup
import json
import re
from dictionaries import collegesDictionary, departmentsDictionary
import boto3


# Returns a soup object for the inputted url
def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


# Generates course search link based on semester
def get_coursesearch_link(semester):
    link = str('https://www.bu.edu/phpbin/course-search/search.php?page=w0&pagesize=-1&adv=1&nolog=&search_adv_all=&yearsem_adv=' 
            + semester 
            + '&credits=*&hub_match=all&pagesize=-1')
    # link = 'https://www.bu.edu/phpbin/course-search/search.php?page=w0&pagesize=-1&adv=1&nolog=&search_adv_all=&yearsem_adv=2020-FALL&college%5B%5D=ENG&credits=*&hub_match=all&pagesize=-1'

    return link


# Gets the prereqs for a course - returns a tuple (list of courses, whole string)
def get_prereqs(pTag):
    prereqCourseList = []
    prereqString = pTag.getText()
    if prereqString == '':
        return ([], '')
    
    prereqAtags = pTag.find_all('a')
    if prereqAtags is None:
        return ([], prereqString)
    else:
        for prereq in prereqAtags:
            prereqCourseList.append(prereq.contents[0])
    
    return (prereqCourseList, prereqString)


# Gets the hub fields for a course and returns a list of them
def get_hub_list(hubTag):
    if hubTag is None:
        return []
    
    hubItems = hubTag.find_all('li')
    hubList = [item.contents[0] for item in hubItems]

    return hubList


# Gets the college and the department name from a course code (eg. ENG EC 311)
def get_college_dept(code):
    splitCode = code.split(' ')
    college = splitCode[0]
    department = splitCode[1]

    collegeName = ''
    departmentName = ''

    if college in collegesDictionary:
        collegeName = collegesDictionary[college]

    if college == 'GRS' and department in departmentsDictionary['CAS']:
        departmentName = departmentsDictionary['CAS'][department]
    elif college in departmentsDictionary and department in departmentsDictionary[college]:
        departmentName = departmentsDictionary[college][department]

    return (collegeName, departmentName)


# Generates a list of dictionaries for each course
def get_course_list(soup):
    courseResults = soup.find('ul', {'class': 'coursearch-results'})
    courseItems = courseResults.find_all('li', recursive=False)
    courseList = []
    for course in courseItems:
        # Sections of course list item
        content = course.find('div', {'class': 'coursearch-result-content'})
        heading = course.find('div', {'class': 'coursearch-result-heading'})
        description = course.find('div', {'class': 'coursearch-result-content-description'})
        hubTag = course.find('ul', {'class': 'coursearch-result-hub-list'})

        # Paragraph (p) tags contain the prerequisites, description, and credits
        # Indices 0, 4, and 5 respectively
        descriptionPtags = description.find_all('p')
        creditString = descriptionPtags[5].contents[0]

        # Portions of course - uses regex to clean the credits string
        courseCode = heading.find('h6').contents[0]
        courseName = heading.find('h2').contents[0]
        courseDescription = descriptionPtags[4].getText()
        courseCredits = re.search(r'(?!cr|\.\])(\b\S+)', creditString).group()

        courseHubList = get_hub_list(hubTag)
        coursePrereqList, coursePrereqString = get_prereqs(descriptionPtags[0])
        courseCollege, courseDepartment = get_college_dept(courseCode)

        courseDictionary = {'code': courseCode, 
                            'name': courseName,
                            'college': courseCollege,
                            'department': courseDepartment,
                            'description': courseDescription,
                            'credits': courseCredits, 
                            'hubList': courseHubList,
                            'prereqList': coursePrereqList,
                            'prereqString': coursePrereqString}

        courseList.append(courseDictionary)

    return courseList


# Writes all the course information to dynamodb
def write_courses_db():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('courses')

    with open('courses.json') as json_file:
        data = json.load(json_file)
        with table.batch_writer() as batch:
            for course in data:
                batch.put_item(Item=course)


# Uses new course search website to gather all courses and parses
def main():
    url = get_coursesearch_link('2020-FALL')
    soup = get_soup(url)
    courseList = get_course_list(soup)

    with open('courses.json', 'w') as json_file:
        json.dump(courseList, json_file, indent=4)


if __name__ == '__main__':
    main()

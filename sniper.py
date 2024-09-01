from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import pyfiglet
import sys 

# Setup Selenium
firefox_executable_path = '/usr/local/bin/geckodriver'
service = Service(executable_path=firefox_executable_path)
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 20)

# TEXT STYLES
def underline(type): sys.stdout.write("\033[4m" + type + "\033[0m")
def bold(type): sys.stdout.write("\033[1m" + type + "\033[0m")
def highlight(type): sys.stdout.write("\033[7m" + type + "\033[0m")

# TEXT COLORS 
def red(skk): sys.stdout.write("\033[91m {}\033[00m" .format(skk))
def green(skk): sys.stdout.write("\033[92m {}\033[00m" .format(skk))

# FUNCTION TO CHECK IF COURSE REGISTRATION IS OPEN
def checkCourseRegistration(courseUrl):
    driver.get(courseUrl)
    coursePageContent = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.usse-id-courselong')))
    courseName = coursePageContent.find_element(By.CSS_SELECTOR, 'h1.title')
    moduleName = courseName.find_element(By.CSS_SELECTOR, 'span.what:nth-child(3)')
    registrationOpen = False
    counter = 0
    print('======================================================================\n\n')
    courseName_ascii_banner = pyfiglet.figlet_format(moduleName.text)
    print(courseName_ascii_banner)
    a = 'Course URL: '
    b = cUrl+'\n\n'
    bold(a)
    underline(b)
    while not registrationOpen and counter < 5:
        try:
            registrationList = coursePageContent.find_element(By.CSS_SELECTOR, 'ul.registrations')
            registrationOpen = True
        except NoSuchElementException:
            counter+=1
    if registrationOpen:
        regInfoElts = registrationList.find_elements(By.XPATH, './*')
        c = 'Registration for course '+courseName.text+' open! Details:\n'
        green(c)
        for elt in regInfoElts:
            bold('-')
            print(f' {elt.text}')
        print('\n')
    else:
        d = 'Registration for course '+courseName.text+' still closed.\n\n'
        red(d)

courseUrlList = [
    'https://ufind.univie.ac.at/de/course.html?lv=051031&semester=2024W', 
    'https://ufind.univie.ac.at/de/course.html?lv=051029&semester=2024W', 
    'https://ufind.univie.ac.at/de/course.html?lv=051030&semester=2024W', 
    'https://ufind.univie.ac.at/de/course.html?lv=051040&semester=2024W',
    'https://ufind.univie.ac.at/de/course.html?lv=051032&semester=2024W',
    'https://ufind.univie.ac.at/de/course.html?lv=051023&semester=2024W',
    'https://ufind.univie.ac.at/de/course.html?lv=051061&semester=2024W'
]

print('\n')

for cUrl in courseUrlList:
    checkCourseRegistration(cUrl)

print(f'======================================================================\n\n')


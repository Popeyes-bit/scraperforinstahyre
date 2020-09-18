from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from webdriver_manager.chrome import ChromeDriverManager
from csv import writer
import csv
import os.path
from os import path


#
file_name = "data.csv"
header=['Company Name','ScrapedLink','Company_profile','Company_location','About','why_us','interview_process','quick_facts','similar-jobs','tech stack','contact','photo_links','dump']

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
def save(file_name, header):
    if(path.exists(file_name)):
    	print("exists")
    else:    	
    	append_list_as_row(file_name,header)
    
    
save(file_name,header)

def scroll(times):
    SCROLL_PAUSE_TIME = times

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Creation of a new instance of Chrome
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

#Base url
newurl='https://www.instahyre.com/jobs-in-delhi-ncr/?page=1'

#input of visit is the page no url and returns a boolean value for continuation of while loop	
def visit(newurl):
	browser.get (newurl)
	scroll(2)
	companyurls=[]
	alpha=True
	for i in range(0,8):
			try:
				linked=browser.execute_script("return document.getElementsByClassName('jobs')["+ str(i+1)+"].getElementsByTagName('a')[0].href")
				alpha=True
			except:
				linked=''
				alpha=False
			companyurls.append(linked)
	for i in range(0,8):
			if (companyurls[i]==''):
				return False
				
			else:
				browser.get(companyurls[i])
				
			if (browser.current_url =="https://www.instahyre.com/"):
				return True
			scroll(1)
			Company= browser.execute_script("return document.getElementById('employer-profile').getElementsByClassName('title-1')[0].innerText")
			Company_profile=browser.execute_script("return document.getElementById('employer-profile').getElementsByClassName('title-2')[0].innerText")
			Company_location=browser.execute_script("return document.getElementById('employer-profile').getElementsByClassName('title-3')[0].innerText")
			dump=browser.execute_script("return document.getElementsByClassName('content-block')[0].innerText")

			try:
			    About=browser.execute_script("return document.getElementById('employer-summary').getElementsByClassName('quill-formatted')[0].innerText")
			except:
			    About=''

			try:
			    why_us=browser.execute_script("return document.getElementById('why-us').getElementsByClassName('quill-formatted')[0].innerText")
			except:
			    why_us=''

			try:
			    interview_process=browser.execute_script("return document.getElementById('interview_process').getElementsByClassName('profile-content')[0].innerText")
			except:
			    interview_process=''

			try:
			    quick_facts=browser.execute_script("return document.getElementById('company-facts').getElementsByClassName('profile-content')[0].innerText")
			except:
			    quick_facts=''

			#try:

			    #skills=browser.execute_script("return document.getElementById('similar-jobs').innerText")
			 #   skills=browser.execute_script("return document.getElementById('similar-jobs').getElementsByTagName('strong')[0].innerText") + "@@" +browser.execute_script("return document.getElementById('similar-jobs').getElementsByTagName('a')[0].href")
			#except:
			 #   skills=''

			try:
				green=True
				g=0
				skills=''
				while(green):
					
					try:
						skills=skills+"#####"+browser.execute_script("return document.getElementById('similar-jobs').getElementsByTagName('strong')["+str(g)+"].innerText") + "@@" +browser.execute_script("return document.getElementById('similar-jobs').getElementsByTagName('a')["+str(g)+"].href")
						g=g+1
						green=True
					except:
						green=False
			    	
			except:
			    skills=''

			try:
				green=True
				g=0
				contact=''
				while(green):
					
					try:
						contact=contact+"    "+browser.execute_script("return document.getElementById('employer-social').getElementsByTagName('a')["+str(g)+"].href")
						g=g+1
						green=True
					except:
						green=False
			    	
			except:
			    contact=''

			try:
				green=True
				g=0
				photo_links=''
				while(green):
					
					try:
						photo_links=photo_links+"    "+ browser.execute_script("return document.getElementById('office-photos').getElementsByTagName('a')["+str(g)+"].href")
						g=g+1
					except:
						green=False

			except:
			    photo_links=''

			try:
				green=True
				g=0
				tech_stack=''
				while(green):
					
					try:
						tech_stack=tech_stack+"    "+ browser.execute_script("return document.getElementById('tech_stack').getElementsByTagName('li')["+str(g)+"].innerText")
						g=g+1
					except:
						green=False

			except:
			    tech_stack=''
			    

			list=[]
			list.append(Company)
			list.append(companyurls[i])
			list.append(Company_profile)
			list.append(Company_location)
			list.append(About)
			list.append(why_us)
			list.append(interview_process)
			list.append(quick_facts)
			list.append(skills)
			list.append(tech_stack)
			list.append(contact)
			list.append(photo_links)
			list.append(dump)
			fields = ['Company', 'Company_profile', 'Company_location', 'head_plus_content1', 'head_plus_content2', 'head_plus_content3', 'head_plus_content4', 'head_plus_content5', 'head_plus_content6', 'head_plus_content7', 'head_plus_content8','dump'] 
			from csv import writer
			filename = "data.csv"
			def append_list(file_name, list_of_elem):
			    # Open file in append mode
			    with open(file_name, 'a+', newline='') as write_obj:
			        # Create a writer object from csv module
			        csv_writer = writer(write_obj)
			        # Add contents of list as last row in the csv file
			        csv_writer.writerow(list_of_elem)
			try:
				append_list(filename, list)
			except:
				error=[]
				error.append(companyurls[i])
				append_list(filename,error)
	#filename="companyurls.csv"
	#append_list_as_row(filename, companyurls)
	return alpha

#initialisation of while loop
alpha=True
p=1
while(alpha):
	print(p)
	t1=time.time()
	alpha= visit(newurl)
	t2=time.time()-t1
	print(str(t2) +'sec')
	p=p+1
	newurl="https://www.instahyre.com/jobs-in-delhi-ncr/?page="+str(p)
	

browser.quit()
print('scraping Ended')
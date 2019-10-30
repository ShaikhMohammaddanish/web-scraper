from googlesearch import search
import requests
import re

contactfile = open("contact_ganrated_by_python.txt", "a")
all_email = []
all_contact = []
URL = []


def get_all_number(url):
    global all_contact, all_email, URL
    session = requests.Session ( )
    session.max_redirects = 60
    content = session.get ( url )
    contact = re.findall ( r"(\d{3}\d{3}\d{4})", content.text )
    if len ( contact ) != 0 :
        print (url)
        line1 = f"\n\nURL: {url}\n"
        contactfile.write ( line1)
        for contacts in contact :
            if contacts not in all_contact:
                URL.append ( url )
                all_contact.append ( contacts )
                print (contacts, end = " " )
                line2 = f"\t{contacts}\n"
                contactfile.write(line2)

def get_all_email(url):
    global all_contact, all_email, URL

    session = requests.Session ( )
    session.max_redirects = 60
    content = session.get ( url )
    email = re.findall( r'[\w\.-]+@[\w\.-]+', content.text )
    if len(email) != 0 :
        print(url)
        line3 = f"\nURL: {url}\n"
        contactfile.write ( line3 )
        for emails in email:
            if emails not in all_email:
                all_email.append(emails)
                print (emails, end = " ")
                line4 = f"\t{emails}\n"
                contactfile.write ( line4 )


query = input("type your Quary")
linex = f'\n\n\nemail id for "{query}"\n\n\n'
contactfile.write(linex)
for url in search ( query, num = 100, stop = 1000, pause = 1 ) :
    try:
        get_all_email(url)
        #get_all_number(url)

    except:
        print("something went rowng")
        continue

print(all_email)
print(all_contact)
contactfile.close()
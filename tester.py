import requests
import urllib.parse
from lxml import html
from bs4 import BeautifulSoup

def extract_school_info_new(address, zip):
    url = "https://geocode.maps.co/search?q="
    property_address = urllib.parse.quote(address)
    property_address = property_address + "%20" + str(zip)
    resp = requests.get(url + property_address)
    if resp.status_code == 200:
        jdata = resp.json()
        lat = jdata[0]['lat']
        lon = jdata[0]['lon']
        r = requests.get("https://www.har.com/api/tax-assign-schools?lat=" + lat + "&lng=" + lon)
        print("https://www.har.com/api/tax-assign-schools?lat=" + lat + "&lng=" + lon)
        schools_json = r.json()
        schools_json = schools_json['html']

        soup = BeautifulSoup(schools_json, 'html.parser')
        school_elements = soup.find_all('div', class_='col-12 col-md-4')
        elementary_schools = []
        middle_schools = []
        for school_element in school_elements:
            label_element = school_element.find('div', class_='card--portrait_school__label')
            if label_element:
                label_text = label_element.text.strip()
                if 'Elementary School' in label_text:
                    school_name_element = school_element.find('h3', class_='pt-4 mb-1')
                if school_name_element:
                    elementary_schools.append(school_name_element.text.strip())
            elif 'Middle School' in label_text:
                school_name_element = school_element.find('h3', class_='pt-4 mb-1')
                if school_name_element:
                    middle_schools.append(school_name_element.text.strip())
        
        print("Elementary Schools:", elementary_schools)
        print("Middle Schools:", middle_schools)

    else:
        print("no geo")


extract_school_info_new('5317 Val Verde St', 77056)

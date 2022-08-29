from my_scraping_functions import section_div_image_scraping, section_div_text_scraping
from bs4 import BeautifulSoup
import time 
import requests

def blog_kodius_pangea (url = None):
    source = requests.get("https://kodius.com/blog/kodius-top-7-percent-at-pangea").text
    soup = BeautifulSoup(source,"lxml")
    
    """ CENTRAL """
    main_path = soup.find("div",{"class":"column is-9 article-area"})
    images = main_path.find_all("img")
    all_h1 = main_path.find_all("h1")
    pangea_image = images[0]["src"]
    print("Pangea iamge link:",pangea_image)
    
    blog_title =  all_h1[0].text
    blog_tags = main_path.find("div",{"class":"blog-tags"}).text
    print("Blog title:",blog_title)
    print(blog_tags)
    print("--"*20)
    
    all_h2 = main_path.find_all("h2")
    intro = all_h2[0].text
    print(intro)
    print("_"*20)
    
    all_p = main_path.find_all("p")
    desc  = all_p[0].text 
    print(desc)
    print("_"*20)
    
    h2_Journey = all_h2[1].text
    print(h2_Journey)
    p_Journey = all_p[1].text
    print(p_Journey)
    img_Journey = images[2]["src"]
    print("Image link:",img_Journey)
    
    h2_Journey_2  = all_h2[2].text 
    print(h2_Journey_2)
    p_Journey_2 = all_p[3].text
    print("--"*20)
    print(p_Journey_2)
    sup_text = all_p[5].text
    print(sup_text)
    
    Journey_image = images[4]["src"]
    print(f"Image link: {Journey_image}")
    paragraph = "\n".join( x.text for x in all_p[6:8])
    print(paragraph)
    
    list_elements = main_path.find("ul")
    list_li = list_elements.find_all("li")
    list_of_all = []
    for elements in list_li:
        list_of_all.append(elements.text)
    print(list_elements.text)
    
    counter = 1 
    for items in list_of_all:
        print(f"{counter}. {items}")
        counter += 1
    
    more_paragraph = "\n".join(x.text for x in all_p[8:11])
    print(more_paragraph)
    
    conclusion = all_h2[3].text
    print("*"*20)
    print(conclusion)       
    conc_parag = all_p[12].text
    print(conc_parag)
    print("-"*40)
    
    """  MORE FROM BUSINESS """
    more_from_business_section = soup.find("section",{"class":"section is-paddingless1"})
    title = more_from_business_section.h2.text
    block_item_content = more_from_business_section.find_all("div",{"class":"blog-item-content"})
    images = []
    text = []
    summary = []
    h2_text = []
    for items in range(len(block_item_content)-1): # -1 because one element does not exist, but python calculates it!
        images.append(block_item_content[items].img["src"])
        text.append(block_item_content[items].text)
        summary.append((block_item_content[items]).find("div",{"class":"blog-item-summary"}).text)
        h2_text.append(block_item_content[items].h2.text)
           
    print(title)
    for result in range(len(images)):
        print(f"Image link: {images[result]}")
        print(f"{text[result]}")
        print(h2_text[result]) 
        print(summary[result])
        print("*"*40)
    


def blog_kodius_clutch (url = None):
    source = requests.get("https://kodius.com/blog/kodius-clutch-2021-rewind/").text
    soup = BeautifulSoup(source,"lxml")
    
    """ Kodius` Clutch 2021 Rewind """
    image = soup.find("div",{"class":"header-image"}).img["src"]
    print("Header image link:",image)    
    title = soup.find("div",{"class":"columns"}).h1.text
    print(title)
    title_tag = soup.find("div",{"class":"blog-tags"}).text
    print(title_tag)
    columns_h2 = soup.find("div",{"class":"columns"}).find_all("h2")
    columns_p = soup.find("div",{"class":"columns"}).find_all("p")
    intro = columns_h2[0].text
    print(intro)
    print("-"*20)
    intro_paragraph = "\n".join([x.text for x in columns_p[0:2]])
    print(intro_paragraph)
    print()
    
    """2021 IN REVIEW """
    _2021 = columns_h2[1].text
    print(_2021)
    print("-"*20)
    paragraph_2021 = "\n".join([x.text for x in columns_p[2:6]])
    print(paragraph_2021)
    first_img = columns_p[5].find_all("img")[0]["src"]
    second_img = columns_p[5].find_all("img")[1]["src"]
    print("First image:",first_img)
    print("Second image:",second_img)
    
    """ FUTURE PROJECTS """
    future_projects = columns_h2[2].text
    print(future_projects)
    print("-"*20)
    future_paragraph = "".join([x.text for x in columns_p[6:10]])
    print(future_paragraph)
    
    print("""  MORE FROM BUSINESS """)
    more_from_business_section = soup.find("section",{"class":"section is-paddingless1"})
    title = more_from_business_section.h2.text
    block_item_content = more_from_business_section.find_all("div",{"class":"blog-item-content"})
    images = section_div_image_scraping("section","https://kodius.com/blog/kodius-clutch-2021-rewind/","section is-paddingless1","div","class","blog-item-content","img")
    text = section_div_text_scraping("section","https://kodius.com/blog/kodius-clutch-2021-rewind/","section is-paddingless1","div","class","blog-item-content")
    summary = []
    h2_text = []
    print(h2_text)
    for items in range(len(block_item_content)-1): # -1 because one element does not exist, but python counter it!
        summary.append((block_item_content[items]).find("div",{"class":"blog-item-summary"}).text)
        h2_text.append(block_item_content[items].h2.text)
           
    print(title)
    for result in range(len(images)):
        print(f"Image link: {images[result]}")
        print(f"{text[result]}")
        print(h2_text[result]) 
        print(summary[result])
        print("*"*40)
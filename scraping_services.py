from bs4 import BeautifulSoup
from my_scraping_functions import complex_sec_div_scraping, section_div_image_scraping, section_div_text_scraping 
import requests
import time

""" Scraping all services page """

def custom_software (url = None):
    # start_time = time.time()
    source = requests.get("https://kodius.com/services/custom-software").text
    soup = BeautifulSoup(source,'lxml')
    
    """ 'Build to win market' on site """
    print("START")
    first_div = soup.find("div",{"class":"width"})
    title = first_div.h1.text
    intro_text = first_div.find("div",{"class":"intro-text"}).text
    text_to_link = first_div.a.text
    link = first_div.find("a")["href"]
    text = first_div.p.text
    print(title)
    print(intro_text)
    print(f"{text_to_link}: https:/{link}")
    print(text)
    
    #crete image field
    image_class = first_div.find("div",{"class":"o-image"}).find("img")["src"]
    print(f"Image link: {image_class}")
    
    """ TOGGLE TO SEE A DIFFERENCE """
    toggle_path = soup.find("section",{"class":"row with-or-without-us dark"})
    toggle_text = toggle_path.find("div",{"class":"dare-to-switch"}).h2.text
    loop_div = toggle_path.find("div",{"class":"without-bullets"}).find_all("div",{"class":"more-details"})
    print(toggle_text)
    for details in range(len(loop_div)):
        print(f"? {loop_div[details].text}")
    
    print(""" Building a new product """)
    mvp_section = soup.find("section",{"class":"mvp"})
    bold_text  = mvp_section.find("div",{"class":"picture-text"}).find_all("p")
    for article in range(len(bold_text)):
        print(bold_text[article].text)
    print("*"*40)

    
    """ CUSTOM SOFTWARE BENEFITS"""
    try:
        custom_software = soup.find("section",{"class" :  "row why-custom"})
        title = custom_software.find("h2").text
    except AttributeError:
        title = None
    finally:         
        print(title)
    
    try:
        description_list = soup.find("main", {"class":"row custom-software"})
        description_list = description_list.find("dl",{"class":"vsa-list"})
    except AttributeError:
        print(None)
    finally:
        print("**"*20)
    
    
    """  HOW TO START """
    start_section = soup.find("section",{"class":"row our-process"})
    start_text = start_section.h2.text
    start_description = start_section.div.text
    print(start_text)
    print(start_description)
    print('**'*20)
    
    """ Make an appointment """
   
    section = section_div_text_scraping("section","https://kodius.com/services/custom-software","row our-process-steps","div","class","head-box")
    section_title =section_div_text_scraping("section","https://kodius.com/services/custom-software","row our-process-steps","h2","class","title")
    section_text = section_div_text_scraping("section","https://kodius.com/services/custom-software","row our-process-steps","div","class","text-box")
    section_image = soup.find("section",{"class":"row our-process-steps"}).find_all("img")
    section_image = section_div_image_scraping("section","https://kodius.com/services/custom-software","row our-process-steps")
    for result in range(len(section)):
        print(section[result])
        print("Title: ",section_title[result])
        print(section_text[result])
        print("Image link:",section_image[result])
        print("--"*20)
    
    """  START DEVELOPING NOW """
    develop_section = soup.find("section",{"class":"row custom-banner"})
    title = develop_section.h2.text
    link = develop_section.a["href"]
    link_text = develop_section.a.text
    print(title)
    print(f"{link_text}: https:/{link}")
    
    """  WHAT TO EXPECT """
    expect_section = soup.find("section",{"class":"row custom-software-devs"})
    head = expect_section.find_all("p")[0].text
    print(head)
    title = expect_section.h2.text
    print(title)
    text = expect_section.find_all("p")[1].text    
    print(text)
    print("**"*20)
    
    """ TECHNOLOGIES USED """
    technologies_section = soup.find("section",{"class","row techs"})
    title = technologies_section.h2.text 
    print(title)   

    all_links = section_div_text_scraping("section","https://kodius.com/services/custom-software","row techs","ul","class","tech-by-tech","a")
    all_images = section_div_image_scraping("section","https://kodius.com/services/custom-software","row techs","ul","class","tech-by-tech","img")
    all_title = section_div_text_scraping("section","https://kodius.com/services/custom-software","row techs","ul","class","tech-by-tech","h4")    
    all_desc = section_div_text_scraping("section","https://kodius.com/services/custom-software","row techs","ul","class","tech-by-tech","p")        
    for all in range(len(all_links)):
        print(all_title[all])
        print(f"Title link: https:/{all_links[all]}")    
        print("Image link:",all_images[all])
        print("Description:",all_desc[all])
        print("--"*20)
    
    button = soup.find("div",{"class": "pointer-fix"}).text
    print(f"Button: {button}")
    
    paragraph_tech = technologies_section.find_all("p")[::-1][0].text
    print(paragraph_tech)
    
    """ ROW PRICING """
    rowpricing_section = soup.find("section",{"class":"row pricing"})
    title = rowpricing_section.h2.text
    rowpricing_div = rowpricing_section.find_all("div")
    first_rp_div = rowpricing_div[0].text
    second_rp_div = rowpricing_div[1].text
    print(title)
    print(first_rp_div)    
    print(second_rp_div)    
    
  
def ux_ui (url = None):
    source = requests.get("https://kodius.com/services/ui-ux").text
    soup = BeautifulSoup(source,"lxml")
    
    """ ux-ui-intro """
    intro = soup.find("div",{"class":"ux-ui-intro"})
    title = intro.h1.text
    first_div = intro.find_all("div")[0].text
    second_div = intro.find_all("div")[1].text
    link_text = intro.a.text
    link = intro.a["href"]
    print(title)
    print(first_div)
    print(second_div)
    print(f" {link_text}: https:/{link}")
    
    """ COVER IMAGE """
    cover = soup.find("div",{"class" : "coverImage"})
    image = cover.find("img")["src"]
    print("Image link:",image)
    print("--"*20)
    
    """ PRODUCT DESIGN PROCES """
    text = soup.find("div",{"class":"owl__title"}).text
    print(text)
    
    """ UX PROCESS"""
    process = soup.find("section",{"class":"row ux-ui-process"})
    title = process.h2.text
    print(title)
    print("*"*29)
    number = complex_sec_div_scraping("section","https://kodius.com/services/ui-ux","row ux-ui-process","div","class","ux-process-grid","div","class","ux-number")
    title_elements = complex_sec_div_scraping("section","https://kodius.com/services/ui-ux","row ux-ui-process","div","class","ux-process-grid","div","class","ux-title")
    text_elements = complex_sec_div_scraping("section","https://kodius.com/services/ui-ux","row ux-ui-process","div","class","ux-process-grid","div","class","ux-text")
    print(text_elements)
    
    for result in range(len(number)):
        print(number[result])
        print("Title:",title_elements[result])
        print(text_elements[result])
        print("--"*20)
        
     
    """ DESIGN PROCESS """   
    process = soup.find_all("section",{"class":"row ux-ui-process"})[1]   
    title = process.h2.text
    print(title)
    all_card = process.find("div",{"class":"ux-process-grid"})
    number_elements = all_card.find_all("div",{"class":"ux-number"})
    title_elements = all_card.find_all("div",{"class":"ux-title"})
    text_elements = all_card.find_all("div",{"class":"ux-text"})
    number = []
    title = []
    text = []

    for article in range(len(number_elements)):
        number.append(number_elements[article].text)
        title.append(title_elements[article].text) 
        text.append(text_elements[article].text)  
    
    for result in range(len(number)):
        print(number[result])
        print("Title:",title[result])
        print(text[result])
        print("--"*20)
        
    """" LAST CASE STUDY """
    last_case_div = soup.find("div",{"class":"latestCase"})
    title = last_case_div.h2.text
    print(title)
    image_link = None
    try: 
        image_link = soup.find("div",{"class":"desktop-only"}).find_all("img")[0]["src"]
    except AttributeError:
         pass     
    print("Image link:",image_link)
    
    text = soup.find("section",{"class":"studies-with-selector"}) ###### SOMETHING WRONG #### The result is not shown

    """ RECOGNITIONS """ 
    recognitions = soup.find("section",{"class":"row ux-ui-testimonials"})
    title = recognitions.find("div",{"class":"title-clutch"}).h2.text
    print(title)
    all_images = recognitions.find("div",{"class":"title-clutch"}).find_all("img")
    print(f"First icon:",all_images[0]["src"])
    print(f"Second icon:",all_images[1]["src"])
    testimonials = recognitions.find("div",{"class":"testimonials-wrapper"}).find_all("div","q-text")
    tests = []
    for testimony in range(len(testimonials)):
            tests.append(testimonials[testimony].text)
    print("TESTIMONIALS:")
    for result in range(len(tests)):
        print(tests[result])
        print("-"*20)
    
    """ WOULD YOU LIKE TO JOIN OUR TEAM """
    title = soup.find("div",{"class":"positions"})
    paragraph = title.p.text
    title = title.h2.text
    print(title)
    print(paragraph)
    
    
def hire_developers(url = None):
    source = requests.get("https://kodius.com/services/hire-developers").text
    soup = BeautifulSoup(source,"lxml")
    
    """ Hiring developer - first section"""    
    hiring_dev = soup.find("section",{"class":"row top-developers"})
    title = hiring_dev.h1.text
    paragraph = hiring_dev.div.text
    link_text = hiring_dev.a.text
    link = hiring_dev.a["href"]
    print(title)
    print(paragraph)
    print(f"{link_text}: https:/{link}")
    print("*"*20)
    
    """Companies link """
    com_link = soup.find("section",{"class":"row trusted-banner"})
    title = com_link.div.text
    clutch_link = com_link.find("div",{"class":"clutch grayscale desktop"}).a["href"]
    print(title)
    print("Clutch:",clutch_link)
    pangea_link = com_link.find("div",{"class":"pangea desktop grayscale"}).a["href"]
    print("Pangea:",pangea_link)
    amplifyre_link = com_link.find("div",{"class":"amplifyre desktop grayscale"}).a["href"]
    print("Amplifyre:",amplifyre_link)
    
    """   Technologies """
    all_tech = soup.find_all("section",{"class":"row single-tech"})
    images_link  = []
    first_paragraph = []
    second_paragraph = []
    third_paragraph = [] 
    for items in range(len(all_tech)):
        images_link.append(all_tech[items].find("img")["src"])
        first_paragraph.append(all_tech[items].find("div",{"class":"tech-text-box"}).find_all("p")[0].text)
        second_paragraph.append(all_tech[items].find("div",{"class":"tech-text-box"}).find_all("p")[1].text)
        third_paragraph.append(all_tech[items].find("div",{"class":"tech-read-wrapper"}).find("p").text)
        
    for result in range(len(images_link)):
        print("Image link:",images_link[result])
        print(first_paragraph[result])
        print(second_paragraph[result])
        print(third_paragraph[result])
        print("--"*20)
        
    print(""" OTHERS INFO """) 
    big_numbers = [6,9,30,1800]
    headlines = section_div_text_scraping("div","https://kodius.com/services/hire-developers","numbers-wrapper","div","class","headline")
    text = section_div_text_scraping("div","https://kodius.com/services/hire-developers","numbers-wrapper","div","class","text")
    
    for result in range(len(big_numbers)):
        print(big_numbers[result])
        print(headlines[result])
        print(text[result])
        print("*"*40)
    
    
    """ More About Technologies"""    
    section = soup.find_all("section",{"class":"row single-tech"})
    title = []
    description = []
    read_more = []
    for items in range(len(section)-3):
        title.append(section[items+3].p.text)
        description.append(section[items+3].find("p",{"class":"tech-statement"}).text)
        read_more.append(section[items+3].find("p",{"class":"tech-read"}).text)
    
    for result in range(len(title)):
        print("Title:",title[result])
        print(description[result])
        print(read_more[result])
        print("--"*20)
    
    """ RECOGNITIONS """
    recognitions = soup.find("section",{"class":"row about-devs-testimonials"})
    rec_title = recognitions.h2.text
    print(rec_title)
    all_images = recognitions.find("div",{"class":"title-clutch"}).find_all("img")
    print(f"First icon:",all_images[0]["src"])
    print(f"Second icon:",all_images[1]["src"])
    testimonials = recognitions.find("div",{"class":"testimonials-wrapper"}).find_all("div","q-text")
    tests = []
    for testimony in range(len(testimonials)):
            tests.append(testimonials[testimony].text)
    print("*"*40)
    for result in range(len(tests)):
        print(tests[result])
        print("-"*20)


from bs4 import BeautifulSoup
from my_scraping_functions import section_div_text_scraping
import requests
import time 

#path for website (homepage)
def scraping_kodius_home_page(url = None):
    
        # time_start = time.time()
        source = requests.get("https://kodius.com/").text
        soup = BeautifulSoup(source,'lxml')
        section_wrapper = soup.find("div",{"class": "landing-hero-text-and-btn-container mobile"})
        
        #find all h1 tags in class landing-hero-text-and-btn-container mobile
        landing_hero = section_wrapper.find_all("h1")
        first_landing_hero =  landing_hero[0].text
        second_landing_hero = landing_hero[1].text
        print(first_landing_hero)
        print(second_landing_hero)
        
        #find all h2 tags in class landing-hero-text-and-btn-container mobile
        landing_hero_story = section_wrapper.find_all("h2")[0].text
        print(landing_hero_story)
        
        #find all b tags in class landing-hero-text-and-btn-container mobile
        landing_hero_b = section_wrapper.find_all("b")[0].text#print()
        print(landing_hero_b)
        
        #find all buttons tags in class landing-hero-text-and-btn-container mobile
        button = soup.find("div",{"class": "pointer-fix"}).text
        print(f"Button: {button}")
    
        print("IMAGES and LINKS")    
        "image links"
        all_images = soup.find("div",{"class" : "logos"})
        links = []
        images = []
        for elements in all_images:
            links.append(elements["href"])
            images.append(elements.find("img")["src"])    
            
        pangea_link = links[0]
        pangea_paragraph = all_images.find("div",{"class","pangea"}).p.text
        clutch_link = links[1]
        print(f"{pangea_paragraph}:",pangea_link)
        print("Pangea image link:",images[0])
        print("Clutch link:",clutch_link)
        print("Clutch image:",images[1])
        
        
        
        """               SECTION              """
        first_section = soup.find("section",{"class":"case-mobile"})
        section_title = first_section.find("div",{"class":"main-wrapper"}).find_all("h1")[0].text
        print(section_title)      
        
        #sigle wrapper 0-5 elements i row
        counter = 0
        flag = True
        while flag:
              if counter >= 6:
                  flag = False
              else:    
                six_wrappers_in_row = first_section.find("div",{"id":f"{counter}"})
                small_title = six_wrappers_in_row.find("div",{"class":"small-title"}).text
                small_subtitle = six_wrappers_in_row.find("div",{"class":"small-subtitle"}).text
                big_title = six_wrappers_in_row.find("div",{"class":"bigTitle"}).text
                big_subtitle = six_wrappers_in_row.find("div",{"class":"bigSubtitle"}).text
                study_link = six_wrappers_in_row.find("div",{"class":"text-block"}).find("a")["href"]
                study_link_text = six_wrappers_in_row.find("div",{"class":"text-block"}).find("span").text
                
                images_div = six_wrappers_in_row.find("div",{"class":"image-block"})
                first_image_link = images_div.find("div",{"class":"relative"}).find("img")["src"]
                
                print(small_title)
                print(small_subtitle)
                print(big_title)
                print(big_subtitle)
                print(f"{study_link_text}: {study_link}")
                print("Image`s link:",first_image_link)
                print("-"*50)
                counter += 1
        
        
        
        print("title: TESTIMONIALS")
        testimonial_section = soup.find("section",{"class":"row testimonials-separate-title"})
        testimonial_title = testimonial_section.find("h2", {"class":"title"}).text
        testimonial_lead_in = testimonial_section.find("div",{"class":"lead-in"}).text
        test_name = soup.find("div",{"class": "testimonial-credentials-wrapper"})
        test_jobtitle = test_name.find("div",{"class": "testimonial-jobtitle-wrapper"})
        first_testimonial   = test_name.find("h4",{"class":"testimonial-name"}).text
        first_testimonial_job   = test_jobtitle.find("p",{"class":"tt-jobtitle"}).text
        print(testimonial_title)
        print(testimonial_lead_in)
        print(first_testimonial)
        print(first_testimonial_job)
        
        try:
          first_testimonial_company   = test_jobtitle.find("p",{"class":"tt-company"}).text
        except Exception as e:
            first_testimonial_company = None
        print(first_testimonial_company)    
    
        testimonial_recommendation =  soup.find("div",{"class":"testimonials-wrapper"}).find("div",{"class":"testimonial-recommendation"})
        testimonial_recommendation = testimonial_recommendation.find("p",{"class":"tt-quote"}).text 
        print(testimonial_recommendation)
        
        """  Build new digital product section  """
        section_dp = soup.find("section",{"class":"colored-bottom"})
        title_text_first_path = section_dp.find_all("p",{"class" : "bold"})[0].text
        title_text_second_path = section_dp.find_all("p",{"class" : "bold"})[1].text
        print(title_text_first_path,title_text_second_path)
        description = section_dp.find("p",{"class":"text"}).text
        print(description)
        image = soup.find("div",{"class":"wrapper"}).find("div",{"class":"book-img__wrapper"}).find("img")["src"]
        print("Image link:",image)
 
        """  SERVICES SECTION   """
        service_section = soup.find("section",{"class":"row home-root-links"})
        service_title = service_section.find_all("div",{"class":"wrapper"})
        print("Title:",service_title[0].h2.text)      
        service_description = service_title[1].h4.text
        print("Description:",service_description)
        
        
        """  ARTICLES """
        job_title  =  section_div_text_scraping("div","https://kodius.com/","article-wrapper","p","class","op-job-title")
        job_experience = section_div_text_scraping("div","https://kodius.com/","article-wrapper","p","class","op-job-experience-location")
        read_more = section_div_text_scraping("div","https://kodius.com/","article-wrapper","p","class","tech-read")
        print(job_title)
           
        for all in range(len(job_title)):
            print("Title:",job_title[all])
            print("Experience:",job_experience[all])
            print(read_more[all])
            print("**"*20)
        
        
        print(""" OTHERS INFO """) 
        big_numbers = [6,9,30,1800]
        headlines = section_div_text_scraping("div","https://kodius.com/","numbers-wrapper","div","class","headline")
        text = section_div_text_scraping("div","https://kodius.com/","numbers-wrapper","div","class","text")
        
        for result in range(len(big_numbers)):
            print(big_numbers[result])
            print(headlines[result])
            print(text[result])
            print("*"*40)
            
        """ TEAM CULTURE """
        print("TEAM CULTURE")
        team_source = soup.find("section",{"class":"team-culture"})
        team_title = team_source.h2.text
        context = team_source.h4.text
        picture = team_source.find("picture",{"class":"image"}).find("img")["src"]
        print(team_title)
        print(context)
        print(picture)


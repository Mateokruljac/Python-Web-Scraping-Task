from bs4 import BeautifulSoup
import requests



def section_div_text_function(tag,link,class_,elements,clas = None,class_value = None,more_elements = None):
    """  tag indicates the element you are searching for, SECTION or DIV.
    link is the link address from which we search.
    class_ is the name of the tag class.
    elements is what we look for in class.
    We can add more classes and elements, but it is not mandatory.
    
    For example: 
        div_class.find(f"{tag}",{"class":f"{class_}"}).find(f"{elements}",{f"{clas}":f"{class_value}"}).find_all(f"{more_elements}")
    
    This function retun list of elements
    """

    source = requests.get(f"{link}").text
    div_class = BeautifulSoup(source,"lxml")
    if clas == None and class_value == None :
        div = div_class.find(f"{tag}",{"class":f"{class_}"}).find_all(f"{elements}")
    

    else:
        if more_elements == None:  
          div = div_class.find(f"{tag}",{"class":f"{class_}"}).find_all(f"{elements}",{f"{clas}":f"{class_value}"})
        else:
          div = div_class.find(f"{tag}",{"class":f"{class_}"}).find(f"{elements}",{f"{clas}":f"{class_value}"}).find_all(f"{more_elements}")
              

    element_list = []
    for items in range(len(div)): 
        if div != False:
          element_list.append(div[items].text)    
        
        if elements == "img":
            element_list.append(div[items].img["src"])  
    
        
    return element_list


def complex_sec_div_func(tag,link,class_,elements,clas,class_value,more_elements,c_val = None,c_val_2 = None):
    """ tag indicates the element you are searching for, SECTION or DIV.
    link is the link address from which we search.
    class_ is the name of the tag class.
    elements is what we look for in class.
    clas element should be CLASS or ID,
    class_value is equal to third parameter and 
    more_elements is equal to forth.
    
    For example:
    name = div_class.find(f"{tag}",{"class":f"{class_}"}).find(f"{elements}",{f"{clas}":f"{class_value}"}).find_all(f"{more_elements}",{f"{c_val}":f"{c_val_2}"})
    
    This function retun list of elements in string (text)"""
    source = requests.get(f"{link}").text
    div_class = BeautifulSoup(source,"lxml")
    div = div_class.find(f"{tag}",{"class":f"{class_}"}).find(f"{elements}",{f"{clas}":f"{class_value}"}).find_all(f"{more_elements}",{f"{c_val}":f"{c_val_2}"})
    element_list = []
    for items in range(len(div)): 
        if div != False:
          element_list.append(div[items].text)    
        
        
    return element_list



def section_div_image_function(tag,link,class_,elements = "img",clas = None,class_value = None,more_elements = None):
    """  tag indicates the element you are searching for, SECTION or DIV.
    link is the link address from which we search.
    class_ is the name of the tag class.
    elements is what we look for in class. DEFAULT - > IMG 
    We can add more classes and elements, but it is not mandatory.
    
    For example: 
        div_class.find(f"{tag}",{"class":f"{class_}"}).find(f"{elements}",{f"{clas}":f"{class_value}"}).find_all(f"{more_elements}")
                                              OR 
                                            
        div_class.find(f"{tag}",{"class":f"{class_}"}).find_all("img")
    This function retun list of elements ("IMAGE!!!!")
  
    """
    
    source = requests.get(f"{link}").text
    div_class = BeautifulSoup(source,"lxml")
    if clas == None and class_value == None:
      div = div_class.find(f"{tag}",{"class":f"{class_}"}).find_all("img")

    else:
        div = div_class.find(f"{tag}",{"class":f"{class_}"}).find(f"{elements}",{f"{clas}":f"{class_value}"}).find_all(f"{more_elements}")
        
       
    element_list = []
    for items in range(len(div)): 
        if div != False:
          element_list.append(div[items]["src"])    
        
    return element_list



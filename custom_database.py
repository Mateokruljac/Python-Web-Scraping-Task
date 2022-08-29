import sqlite3
from sqlite3 import Error
from error_raising import WebsiteNotFoundError,ShortestPathNotFoundError

#create database and table
connection = sqlite3.connect("python_task")
my_cursor  = connection.cursor()

def create_table():
    try:
        my_cursor.execute("""CREATE TABLE IF NOT EXISTS url_path( 
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    url_value CHAR(300))
                                    """)
        connection.commit()
    except Error as e:
        print(e)
            
    return 

create_table()


#insert into database
def add_new_url():
    new_url = input("URL (copy+paste): ")
    try:
     my_cursor.execute(""" INSERT INTO url_path(url_value)  VALUES (?)""",(new_url,))
     connection.commit()
     print("Successfully added!")
     print("*"*18)
    except Error as e:
        print(e)
    return 



#separate by /
def split_function(url):
    """ remove htttp:// from function and split function by / 
    """
    
    get_url = str(url).removeprefix("https://")
    get_url = get_url.removesuffix("/")
    get_url = get_url.split("/")
    
    return get_url   
    

#select from database 
def get_shortest_path (url):
    """ 
    pass the function for which you want to get the shortest path
    """
    parsed_url = split_function(url) #
    START_URL  = parsed_url[0] 
    END_URL    = parsed_url[-1] 
    DEPTH      = 2 #default   
    #if start_url exists!
    if START_URL and  "https://"  in url:

        my_cursor.execute(f"SELECT url_value from url_path where url_value like 'https://{START_URL}%' and url_value like '%{END_URL}' or url_value like '%{END_URL}/' ")
        get_value = my_cursor.fetchall()
        #result can not be empty list   
        if bool(get_value) is not False:
            get_value_empty_list = []
           
            for x in range (len(get_value)):
                # for the first element in each list, although list has only one element, because it is two-dimensional list
                get_value_empty_list.append(split_function(get_value[x][0]))   
            
            more_then_one_element = [] # more then START_URL
            for x in range (len(get_value_empty_list)):
                  if len(get_value_empty_list[x]) > 1: # 
                   more_then_one_element.append(get_value_empty_list[x])
                
            if bool(more_then_one_element) == False:
                DEPTH = len(get_value_empty_list)
                raise WebsiteNotFoundError(message="Website not have end_url")   
                
            more_then_start_and_end = []
            list_result = [] 
            result = ''
            counter = 1
            for x in range (len(more_then_one_element)): 
                   try:
                    # if more_then_one_element has 3 elements or more, it will be stored in more_then_start_and_end.
                    if len(more_then_one_element[x]) > 2:
                        more_then_start_and_end.append(more_then_one_element[x])         
                  
                   except:
                           #if more_then_one_element has 2 or fewer elements, it will be stored in clear_more_then_one
                           list_result = [] 
                           result = ''
                           clear_more_then_one = []
                           clear_more_then_one.append(more_then_one_element[x])  
                                  
                           for x in range (len(clear_more_then_one)):
                               print(f"{counter}. OPTION ")
                               print("*"*18)
                               list_result.clear()
                               for y in range (len(clear_more_then_one[x])):    
                                   # final result will be stored in list_result
                                   list_result.append(clear_more_then_one[x][y])
                                   #then stored in result string
                                   result = ' '.join(list_result)
                                   result = result.replace(" ","/")
                                   if len(list_result) > 2 and  DEPTH <= len(list_result):
                                       DEPTH += 1
            
                                   else:
                                       pass
                                   print(f"{x+1}.   https://{result}")
                               if len(list_result) < 2:
                                   DEPTH = len(list_result)
                                      
                               print("Depth:",DEPTH)
                               print()
                               counter += 1
                         
                           raise ShortestPathNotFoundError(message=f"Shortest path does not exist. you only have start and final url[start: {get_value[0]}, end: {get_value[1]}")             
            if bool(more_then_start_and_end) == False:
                raise ShortestPathNotFoundError()                  
            for i in range (len(more_then_start_and_end)):     
                print(f"{counter}. OPTION ")
                print("*"*18)
                list_result.clear()
                for y in range (len(more_then_start_and_end[i])):
                    list_result.append(more_then_start_and_end[i][y])
                    result = " " .join(list_result)
                    result = result.replace(" ","/")
                    print(f"{y+1}.   https://{result}")
                    if len(list_result) > 2:
                        DEPTH += 1
                        if DEPTH > len(list_result):
                            DEPTH = len(list_result)
                    else:
                        pass
                print("Depth:",DEPTH)    
                print()
                counter += 1           
            
     

        else:
           DEPTH = len(get_value)
           raise WebsiteNotFoundError()
    else:
        DEPTH = 0
        raise WebsiteNotFoundError()            
    
   


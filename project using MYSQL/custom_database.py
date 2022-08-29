import mysql.connector
from error_raising import WebsiteNotFoundError,ShortestPathNotFoundError

#database
my_database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "url_path"
)

#cursor
my_cursor = my_database.cursor()

#insert into database
def add_new_url():
    new_url = input("URL (copy+paste): ")
    try:
     my_cursor.execute(f"""INSERT INTO url_path (url_value) VALUE ('{new_url}')
                      """)
     my_database.commit()
     print("Successfully added!")
     print("*"*18)
    except:
        raise ConnectionError(message = "Something went wrong!")
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
    """ parse url path
    """
    parsed_url = split_function(url)
    START_URL  = parsed_url[0]
    END_URL    = parsed_url[-1]
    DEPTH = 2
    
    #if start_url exists!
    if START_URL  and  "https://"  in url:
        my_cursor.execute(f"SELECT url_value from url_path where url_value like 'https://{START_URL}%' and url_value like '%{END_URL}' or url_value like '%{END_URL}/'")
        get_value = my_cursor.fetchall()

        if bool(get_value) is not False:
            get_value_empty_list = []
            for x in range (len(get_value)):
                 get_value_empty_list.append(split_function(get_value[x][0]))          
            
            more_then_one_element = []
            for x in range (len(get_value_empty_list)):
               if len(get_value_empty_list[x]) > 1: # if has at least start_url and end_url exist! 
                 more_then_one_element.append(get_value_empty_list[x])
               else:
                   pass
            
            if bool(more_then_one_element) == False:
                DEPTH  = 1
                raise WebsiteNotFoundError()  
            list_result = []
            result = ''
            more_then_start_and_end = []
            counter= 1
            for x in range (len(more_then_one_element)): 
                               
                try:
                    if len(more_then_one_element[x]) > 2:
                        more_then_start_and_end.append(more_then_one_element[x])
                       
                except:
                           list_result = []
                           result = ''
                           clear_more_then_one = []
                           clear_more_then_one.append(more_then_one_element[x])  
                                  
                           for x in range (len(clear_more_then_one)):
                               for y in range (len(clear_more_then_one[x])):    
                                   list_result.append(clear_more_then_one[x][y])
                                   result = ' '.join(list_result)
                                   result = result.replace(" ","/")
                                   print(f"{counter}. OPTION ")
                                   print("*"*18)
                                   print(f"{x+1}.   https://{result}")
                                   if len(list_result) > 2:
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
                raise WebsiteNotFoundError()
                           
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
                    else:
                        pass
                print("Depth:",DEPTH) 
                print()
                counter += 1
                          
                               
   
        else:
           DEPTH = 0
           raise WebsiteNotFoundError()
    else:
        DEPTH = 0
        raise WebsiteNotFoundError()            
    
   
get_shortest_path("https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/?ref=leftbar-rightbar")
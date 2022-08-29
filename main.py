from custom_database import create_table,add_new_url, get_shortest_path
from scraping_blog import blog_kodius_clutch, blog_kodius_pangea
from scarping_homepage import scraping_kodius_home_page
from scraping_services import custom_software, hire_developers,ux_ui
import time
import typer

app = typer.Typer()
#this function able to create table
create_table()

#if you want to add new url-----------> add_new_url


"""
The following links has only one option. If you want to see how more options looks, please pass the following link:

https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/?ref=leftbar-rightbar

Maybe you have to add this link to database    add_new_url()
"""
    


@app.command()#decorator
def  main(url: str):
    if url == "https://kodius.com/":
       scraping_kodius_home_page()
       time.sleep(2)
       get_shortest_path(url)
    
    elif url == "https://kodius.com/blog/kodius-top-7-percent-at-pangea":
        blog_kodius_pangea()
        time.sleep(2)
        get_shortest_path(url)
    
    elif url == "https://kodius.com/blog/kodius-clutch-2021-rewind/":
        blog_kodius_clutch()
        time.sleep(2)
        get_shortest_path(url)
    
    elif url == "https://kodius.com/services/custom-software":  
         custom_software()
         time.sleep(2)
         get_shortest_path(url)
    
    elif url == "https://kodius.com/services/ui-ux":
        ux_ui()
        time.time(2)
        get_shortest_path(url)
    
    elif url == "https://kodius.com/services/hire-developers":
        hire_developers()
        time.sleep(2)
        get_shortest_path(url)
    
    else:
        get_shortest_path(url)
    
     


if __name__ == "__main__":
    app()
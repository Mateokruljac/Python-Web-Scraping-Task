from error_raising import WebsiteNotFoundError,ShortestPathNotFoundError
from custom_database import split_function,my_cursor
import unittest

class TestException(unittest.TestCase):    
    
    def setUp(self):
        self.name = self.shortDescription()
        print(f"Test: {self.name}")
        
    def tearDown(self):
        print("Test done!")
        
    
    @classmethod
    def tearDownClass(cls):
        print("All tests finished!")
    
    @classmethod
    def setUpClass(cls):
        print("START TESTING") 
    
    
    def test_shortest_path_error(self):
        """  
        Check Exception ShortestPathNotFoundError
        """
        url = "https://kodius.com/blog/"     
        parsed_url = split_function(url)    
        if len(parsed_url) <= 2:
            self.assertRaises(ShortestPathNotFoundError,msg ="Short path not found!")
    
    def test_web_not_exists_case1(self):
        """ 
        if my cursor fetch empty list, WebsiteNotFoundError should be raised!
        """
        
        START_URL = "https://google.com"
        my_cursor.execute(f"SELECT url_value from url_path where url_value like 'https://{START_URL}%'")
        get_value = my_cursor.fetchall()
        if get_value == False:
            self.assertRaises(WebsiteNotFoundError,msg=f"URL with start_value = {START_URL} does not exist!")
        
    def test_web_not_exists_case2(self):
        """ 
         if end_url not exists, WebsiteNotFoundError should be raised!!
        """
        url = "https://kodius.com"
        parsed_url = split_function(url) #
        START_URL  = parsed_url[0] 
        END_URL    = parsed_url[-1] 
        self.assertEqual(START_URL,"kodius.com")
        if END_URL == False:
            self.assertRaises(WebsiteNotFoundError)


if __name__ == "__main__":
    unittest.main()
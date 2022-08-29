from custom_database import split_function
import unittest



class TestShortestPath(unittest.TestCase):
    
    def setUp(self):
        self.name = self.shortDescription()
        print(f"Test: {self.name}")
        
    def tearDown(self):
        print("End!")
    
    @classmethod
    def tearDownClass(cls):
        print("All tests finished!")
    
    @classmethod
    def setUpClass(cls):
        print("START") 
    
    def test_split_function(self):
        """
        this function return list of elements without https: and /
        """
        testing_url_kodius_1DEPTH = "https://kodius.com/"
        testing_url_kodius_2DEPTH = "https://kodius.com/blog/"
        testing_url_kodius_3DEPTH = "https://kodius.com/blog/kodius-top-7-percent-at-pangea"

        self.assertEqual(split_function(testing_url_kodius_1DEPTH),["kodius.com"])
        self.assertEqual(split_function(testing_url_kodius_2DEPTH),["kodius.com","blog"])
        self.assertEqual(split_function(testing_url_kodius_3DEPTH),["kodius.com","blog","kodius-top-7-percent-at-pangea"])
    
    def test_start_end(self):
        """ 
        in order for the action to be executed successfully, 
        we need to check that start_url and end_url accept the correct values
        """
        url = "https://kodius.com/blog/kodius-top-7-percent-at-pangea"
        parsed_url = split_function(url) #
        START_URL  = parsed_url[0] 
        END_URL    = parsed_url[-1] 
        self.assertEqual(START_URL,"kodius.com")
        self.assertEqual(END_URL,"kodius-top-7-percent-at-pangea")
    
    @unittest.expectedFailure
    def test_start_end_fail(self):
        """
        it is necessary to check if END_URL_ exists!
        """
        url = "https://kodius.com"
        parsed_url = split_function(url) #
        START_URL  = parsed_url[0] 
        END_URL    = parsed_url[-1] 
        self.assertEqual(START_URL,"kodius.com")
        self.assertTrue(END_URL,True)
        


        
if __name__ == "__main__":
    unittest.main()
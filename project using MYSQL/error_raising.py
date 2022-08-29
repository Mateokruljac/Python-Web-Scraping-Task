#create WebsiteNotExistError
class WebsiteNotFoundError(Exception):
    """ 
    Error occurs if START_URL does not exist or  if START_URL or END_URL doesnt exist in sqlite database
    Attributes:
         message: -> explanation of error (Does Not Exist!)
    """
    def __init__(self,message = "Website does not exist!"):
        self.message = message 
        super().__init__(message)


#create ShortestPathNotFoundError
class ShortestPathNotFoundError(Exception):
    """ 
    Error ocurrs if there is no path between START_URL and END_URL
    Attributes:
         message : -> expalnation of error (The Shortest path not found!)
    """
  
    def __init__(self,message  = "The Shortest path does not exist!"):
        self.message = message 
        super().__init__(message)
        
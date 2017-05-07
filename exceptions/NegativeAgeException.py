class NegativeAgeException(Exception):
    def __init__(self,error):
        Exception.__init__(self, error)

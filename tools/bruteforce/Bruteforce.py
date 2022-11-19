import requests

class Bruteforce():
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def start(self):
        url = self.url
        username = self.username
        password = self.password

        #checking username file or not
        try:    
            if ".txt" in username:
                pass
            elif "/" in username:
                pass
            else:
                pass
        except:
            pass


        def checking_dir(isUserName=False,isPassword=False):
            pass

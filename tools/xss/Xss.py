from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from rich import print
import os,datetime

class Xss():
    def __init__(self,url,wordlist):
        self.url = url
        self.wordlist = wordlist
        self.path = os.path.dirname(os.path.realpath(__file__))# current project path

    def start(self):
        url = self.url
        wordlist = self.wordlist
        path = self.path
        #Setting Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-xss-auditor')
        options.add_argument('--disable-web-security')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options)
        
        #checking file 
        try:
            if wordlist:
                payload = open(wordlist,'r').readlines()
            else:
                path = self.path+"/payloads.txt"
                payload = open(path,'r').readlines()
        except:
            print("[bold red][!] Error : Failed to read specified file check the file name is correct[/bold red]")


        try:

            print("\n\t[bold yellow]STARTING TIME :%s [/bold yellow]"%str(datetime.datetime.now()))
            print("\t[bold yellow]GENERATED WORDS:%s [/bold yellow]"%str(len(payload)))
            print("\t[bold yellow]BASE URL :%s [/bold yellow]"%url)
            print("\t[bold yellow]PAYLOAD FILES :%s [/bold yellow]"%path)
            print("\n\n")

            print("[bold blue]-----[ SCANNING URL : %s ]-----[/bold blue]"%url)

            #checking directory in given url  
            for payloadLine in payload:
                payloadLine = payloadLine.strip('\n')
                print('{payloadLine}',payloadLine) 


        except UnicodeDecodeError:
            print("[bold red][!] Error : Invalid continuation byte[/bold red]")
        except UnboundLocalError:
            print("[bold red][!] Error : Referenced before assignment[/bold red]")
        except KeyboardInterrupt:
            pass
        except TimeoutException:
            print("[bold red][!] Error : XSS doesn't work with [/bold red]"+payloadLine)
        # except:
        #     print("[bold red][!] Error : Something went wrong[/bold red]")
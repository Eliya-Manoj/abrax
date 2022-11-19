import os,sys
import time
import requests
import threading
from rich import print,progress
import datetime


rhost = 'https://null-byte.wonderhowto.com/'
class Direcory_Scanner():
    def __init__(self,url,saveOutPut=False,wordList=False):
        self.url = url
        self.saveOutPut = saveOutPut
        self.wordList = wordList
        self.path = path = os.path.dirname(os.path.realpath(__file__))# current project path

    def checking_dir(self):
        if self.url and self.saveOutPut and self.wordList:
            #url, save result file and custom word list
            print('url, saveoutput and word list file')
        elif self.url and self.saveOutPut:
            #url and save result file 
            self.wordlist_gen(True)
        elif self.url and self.wordList:
            #url and word list 
            self.wordlist_gen(False,True)
        else:
            # url only 
            self.wordlist_gen()

    def wordlist_gen(self,output=False,cWordlist=False):
        url = str(self.url).strip("/")
        #checking default list or custom list

        try:
            if cWordlist:
                path = self.wordList
                file = open(path,'r')
                lines = file.readlines()
            else:
                path = self.path+"/common.txt"
                file = open(path,'r')
                lines = file.readlines()
                
        except:
            print("[bold red][!] Error : Failed to read specified file check the file name is correct[/bold red]")

        try:

            print("\n\t[bold yellow]STARTING TIME :%s [/bold yellow]"%str(datetime.datetime.now()))
            print("\t[bold yellow]GENERATED WORDS:%s [/bold yellow]"%str(len(lines)))
            print("\t[bold yellow]BASE URL :%s [/bold yellow]"%url)
            print("\t[bold yellow]WORDLIST FILES :%s [/bold yellow]"%path)
            print("\n\n")

            print("[bold blue]-----[ SCANNING URL : %s ]-----[/bold blue]"%url)
            #checking directory in given url  

            for line in lines:
                line = line.strip("\n")
                response = requests.get(url+"/"+line)
                if response.status_code != 404:
                    print("[bold green][*] Founded : "+url+"/"+line+" [/bold green]")

                print("[bold blue]--> [/bold blue]"+url+"/"+line, end="\r")
                       

        except UnicodeDecodeError:
            print("[bold red][!] Error : Invalid continuation byte[/bold red]")
        except UnboundLocalError:
            print("[bold red][!] Error : Referenced before assignment[/bold red]")
        except KeyboardInterrupt:
            pass
        except:
            if "https" in url:
                print("[bold red][!] Error : Something went wrong[/bold red]")
            elif "http" in url:
                print("[bold red][!] Error : Something went wrong[/bold red]")
            else:
                print("[bold red][!] Error : Please Enter proper url[/bold red]")
                



            

import os
import whois
import datetime
from rich import print

class Whois:
    def __init__(self,url,o):
        self.url = url
        self.outputLocation = o

    def start(self):
        url = self.url
        outputLocation = self.outputLocation

        if ".com" in url:
            response = whois.whois(url)
            response.expiration_date  # dates converted to datetime object
            creation_date =response['creation_date']
            try:
                indexing = list(response)
                for index in indexing:    
                    if 'creation_date' in index:
                        print("[bold blue][*] "+str(index)+"[/bold blue][bold red] : [/bold red][bold green]"+str(creation_date[0])+"[/bold green]")
                    else:
                        print("[bold blue][*] "+str(index)+"[/bold blue][bold red] : [/bold red][bold green]"+str(response[index])+"[/bold green]")

            except KeyError:
                print("[bold red][!] Error : Key Error[/bold red]")
            except:
                print("[bold red][!] Error : Something went wrong[/bold red]")
        else:
            print("[bold red][!] Error : Please Enter Proper Url[/bold red]")

            
        
        

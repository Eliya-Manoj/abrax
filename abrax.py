#!/usr/bin/python
import typer

#importing packages
from tools.directoryScanner.Directory_Scanner import Direcory_Scanner
from tools.bruteforce.Bruteforce import Bruteforce
from tools.whois.Whois import Whois
from tools.xss.Xss import Xss
from tools.subDomain.SubDomain import SubDomain
from tools.dataExposure.DataExposure import DataExposure
from tools.dnsEnum.DnsEnum import DnsEnum
from tools.wappalyzer.Wappalyz import Wappalyz
#  ______     ______     ______     ______     __  __
# /\  __ \   /\  == \   /\  == \   /\  __ \   /\_\_\_\
# \ \  __ \  \ \  __<   \ \  __<   \ \  __ \  \/_/\_\/_
#  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\ \_\   /\_\/\_\
#   \/_/\/_/   \/_____/   \/_/ /_/   \/_/\/_/   \/_/\/_/
#

app = typer.Typer()

#=============[ data sxposure ]================
@app.command()
def data_exposure(u:str = typer.Option(...,help='url',show_default=False)):
    """
    sdfhsdjkfhsjkdfh
    """
    DataExposure(u).start()

#=============[ xxe ]================
@app.command()
def xxe():
    pass 

#=============[ security misconfig ]================
@app.command()
def security_misconfiguration():
    pass

#=============[ xss ]================
@app.command()
def xss(u:str = typer.Option(..., help="url",show_default=False),
    w:str = typer.Option('', help='wordlist',show_default=False)):
    """
    Example : ./abrax.py xss --u http://example.com --w wordlist.txt
    """
    Xss(u,w).start()   

#
# Basic Enum
#
#=============[ directory scanner ]================
@app.command(rich_help_panel="Basic Enum")
def directory_scanner(u: str = typer.Option(..., help='Specify the url you want to check', show_default=False),
    o: str = typer.Option("", help='Save Output To Disk', show_default=False),
    w: str = typer.Option("", help='Custom Wordlist', show_default=False)):
    """
    Example : ./abrax.py bruteforce --u http://example.com
    """
    Direcory_Scanner(u,o,w).checking_dir()

#=============[ sub domain enum ]================
@app.command(rich_help_panel="Basic Enum")
def sub_domain(d:str = typer.Option(..., help="Specify the domain name you want to check")):
    """
    Example ./abrax.py sub-domain --d example.com
    """
    SubDomain(d).start()

#=============[ dns enum ]================
@app.command(rich_help_panel="Basic Enum")
def dns_enum(d:str = typer.Option(..., help="Specify the domain name you want to Check", show_default=False)):
    """
    Example ./abrax.py dns-enum --d domain_name
    """
    DnsEnum(d).start()

#=============[ wp scanner ]================
@app.command(rich_help_panel="Basic Enum")
def wp_scanner ():
    pass  

#=============[ network scanner ]================
@app.command(rich_help_panel="Basic Enum")
def network_scanner():
    pass 

#=============[ whois ]================
@app.command(rich_help_panel="Basic Enum")
def whois(u:str=typer.Option(...,help="Specify the url you want to check",show_default=False),
    o:str =typer.Option("", help='Save output to disk',show_default=False)):
    """
    Example ./abrax.py whois --u https://example.com
    """
    Whois(u,o).start()

#=============[ bruteforce ]================
@app.command(rich_help_panel="Basic Enum")
def bruteforce(u:str = typer.Option(..., help="URL",show_default=False),
    l:str = typer.Option(..., help="Login with LOGIN name, or load several logins from FILE", show_default=False),
    p:str = typer.Option(..., help="Password PASS, or load several passwords from FILE",show_default=False)):
    """
    Example : ./abrax.py bruteforce --u http://example.com/login --l admin --p passwordlist.txt
    """
    Bruteforce(u,l,p).start()
#
# Injections
#
#=============[ sql-injection ]================
@app.command(rich_help_panel="Injections")
def sql_injection():
    pass

#=============[ host header ]================
@app.command(rich_help_panel="Injections")
def host_header():
    pass

#
# Technologies used
#
#=============[ wappalyzer ]================
@app.command(rich_help_panel="Technology")
def wappalyzer(u:str = typer.Option(...,help="Specify the url you want to check", show_default=False)):
    Wappalyz(u).start()

#
# Privilege escalation
#
#=============[ broken access control ]================
@app.command(rich_help_panel="Privilage Escalation")
def broken_access_control():
    pass

#=============[ broken auth ]================
@app.command(rich_help_panel="Privilage Escalation")
def broken_auth():
    print("hello")


if __name__ == "__main__":
    app()

from dns import resolver
from rich import print,console
class DnsEnum():
    def __init__(self,domain):
        self.domain = domain

    def start(self):
        consoles = console.Console()
        domain = self.domain
        record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
        for record in record_types:
            try:
                response = resolver.resolve(domain, record)
                consoles.log(f'[bold blue]{record} Records')
                print('-' * 50)
                for server in response:
                    consoles.log(f'[bold blue]{server.to_text()} Records')

            except resolver.NoAnswer:
                consoles.log('[bold yellow] Time Out [/bold yellow]')

            except resolver.NXDOMAIN:
                consoles.log(f'[bold red]{domain} does not exist[/bold red]')

            except KeyboardInterrupt:
                exit()
            except resolver.LifetimeTimeout:
                print("[bold red][!] Error : DNS operation timed out[/bold red]")

            except:
               print("[bold red][!] Error : Something went wrong[/bold red]")
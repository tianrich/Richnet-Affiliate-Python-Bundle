import requests
from bs4 import BeautifulSoup

def check_redirects(url):
    try:
        r = requests.get(url, allow_redirects=False)
        if r.status_code in [301, 302]:
            soup = BeautifulSoup(r.content, 'html.parser')
            print(f"{url} redirects to {r.headers['Location']}")
            print("Do you want to copy the final url? Press y for Yes and n for no")
            choice = input()
            if choice == 'y':
                import pyperclip
                pyperclip.copy(r.headers['Location'])
                print("The final url has been copied to clipboard.")
            check_redirects(r.headers['Location'])
        else:
            print(f"{url} does not redirect.")
    except Exception as e:
        print(e)

while True:
    print("Enter the url:")
    url = input()
    check_redirects(url)

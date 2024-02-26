import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url=input("Enter a URL: ")

if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)

    print(f"Website headers are {url} \n, {response.headers} \n\n")

    server=response.headers.get("Server")

    if server:
        print(f"The server is {server}")
    else:
        print("No server found")

    cookies = response.headers.get("Set-Cookie")

    if cookies:
        cookies=cookies.split(';')
        for cookie in cookies:
            print(f"The cookie is {cookie}")
    else:
        print("No cookie found")
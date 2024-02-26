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

#zitaei aitima apo ton xristi
url=input("Enter a URL: ") 

#http aitima
if not url.startswith("http://"):
    url = "http://" + url

#pragmatopoiei aitima get se afto to url http
with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)

    #tupwnei headers apokrisis response http
    print("\nRESPONSE HEADER")
    for key, value in response.headers.items():
        print(f"{key:30s} {value}")

    #(a) poio logismiko xrisimopoiei o web server
    server=response.headers.get("Server")

    if server:
        print(f"The server is {server}")
    else:
        print("No server found")

    #(b) an xrisimopoiei cookies
    cookies = response.headers.get("Set-Cookie")

    if cookies:
        print(f"The webpage is using cookies")
        cookies=cookies.split(';')
        for cookie in cookies:
            #(c) onoma ka8e cookie kai expiration date se opoio exei
            print(f"The cookie is {cookie}")
    else:
        print("No cookie found")
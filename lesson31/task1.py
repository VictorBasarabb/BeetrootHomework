import requests


urls = {
    "Wikipedia": "https://en.wikipedia.org",
    "Twitter": "https://twitter.com",
}


def download_robots_txt(url, filename):
        response = requests.get(url + "/robots.txt")
        with open(filename, "wb") as f:
            f.write(response.content)


for name, url in urls.items():
    download_robots_txt(url, f'{name.lower()}_robots.txt')








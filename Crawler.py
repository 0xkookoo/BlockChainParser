#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import os.path

# This part is for the initialization of the crawler parameters
# N = int(sys.argv[1])  # This is the the limit on the number of pages to retrieve
directory = 'download'  # This is the directory name where the download .bin files are
URL_BASE = 'https://webbtc.com/block/'

# Defining Agent Name for the crawler
AGENT_NAME = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
if not os.path.isdir(directory):  # To Check if Directory exists
    os.mkdir(directory)  # if it doesnt then make it

os.chdir(directory)  # then change directory to that folder


# This function is to define how to handle the http status code.
def handle_http_status_code(status_code):
    success_http_status_code = [200, 304]  # this stores the http_status_code representing current request is good
    broken_http_status_code = [404, 500]  # this stores the http_status_code representing current page is broken
    stop_http_status_code = [401, 403, 503,
                             504]  # this stores the http_status_code representing we need to stop request
    redirect_http_status_code = [301, 302]  # this stores the http_status_code representing redirect to another page
    download_allowed = 0
    if status_code in success_http_status_code:
        download_allowed = 0
    if status_code in broken_http_status_code:
        download_allowed = 1
    if status_code in stop_http_status_code:
        download_allowed = 2
    if status_code in redirect_http_status_code:
        download_allowed = 3

    return download_allowed


# This function is to define how to handle the response of given URL
def handle_response_status_code(input_url):
    try:
        source_code = requests.get(input_url.rstrip(), headers={'User-Agent': AGENT_NAME},
                                   allow_redirects=False)  # Get source code for given URL with User-Agent and Host defined
        print(source_code)
        status_code = handle_http_status_code(source_code.status_code)  # Get response http status code

        # To handle 301 Response Code
        if status_code == 3:
            redirected_location = source_code.headers['Location']
            print("There is a Redirect Response Code")
            return redirected_location

        # To handle 401/403/5xx Response Code
        if status_code == 2:
            print("The WebServer sent me a 401/403/5xx Response Code So I am Stopping the crawler")
            # sys.exit()

        # To handle 404/500 Response Code
        if status_code == 1:
            print("The Page is Broken")

        # To handle 2xx Response Code
        if status_code == 0:
            html = source_code.text  # get source code of page
            soup = BeautifulSoup(html, 'html.parser')  # variable to call beautifulsoup(variable of the source code)
            return [html, soup]
    except:
        print(input_url)


def get_filename(relative_path):  # get the filename from download_url
    if '/' in relative_path:
        filename = relative_path.split('/')[-1].split('.')[0] + '.bin'
        return filename
    else:
        return relative_path.split('.')[0] + '.bin'


def crawler(hash):
    try:
        html, soup = handle_response_status_code(URL_BASE + hash)
        print(soup.table('tr')[-1]('td')[-1]('a')[-1]['href'])
        download_url = URL_BASE[:-6] + soup.table('tr')[-1]('td')[-1]('a')[-1]['href']
        r = requests.get(download_url, allow_redirects=True)
        filename = get_filename(download_url)
        open(filename, 'wb').write(r.content)
        with open(filename, "rb") as f:
            data = f.read()
        f.close()
        return 'hash valid'
    except:
        reminder = 'You may check if your hash is invalid, or the internet is disconnected.'
        print(hash + '.bin file retrieved failed!' + '!' * 20)
        print(reminder)
        if len(hash) < 64:
            return 'Your hash is shorter than 64'
        elif len(hash) > 64:
            return 'Your hash is longer than 64'
        else:
            print('sssssssssssssssssssss')
            status = handle_http_status_code(
                requests.get((URL_BASE + hash).rstrip(), headers={'User-Agent': AGENT_NAME},
                             allow_redirects=False).status_code)
            print('status   ', status)
            if status == 1:
                return 'invalid hash, 404'
            elif status == 2:
                return '401/403/5xx Response'

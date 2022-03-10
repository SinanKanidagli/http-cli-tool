import requests

from httpy.output.colors import Colors
from httpy.output.lexers import print_html, print_json


def print_status(res: requests.Response):
    print(
        f"{Colors.RED}{Colors.BOLD}HTTP/1.1{Colors.ENDC}{Colors.CYAN} {res.status_code} {res.reason}"
    )


def print_headers(res: requests.Response):
    for header in res.headers.items():
        print(f"{Colors.CYAN}{header[0]} : {Colors.ENDC}{header[1]}")
    print()


def print_body(res: requests.Response):
    json_content_type = "application/json"
    html_content_type = "text/html"

    content_type = res.headers["content-type"]

    if content_type.startswith(json_content_type):
        print_json(res)
    elif content_type.startswith(html_content_type):
        print_html(res)

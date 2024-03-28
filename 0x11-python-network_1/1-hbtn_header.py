#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a request to the URL
    req = urllib.request.Request(url)

    # Open the URL using a with statement to ensure the connection is closed properly
    with urllib.request.urlopen(req) as response:
        # Retrieve the value of the X-Request-Id variable from the header
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


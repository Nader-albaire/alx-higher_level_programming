#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode email parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')  # Data should be bytes

    # Send a POST request to the URL with the email parameter
    req = urllib.request.Request(url, data=data, method='POST')

    # Open the URL using a with statement to ensure the connection is closed properly
    with urllib.request.urlopen(req) as response:
        # Decode and print the body of the response
        print(response.read().decode('utf-8'))

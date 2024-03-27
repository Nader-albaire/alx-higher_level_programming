#!/bin/bash

# This script makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with a message containing "You got me!"

# Send a PUT request with custom data to trigger the desired response
curl -s -X PUT --data "user_id=98" 0.0.0.0:5000/catch_me


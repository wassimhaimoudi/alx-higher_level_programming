#!/bin/bash
# This script sends a `POST` request to the specified url and returns the body of the response
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%PLD" "$1"

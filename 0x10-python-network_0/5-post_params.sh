#!/bin/bash
# This script sends a `POST` request to the specified url and returns the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

#!/bin/bash
# This script shows the allowed HTTP methods I can use to make a request to the specified server in the url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

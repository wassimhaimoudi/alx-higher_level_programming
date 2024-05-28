#!/bin/bash
# This script sends a request to a url and displays displays the status code of the response
curl -sI "$1" | head -n 1 | cut -d " " -f 2

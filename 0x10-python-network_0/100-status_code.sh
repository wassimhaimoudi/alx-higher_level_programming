#!/bin/bash
# This script sends a request to a url and displays displays the status code of the response
sudo curl -so /dev/null -w "%{http_code}" "$1"

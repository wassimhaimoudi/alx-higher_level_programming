#!/usr/bin/bash
# This script sends a delete request to the destination url and displays the body of the response
curl -s -X DELETE "$1"

#!/bin/bash
# This script takes in a url as an argument and displays the requested body in response. A header varible `X-School-User-Id` must be sent with the value `98`
curl -s -H "X-School-User-Id: 98" "$1"

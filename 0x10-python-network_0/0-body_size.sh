#!/bin/bash
# This script takes a url as a command line argument and displays its body's content size
curl -s "$1" | wc -b

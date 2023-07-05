#!/bin/bash
# Bash script displays size of the body of a response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

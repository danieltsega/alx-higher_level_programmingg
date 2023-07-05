#!/bin/bash
#  Bash script displays only the status code of the response
curl -sL -w "%{http_code}" "$1" -o /dev/null

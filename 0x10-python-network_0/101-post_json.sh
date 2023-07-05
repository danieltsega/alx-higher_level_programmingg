#!/bin/bash
# Bash script that sends a JSON POST and displays the body of the response
if [ -f "$2" ]; then curl -sL -X POST -H "Content-Type: application/json" -d @"$2" "$1"; else echo "File not found"; fi

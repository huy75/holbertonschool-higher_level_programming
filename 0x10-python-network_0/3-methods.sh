#!/bin/bash
#Print options allowed in headers
curl -sI "$1" | grep "Allow:" | cut -d ":" -f 2-

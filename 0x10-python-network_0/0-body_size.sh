#!/bin/bash
# takes in server ip and outputs content-length
curl -sI "$1" | grep Content-Length | cut -d " " -f2

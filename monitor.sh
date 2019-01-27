#!/bin/sh
inotifywait -m $0 -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        bash ./ai-api/runner.sh
    done
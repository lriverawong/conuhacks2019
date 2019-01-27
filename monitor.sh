#!/bin/sh
inotifywait -m ~/image-bank -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        bash ~/conuhacks2019/ai-api/runner.sh
    done

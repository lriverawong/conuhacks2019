#!/bin/sh
inotifywait -m /home/hacker/image-bank -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        bash /home/hacker/conuhacks2019/ai-api/runner.sh
    done

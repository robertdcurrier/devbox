#!/bin/bash
docker exec -e COLUMNS="`tput cols`" -e LINES="`tput lines`" -ti devbox_tools_1 /bin/bash

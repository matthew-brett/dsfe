#!/bin/bash
# Kill Jekyll server
jekyll_pid=$(ps aux | grep '[j]ekyll' | awk '{print $2}')
if [ -n "${jekyll_pid}" ]; then
    kill ${jekyll_pid}
fi

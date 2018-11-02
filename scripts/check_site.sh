#!/bin/bash
# Final check for local server build
res=$(grep -r localhost:4000 --include "*.html" _site)
if [ -n "$res" ]; then
    echo "localhost:4000 in _site"
    exit 1
fi

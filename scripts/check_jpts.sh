#!/bin/bash
# Check Jupytext format strings
res=$(grep -Er '"?jupytext_formats"?: "?Rmd(:rmarkdown)?"?,?$' --include "*.Rmd" --include "*.ipynb" notebooks/*)
if [ -z "$res" ]; then
    echo OK
    exit 0
fi
echo "Dubious notebook files, please check"
printf "$res\n"
exit 1

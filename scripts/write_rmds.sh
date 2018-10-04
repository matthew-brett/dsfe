#!/bin/bash
# Write notebooks from Rmds
for fn in $(find notebooks -name "*.Rmd" | grep --invert .ipynb_checkpoints); do
    jupytext --to notebook ${fn}
done

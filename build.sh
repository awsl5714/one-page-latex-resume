#!/usr/bin/env bash
# Compile every resume variant into build/ and print each PDF's page count.
set -e
mkdir -p build
for m in main-internet main-soe main-ats main-en; do
  echo ">> $m"
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$m.tex" >/dev/null
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$m.tex" >/dev/null
done
echo "Done -> build/*.pdf"

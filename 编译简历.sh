#!/bin/sh
set -eu
cd "$(dirname "$0")"
export TEXMFHOME="$PWD/assets/texmf"
if command -v xelatex >/dev/null 2>&1; then
  engine=xelatex
else
  engine=/Library/TeX/texbin/xelatex
fi
mkdir -p tmp/pdfs
"$engine" -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs 刘元智_简历.tex
"$engine" -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs 刘元智_简历.tex
cp tmp/pdfs/刘元智_简历.pdf 刘元智_简历.pdf

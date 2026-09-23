#!/bin/bash
set -euo pipefail

curl -fSLO https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

sed 's/\t/,/g' cleaned.tsv > converted.csv
cleaned_lines=$(wc -l < cleaned.tsv)
data_lines_count=$((cleaned_lines - 1))
echo "rows of data: $data_lines_count"
tar -czvf converted-archive.tar.gz converted.csv


#!/bin/sh

xgboost train.conf task=pred model_in=$1

paste pred.txt ./format_data/test.txt > ./result_data/validate.txt

python metrics.py

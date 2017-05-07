#!/bin/sh

xgboost train.conf

timestamp=`date +%Y%m%d.%H%M%S`

xgboost train.conf task=dump model_in=0200.model fmap=./result_data/featmap.txt name_dump=./result_data/dump.nice.txt.${timestamp}

#!/bin/sh

python step1_filtering_by_value.py

python step2_extract_features.py
python step3_map_feature.py
sh step4_make_n_fold.sh

sh step5_model_training.sh
sh step6_model_testing.sh 0200.model >> training.log
sh step7_export_model.sh

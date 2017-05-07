# -*- coding: utf-8 -*-
import sys

THRESHOLD = 10

predict_file = './result_data/validate.txt'
badcase_file = './result_data/bad_cases.txt'

correct_count = 0
all_count = 0

with open(badcase_file, "w") as out_file:
    with open(predict_file, "r") as in_file:
        for line in in_file:
            tokens = line.strip().split()
            pred = float(tokens[0])
            real = float(tokens[1])
            count = int(tokens[2])

            all_count += 1
            all_sum += count

            gap = abs(pred - real)

            if gap < THRESHOLD:
                correct_count += 1
                correct_sum += count
            if gap < THRESHOLD*2:
                correct_double_count += 1
                correct_double_sum += count

print "ALL=%d CORRECT=%d PRECISION=%f" % (all_count, correct_count, correct_count * 100.0 / all_count)

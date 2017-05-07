import math

# TODO: config file for common parameters

def filtering(origin_file_path, result_file_path, is_train=False):
    with open(result_file_path, "w") as out_file:
        with open(origin_file_path) as in_file:
            for line in in_file:
                tokens = line.strip().split()
                value = float(tokens[0])

                if (value > 500 or value < 10): # XXX: filter by value
                    continue

                out_file.write(str(value) + "\t" + " ".join(tokens[1:]) + "\n")

if __name__ == '__main__':
    train_origin_file = "./raw_data/train.txt.origin"
    train_result_file = "./format_data/train.txt"
    test_origin_file = "./raw_data/test.txt.origin"
    test_result_file = "./format_data/test.txt"

    filtering(train_origin_file, train_result_file, True)
    filtering(test_origin_file, test_result_file, False)

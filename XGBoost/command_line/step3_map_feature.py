#!/usr/bin/python

def map_features(fmap, text_file_path, id_file_path, is_train=True):
    with open(id_file_path, 'w') as out_file:
        for l in open(text_file_path):
            arr = l.strip().split()
            value = float(arr[0])

            cnt = int(arr[1])
            if is_train and cnt < 50:
                continue

            out_file.write(str(value))

            for i in xrange(len(arr)-7): # XXX: features start from column 7
                terms = arr[7+i].split(':')

                if len(terms) < 2:
                    continue

                if not terms[0] in fmap:
                    continue

                out_file.write( ' %d:%s' % (fmap[terms[0]], terms[1]) )

            out_file.write('\n')

if __name__ == '__main__':
    fmap = {}
    with open('./result_data/featmap.txt') as in_file:
        for line in in_file:
            tokens = line.strip().split()
            fmap[ tokens[1] ] = int(tokens[0])

    train_text_file_path = './format_data/train.txt'
    train_id_file_path = './format_data/train.libsvm'
    test_text_file_path = './format_data/test.txt'
    test_id_file_path = './format_data/test.libsvm'

    map_features(fmap, train_text_file_path, train_id_file_path, True)
    map_features(fmap, test_text_file_path, test_id_file_path, False)

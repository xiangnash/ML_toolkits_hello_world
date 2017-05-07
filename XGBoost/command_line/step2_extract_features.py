#!/usr/bin/python

cnt = 0
fmap = {}
for line in open('./format_data/train.txt'):
    tokens = line.split()

    i = 0
    for token in tokens:
        i += 1
        if i <= 8:
            continue

        #if not token.startswith('int#xxx'): # XXX: feature filtering
        #    continue

        if not (token.startswith('i') or token.startswith('f')):
            continue

        term = token.split(':')

        if len(term) < 2:
            continue

        if term[0] not in fmap:
            fmap[ term[0] ] = cnt
            cnt += 1

# create feature map for machine data
with open('./result_data/featmap.txt', 'w') as out_file:
    for v, k in sorted( fmap.items(), key = lambda x:x[1] ):
        #print k, v
        type = v.split("#")[0]
        out_file.write( '%d\t%s\t%s\n' % (k, v, type))

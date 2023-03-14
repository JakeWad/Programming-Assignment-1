import itertools

data = {'1':['x', 'y', 'z'], '2':['s', 't']}

combinations = list(itertools.product(*[data[k] for k in sorted(data.keys())]))

for c in combinations:
    print(''.join(c))

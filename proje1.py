l = [[1,[2,4],3],"a",[5,6]]
flatten_l = []

def flatten(x):
    for i in x:
        if isinstance(i, list):
            flatten(i)
        else:
            flatten_l.append(i)

    return flatten_l

print(flatten(l))

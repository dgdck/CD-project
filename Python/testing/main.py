def main():
    print(
        flatten_dict({'a': [{'inner_inner_a': 42}]})
        )
    print(flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))


def get_none():
    return None


def flatten_dict(input):
    list_flatten = []
    for x in input:
        if isinstance(input[x], dict):
            list_flatten.append(flatten_dict(input[x]))
        elif isinstance(input[x], list):
            for z in input[x]:
                list_flatten.append(flatten_dict(z))
        else:
            list_flatten.append(input[x])
    list_final = []
    for sublist in list_flatten:
        if isinstance(sublist, list):
            for var in sublist:
                list_final.append(var)
        else:
            list_final.append(sublist)
    return list_final


if __name__ == '__main__':
    main()

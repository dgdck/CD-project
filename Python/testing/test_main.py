# import from main

from main import get_none
from main import flatten_dict


def main():
    print(
        test_flatten_dict()
    )


# tests

def test_get_none():
    assert get_none() is None


def test_flatten_dict():
    assert type(flatten_dict({
        'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14
        })) == list


if __name__ == '__main__':
    main()

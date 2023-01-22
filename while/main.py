from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# 1


def unique_koala_facts(x):
    unique_koala_facts_list = []
    count = 0
    while x > 0 and count < 1000:
        fact = random_koala_fact()
        if fact not in unique_koala_facts_list:
            unique_koala_facts_list.append(fact)
            x -= 1
        count += 1
    return unique_koala_facts_list

# 2


def num_joey_facts():
    joey_list = []
    list_duplicate = []
    duplicate = 0
    while duplicate < 100:
        fact = random_koala_fact()
        if fact not in list_duplicate:
            list_duplicate.append(fact)
            if 'joey' in fact.lower() or 'joeys' in fact.lower():
                joey_list.append(fact)
        if fact in list_duplicate:
            duplicate += 1
    return int(len(joey_list))

# 3


def koala_weight():
    i = 0
    while i <= 1000:
        fact = random_koala_fact()
        if 'kg' in fact:
            return int(fact[fact.find('kg') - 2:fact.find('kg')])
        i += 1

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.


if __name__ == "__main__":
    print(random_koala_fact())
    x = 50
    print(unique_koala_facts(x))
    fact = random_koala_fact()
    print(num_joey_facts())
    print(koala_weight())

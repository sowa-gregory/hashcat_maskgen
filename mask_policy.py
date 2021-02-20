'''
The complete alphabet is always used. The reason is to always generate masks containing all alphabet
symbols, which allows for incremental masks usage.
Example:
If cracking password with masks assuming at least three digits fails, new differential masks can
be generated for passwords with at least two digits substracting previous masks sets.
'''
from itertools import product

# possible chars in each symbol
ALPHABET = "slud"
SYMBOLS = {'s': 33, 'u': 26, 'l': 26, 'd': 10}

ALL_CHARS = 95
MAX = 1000


def filter_mask(policy: dict, mask: list):
    symbol_counter = dict.fromkeys(policy, 0)
    for symbol in mask:
        symbol_counter[symbol] += 1

    for symbol in symbol_counter:
        cond = policy[symbol]
        exp_min = cond.get('min', 0)
        exp_max = cond.get('max', MAX)
        counted = symbol_counter[symbol]
        if counted < exp_min or counted > exp_max:
            return False
    return True


def calc_number(cand):
    mul = 1
    for symbol in cand:
        mul *= SYMBOLS[symbol]
    return mul


def gen_masks(pass_len, policy):

    all_masks = product(list(ALPHABET), repeat=pass_len)
    # filter masks
    return set([mask for mask in all_masks if filter_mask(policy, mask)])


def calc_total_iters(masks:set):
    iters=0
    for mask in masks:
        iters+=calc_number(mask)
    return iters

def save_masks(file_name: str, masks: set):
    with open(file_name, "wt") as file:
        for mask in masks:
            file.write("".join(['?'+x for x in mask]))
            file.write("\n")


def print_info(pass_len, masks):
    iters = calc_total_iters(masks)
    print()
    print("total iterations:", iters)
    print("number of masks:", len(masks))
    print("% of total set", iters/pow(ALL_CHARS, pass_len)*100)
    print("estimated time hours:", iters/1420000000/3600)

def gen_single_set(pass_len, policy, file_name):
    masks = gen_masks(pass_len, policy)
    print_info(pass_len, masks)
    save_masks(file_name, masks)

def gen_incremental_set(pass_len, policy1, policy2, file_name):   
    masks1 = gen_masks(pass_len, policy1)
    masks2 = gen_masks(pass_len, policy2)
    out_masks = masks2-masks1
    print_info(pass_len, out_masks)
    save_masks(file_name, out_masks)

def test1():
    policy = {'u': {'min': 0, 'max': 8}, 'l': {'min': 3, 'max': 8},
               'd': {'min': 1, 'max': 4}, 's': {'min': 0, 'max': 2}}
    #policy = {'u': {'min': 0, 'max': 8}, 'l': {'min': 0, 'max': 8},
     #          'd': {'min': 0, 'max': 8}, 's': {'min': 0, 'max': 8}}

    pass_len = 8
    gen_single_set(pass_len,policy, "out1")

def test2():
    policy = {'u': {'min': 0, 'max': 8}, 'l': {'min': 1, 'max': 8},
               'd': {'min': 1, 'max': 4}, 's': {'min': 0, 'max': 2}}
    pass_len = 8
    gen_single_set(pass_len,policy, "out2")

def test3():
    policy1 = {'u': {'min': 0, 'max': 8}, 'l': {'min': 3, 'max': 8},
               'd': {'min': 1, 'max': 4}, 's': {'min': 0, 'max': 2}}

    policy2 = {'u': {'min': 0, 'max': 8}, 'l': {'min': 1, 'max': 8},
               'd': {'min': 1, 'max': 4}, 's': {'min': 0, 'max': 2}}
    pass_len = 8
    gen_incremental_set(pass_len, policy1, policy2, "out2")

test1()
test2()
test3()
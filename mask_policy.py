'''
The complete alphabet is always used. The reason is to always generate masks containing all alphabet
symbols, which allows for incremental masks usage.
Example:
If cracking password with masks assuming at least three digits fails, new differential masks can
be generated for passwords with at least two digits substracting previous masks sets.
'''
from itertools import product

# possible chars in each symbol
ALPHABET = "suld"
SYMBOLS = {'s': 33, 'u': 26, 'l': 26, 'd': 10}

ALL_CHARS = 95
MAX = 1000

def filter_mask(policy:dict, mask: list):
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


def main():
    policy = {'u': {'min': 0, 'max': 8}, 'l': {'min': 0, 'max': 8},
            'd': {'min': 0, 'max': 8}, 's': {'min': 0, 'max': 8}}

    pass_len = 8
    all_masks = product(list(ALPHABET), repeat=pass_len)

    cnt = reps = 0

    # filter masks
    fit_masks = [mask for mask in all_masks if filter_mask(policy, mask)]

    for mask in fit_masks:
        repeats += calc_number(cand)
        counter += 1

    print("masks:", counter)
    print()
    print(repeats)
    print(repeats/pow(ALL_CHARS, pass_len))


main()

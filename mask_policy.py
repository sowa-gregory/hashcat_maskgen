import itertools

alphabet = ""


symbols = {'~': 0, 's': 33, 'u': 26, 'l': 26, 'd': 10}

policy = {'u': {'min': 0, 'max':0}, 'l': {'min': 0, 'max':2}, 'd': {'min': 1, 'max':6}, 's': {'min': 0}}
ALL_CHARS = 95
MAX = 1000

# detect used symbols - calculate value of 'other' symbol
def scan_policy():
    global alphabet
    other_symbol_chars = ALL_CHARS
    for sym in policy:
        if policy[sym]['min'] > 0 or ('max' in policy[sym] and policy[sym]['max'] > 0):
            other_symbol_chars -= symbols[sym]
            alphabet += sym
    if other_symbol_chars > 0:
        alphabet += "~"
        symbols['~']=other_symbol_chars
    print("symbols", alphabet)
    print("other symbol", other_symbol_chars)


def check_conf(data):
    count = dict.fromkeys(policy, 0)
    for d in data:
        if d != '~':
            count[d] += 1
    for key in count:
        cond = policy[key]
        expected_min = 0
        expected_max = MAX
        if 'min' in cond:
            expected_min = cond['min']
        if 'max' in cond:
            expected_max = cond['max']

        counted = count[key]
        if counted < expected_min or counted>expected_max:
            return False
    return True


def calc_number(cand):
    mul = 1
    for symbol in cand:
        mul *= symbols[symbol]
    return mul


scan_policy()
pass_len = 8
all = list(itertools.product(list(alphabet), repeat=pass_len))

counter = 0
repeats = 0
for cand in all:
    res = check_conf(cand)
    if res:
        # print(cand)
        repeats += calc_number(cand)
        counter += 1
print("masks:", counter)
print()
print(repeats)
print(repeats/pow(95, pass_len))

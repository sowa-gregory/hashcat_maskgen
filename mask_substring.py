'''
Script to generate masks which contains specific characters

Problem - obejmujemy scenariusze w ktorych mamy dokladnie po jednym ze znakow w substr

'''

FULL_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
DIGITS = "0123456789"
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def generate_masks(pass_len, substr) -> list:
    current_mask = [-1]*pass_len
    masks = []

    def gen_char(char_num):
        if char_num == len(substr):
            masks.append(current_mask.copy())
            return

        for i in range(pass_len):
            if current_mask[i] == -1:
                current_mask[i] = char_num
                gen_char(char_num+1)
                current_mask[i] = -1
    gen_char(0)
    return masks


def mask_convert(mask: list, substr: str) -> str:
    mask_str = ""
    for val in mask:
        if val == -1:
            mask_str += "?1"
        else:
            mask_str += substr[val]
    return mask_str


def get_iterations(masks: list, neg_alphabet_len: int) -> int:
    iters = 1
    for mask in masks:
        mask_iters = 1
        for val in mask:
            if val == -1:
                mask_iters *= neg_alphabet_len
        iters+=mask_iters
    return iters

def write_masks(file_name:str, charset:str, masks):
    with open(file_name, "wt") as file:
        for element in masks:
            file.write(charset+","+element+"\n")


def generate(file_name:str, pass_len: int, substr: str):
    alphabet_negation = "".join(
        [char for char in FULL_ALPHABET if not char in substr])

    alphabet_chars = len(alphabet_negation)
    print(alphabet_chars)
    #alphabet_negation = alphabet_negation.replace(UPPER, "?u")
    #alphabet_negation = alphabet_negation.replace(LOWER, "?l")
    #alphabet_negation = alphabet_negation.replace(DIGITS, "?d")
    #alphabet_negation = alphabet_negation.replace(SPECIAL, "?s")
    
        
    alphabet_negation = alphabet_negation.replace(",", "\,")
    alphabet_negation = alphabet_negation.replace("?", "??")
    

    masks = generate_masks(pass_len, substr)
    iters = get_iterations(masks, alphabet_chars)
    print("Generated masks:", len(masks))
    print("% iterations:", iters/pow(len(FULL_ALPHABET), pass_len)*100)

    out_masks = [mask_convert(mask, substr) for mask in masks]

    write_masks(file_name, alphabet_negation, out_masks)

generate("substring.mask", 6, "12")

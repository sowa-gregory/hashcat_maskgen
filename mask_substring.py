'''
Script to generate masks which contains specific characters
'''


class GenChar:
    def __init__(self):
        pass

    def generate(self, pass_len, substr) -> list:
        self.pass_len = pass_len
        self.substr = substr
        self.mask = [-1]*pass_len
        self.gen_masks = set()
        self.__gen_char(0)
        return self.gen_masks

    def mask_conv(self, mask):
        mask_str = ""
        for x in mask:
            if x == -1:
                mask_str += "?a"
            else:
                mask_str += self.substr[x]
        return mask_str

    def __gen_char(self, char_num):
        if char_num == len(self.substr):
            self.gen_masks.add(self.mask_conv(self.mask))
            return

        for i in range(self.pass_len):
            if(self.mask[i] == -1):
                self.mask[i] = char_num
                self.__gen_char(char_num+1)
                self.mask[i] = -1


out = (GenChar().generate(8, "12"))
for mask in out:
    print(mask)

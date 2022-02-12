from braille_utils.letters import *

# pinyin_SHENG = {
#     **pinyin_SPE_SHENG,
#     **pinyin_ABG_SHENG,
#     **pinyin_PLN_SHENG,
# }


# pinyin_YUN = {
#     **pinyin_SPE_Y_YUN,
#     **pinyin_SPE_Y_DEL_FST_YUN,
#     **pinyin_SPE_Y_I_TO_O_YUN,
#     **pinyin_SPE_W_YUN,
#     **pinyin_SPE_W_DEL_FST_YUN,
#     **pinyin_SPE_W_FST_TO_E_YUN,
#     **pinyin_SPE_SIG_YUN,
# }

class ParseMachine(object):
    WAIT_FIRST = 0
    WAIT_SECOND = 1
    FINISH = 2

    def __init__(self, braille123: list):
        self.braille123 = braille123
        self.state = ParseMachine.WAIT_FIRST
        self.line = len(braille123)
        self.cur_line = 0
        self.cur_idx = 0

    def get_one(self):
        append_str = ""
        while self.state != ParseMachine.FINISH and self.cur_line < self.line:
            if self.state == ParseMachine.WAIT_FIRST:
                append_str = self.handle_fist()
            elif self.state == ParseMachine.WAIT_SECOND:
                append_str = self.handle_second()
        self.state = ParseMachine.WAIT_FIRST
        if self.cur_line >= self.line:
            return None
        return append_str

    def handle_fist(self) -> str:
        cur_char = self.braille123[self.cur_line][self.cur_idx]
        if cur_char == '0':
            if self.cur_idx + 1 >= len(self.braille123[self.cur_line]):
                self.cur_line += 1
                self.cur_idx = 0
            else:
                self.cur_idx += 1
            return ''
        try:
            next_char = self.braille123[self.cur_line][self.cur_idx + 1]
        except IndexError:
            self.state = ParseMachine.FINISH
            self.cur_line += 1
            self.cur_idx = 0
            return '\n'

        # punctuation handle
        if cur_char in ['5', '56', '4']:
            if self.cur_idx + 2 >= len(self.braille123[self.cur_line]):
                self.cur_line += 1
                self.cur_idx = 0
            else:
                self.cur_idx += 2
            if cur_char == '5':
                self.state = ParseMachine.FINISH
                if next_char == '23':
                    return ".\n"
                elif next_char == '0':
                    return ",\n"
                elif next_char == '3':
                    return "?\n"
                else:
                    return '\n'
            elif cur_char == '56':
                self.state = ParseMachine.FINISH
                if next_char == '2':
                    return "!\n"
                return '\n'
            elif cur_char == '4':
                self.state = ParseMachine.FINISH
                if next_char == '0':
                    return ",\n"
                return '\n'

        # letter handle
        self.cur_idx += 1
        if cur_char in pinyin_SHENG.keys():
            self.state = ParseMachine.WAIT_SECOND
            return ''
        elif cur_char in pinyin_YUN.keys():
            self.state = ParseMachine.WAIT_SECOND
            return ''
        else:
            self.state = ParseMachine.FINISH
            return ''

    def handle_second(self) -> str:
        self.state = ParseMachine.FINISH
        suf = ''
        try:
            prev_char = self.braille123[self.cur_line][self.cur_idx - 1]
            cur_char = self.braille123[self.cur_line][self.cur_idx]
        except IndexError:
            return ''
        finally:
            if self.cur_idx + 1 >= len(self.braille123[self.cur_line]):
                self.cur_line += 1
                self.cur_idx = 0
                suf = '\n'
            else:
                self.cur_idx += 1

        # sign punc handle
        ret = ''
        if cur_char in ['1', '2', '3', '23']:
            if prev_char in pinyin_SPE_SHENG.keys():
                ret = pinyin_SPE_SHENG[prev_char] + 'i'  # eg: zhi
            elif prev_char in pinyin_SPE_Y_YUN.keys():
                ret = 'y' + pinyin_SPE_Y_YUN[prev_char]
            elif prev_char in pinyin_SPE_Y_DEL_FST_YUN.keys():
                ret = 'y' + pinyin_SPE_Y_DEL_FST_YUN[prev_char][1:]
            elif prev_char in pinyin_SPE_Y_I_TO_O_YUN.keys():
                ts = pinyin_SPE_Y_I_TO_O_YUN[prev_char]
                ts[0] = 'o'
                ret = 'y' + ts
            elif prev_char in pinyin_SPE_W_YUN.keys():
                ret = 'w' + pinyin_SPE_W_YUN[prev_char]
            elif prev_char in pinyin_SPE_W_DEL_FST_YUN.keys():
                ret = 'w' + pinyin_SPE_W_DEL_FST_YUN[prev_char][1:]
            elif prev_char in pinyin_SPE_W_FST_TO_E_YUN.keys():
                ts = pinyin_SPE_W_FST_TO_E_YUN[prev_char]
                ts[0] = 'e'
                ret = 'w' + ts
            elif prev_char in pinyin_SPE_SIG_YUN.keys():
                ret = pinyin_SPE_SIG_YUN[prev_char]
            else:
                ret = ''
            return ret + suf

        # compose handle
        elif prev_char in pinyin_SHENG.keys() and \
                cur_char in pinyin_YUN.keys():
            # special pinyin:
            if prev_char in pinyin_ABG_SHENG.keys():
                b1 = cur_char in pinyin_SPE_W_YUN.keys() or \
                     cur_char in pinyin_SPE_W_DEL_FST_YUN.keys() or \
                     cur_char in pinyin_SPE_W_FST_TO_E_YUN.keys() or \
                     cur_char in ['1236', '236', '356', '3456', '246', '235', '2346', '12356', '35', '26']
                if prev_char == '1245':  # g/j
                    if b1:
                        ret = 'g' + pinyin_YUN[cur_char]
                    else:
                        ret = 'j' + pinyin_YUN[cur_char]
                elif prev_char == '13':  # k/q
                    if b1:
                        ret = 'k' + pinyin_YUN[cur_char]
                    else:
                        ret = 'q' + pinyin_YUN[cur_char]
                elif prev_char == '125':  # h/x
                    if b1:
                        ret = 'h' + pinyin_YUN[cur_char]
                    else:
                        ret = 'x' + pinyin_YUN[cur_char]
            else:
                ret = pinyin_SHENG[prev_char] + pinyin_YUN[cur_char]
            return ret + suf
        else:
            return '' + suf


def braille_to_int123(result_dict):
    braille = result_dict['braille']
    braille123 = []
    for b in braille:
        line123 = []
        for ch in b:
            try:
                line123.append(str(braille_to_int123_map[ch]))
            except KeyError:
                pass
        braille123.append(line123)
    return braille123


def parse_results_dict(result_dict, filename):
    braille123 = braille_to_int123(result_dict)
    parse_machine = ParseMachine(braille123)
    pinyin_list = []
    word = parse_machine.get_one()
    while word != None:
        print(word, end=' ')
        pinyin_list.append(word)
        word = parse_machine.get_one()
    # with open(filename + '.txt', 'w') as f:
    #     f.write('\n'.join(pinyin_list))


braille_to_int123_map = {
    '\u2800': 0,
    '\u2801': 1,
    '\u2802': 2,
    '\u2803': 12,
    '\u2804': 3,
    '\u2805': 13,
    '\u2806': 23,
    '\u2807': 123,
    '\u2808': 4,
    '\u2809': 14,
    '\u280a': 24,
    '\u280b': 124,
    '\u280c': 34,
    '\u280d': 134,
    '\u280e': 234,
    '\u280f': 1234,
    '\u2810': 5,
    '\u2811': 15,
    '\u2812': 25,
    '\u2813': 125,
    '\u2814': 35,
    '\u2815': 135,
    '\u2816': 235,
    '\u2817': 1235,
    '\u2818': 45,
    '\u2819': 145,
    '\u281a': 245,
    '\u281b': 1245,
    '\u281c': 345,
    '\u281d': 1345,
    '\u281e': 2345,
    '\u281f': 12345,
    '\u2820': 6,
    '\u2821': 16,
    '\u2822': 26,
    '\u2823': 126,
    '\u2824': 36,
    '\u2825': 136,
    '\u2826': 236,
    '\u2827': 1236,
    '\u2828': 46,
    '\u2829': 146,
    '\u282a': 246,
    '\u282b': 1246,
    '\u282c': 346,
    '\u282d': 1346,
    '\u282e': 2346,
    '\u282f': 12346,
    '\u2830': 56,
    '\u2831': 156,
    '\u2832': 256,
    '\u2833': 1256,
    '\u2834': 356,
    '\u2835': 1356,
    '\u2836': 2356,
    '\u2837': 12356,
    '\u2838': 456,
    '\u2839': 1456,
    '\u283a': 2456,
    '\u283b': 12456,
    '\u283c': 3456,
    '\u283d': 13456,
    '\u283e': 23456,
    '\u283f': 123456,
}

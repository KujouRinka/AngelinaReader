import enum

from braille_utils.letters import *
from braille_utils.label_tools import *


def parse_lines_and_save(lines: list, filename):
    read_lines = []
    for ln in lines:
        each_line = []
        for ch in ln.chars:
            if ch.char.isspace() == False:
                each_line.append(ch.char)
        read_lines.append(each_line)
    print(read_lines)

    # 清洗拼音
    # TODO some logic
    for ln in read_lines:
        for ch in ln:  # 声母
            if ch in pinyin_SHENG:
                pass
            else:  # 韵母
                pass


class ParseMachine(object):

    OPEN = 1


    def __init__(self, braille123: list):
        self.braille123 = braille123


    def get_one(self) -> str:
        pass


def braille_to_int123(result_dict):
    braille = result_dict['braille']
    braille123 = []
    for b in braille:
        line123 = []
        for ch in b:
            try:
                line123.append(braille_to_int123_map[ch])
            except KeyError:
                pass
        braille123.append(str(line123))
    return braille123


def parse_results_dict(result_dict, filename):
    braille123 = braille_to_int123(result_dict)
    parse_machine = ParseMachine(braille123)
    pinyin_list = []
    while parse_machine.get_one() != '':
        pinyin_list.append(parse_machine.get_one())
    with open(filename + '.txt', 'w') as f:
        f.write('\n'.join(pinyin_list))


braille_to_int123_map = {
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

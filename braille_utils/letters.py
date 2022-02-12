#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Braille symbols declaration
'''

# constants for special symbols label
num_sign = '##'
caps_sign = 'CC'
markout_sign = 'XX'

# general symbols common for various languages
sym_map = {
    '256': '.',
    '2'  : ',',
    '25' : ':',
    '26' : '?',
    '23' : ';',
    '235': '!',
    '2356':'()', # postprocess to (, ). Labeled as ((, )), ()
    '126':'(',
    '345':')',
    '36' : '-',
    '34' : '/',
    '3456': num_sign,
    '123456': markout_sign,
    # '6': "en",
    # '46': "EN",  # TODO only for Russian ?
}

# RU symbols
alpha_map_RU = {
    '1'  : 'а',
    '12' : 'б',
    '2456':'в',
    '1245':'г',
    '145' : 'д',
    '15' : 'е',
    '16' : 'ё',
    '245' : 'ж',
    '1356' : 'з',
    '24' : 'и',
    '12346' : 'й',
    '13' : 'к',
    '123' : 'л',
    '134' : 'м',
    '1345' : 'н', # preprocess to № if followed by number
    '135' : 'о',
    '1234' : 'п',
    '1235' : 'р',
    '234' : 'с',
    '2345' : 'т',
    '136' : 'у',
    '124' : 'ф',
    '125' : 'х',
    '14' : 'ц',
    '12345' : 'ч',
    '156' : 'ш',
    '1346' : 'щ',
    '12356' : 'ъ',
    '2346' : 'ы',
    '23456' : 'ь',
    '246' : 'э',
    '1256' : 'ю',
    '1246' : 'я',

    '45': caps_sign,
    '236': '«',  # <<
    '356': '»',  # >>
    '4': "'",
    '456': "|",
    '346': '§',  # mark as &&
}

# UZ symbols
alpha_map_UZ = {
    **alpha_map_RU,
    '1236': 'ў',
    '13456': 'қ',
    '12456': 'ғ',
    '1456': 'ҳ',
}

# EN symbols
alpha_map_EN = {
    '1': 'a',
    '12': 'b',
    '14': 'c',
    '145': 'd',
    '15': 'e',
    '124': 'f',
    '1245': 'g',
    '125': 'h',
    '24': 'i',
    '245': 'j',
    '13': 'k',
    '123': 'l',
    '134': 'm',
    '1345': 'n',
    '135': 'o',
    '1234': 'p',
    '12345': 'q',
    '1235': 'r',
    '234': 's',
    '2345': 't',
    '136': 'u',
    '1236': 'v',
    '2456': 'w',
    '1346': 'x',
    '13456': 'y',
    '1356': 'z',

    #'6': caps_sign, # TODO duplicate оf RU caps_sign
    '3': "'",
    '236': '«',  # <<
    '356': '»',  # >>
    # '236': '"',  # mark as <<
    # '356': '"',  # mark as >>
}

# UZL symbols
alpha_map_UZL = {
    **alpha_map_EN,
    '1236': 'o`',
    '12456': 'g`',
    '156': 'sh',
    '12345': 'ch',
}

# Greek letters
alpha_map_GR = {
    '1': 'α',
    '12': 'β',
    '1245': 'γ',
    '145': 'δ',
    '15': 'ε',
    '1356': 'ζ',
    '345': 'η',
    '1456': 'θ',
    '24': 'ι',
    '13': 'κ',
    '123': 'λ',
    '134': 'μ',
    '1345': 'ν',
    '1346': 'ξ',
    '135': 'ο',
    '1234': 'π',
    '1235': 'ρ',
    '234': 'σ',
    '2345': 'τ',
    '13456': 'υ',
    '124': 'φ',
    '125': 'χ',
    '12346': 'ψ',
    '245': 'ω',
    '46': caps_sign,
    '5': "'",  # stress
    '126': 'αι',
    '146': 'ει',
    '246': 'οι',
    '12456': 'υι',
    '16': 'αυ',
    '156': 'ευ',
    '1256': 'ηυ',
    '136': 'ου',
}

# Latvian letters
alpha_map_LV = {
    '1': 'a',
    '16': 'ā',
    '12': 'b',
    '14':'c',
    '146': 'č',
    '145': 'd',
    '15': 'e',
    '156': 'ē',
    '124': 'f',
    '1245': 'g',
    '12456': 'ģ',
    '125': 'h',
    '24': 'i',
    '246': 'ī',
    '245': 'j',
    '13': 'k',
    '136': 'ķ',
    '123': 'l',
    '1236': 'ļ',
    '134': 'm',
    '1345': 'n',
    '13456': 'ņ',
    '135': 'o',
    '1234': 'p',
    '1235': 'r',
    '234': 's',
    '2346': 'š',
    '2345': 't',
     '34': 'u',
    '346': 'ū',
    '2456': 'v',
    '345': 'z',
    '3456': 'ž',
    '46': caps_sign
}

# PL symbols
alpha_map_PL = {
    **alpha_map_EN,
    '16': 'ą',
    '146': 'ć',
    '156': 'ę',
    '126': 'ł',
    '1456': 'ń',
    '346': 'ó',
    '246': 'ś',
    '2346': 'ź',
    '12346': 'ż',

    '3': '.',
    '256': '/',
    '34': '\\',
}

# Digit symbols (after num_sign)
num_map = {
    '1': '1',
    '12': '2',
    '14': '3',
    '145': '4',
    '15': '5',
    '124': '6',
    '1245': '7',
    '125': '8',
    '24': '9',
    '245': '0',
}

# Digits in denominators of fraction
num_denominator_map = {
    '2': '/1',
    '23': '/2',
    '25': '/3',
    '256': '/4',
    '26': '/5',
    '235': '/6',
    '2356': '/7',
    '236': '/8',
    '35': '/9',
    '356': '/0', # postprocess num 0 /0 to %
}

# Symbols for Math Braille (in Russian braille, I suppose)
math_RU = {
    '2': ',',  # decimal separator
    '3': '..',  # postprocess to "." (thousand separator) if between digits else to * (multiplication).
    '235': '+',
    '36': '-',
    '236': '*',
    '256': '::',  # postprocess to ":" (division).
    '246': '<',
    '135': '>',
    '2356': '=',
    '126':'(',
    '345':')',
    '12356': '[',
    '23456': ']',
    '246': '{',
    '135': '}',
    '456': "|",
    '6': "en",
    '46': "EN",
}

pinyin_SPE_SHENG = {
    # 特殊声母
    '34': 'zh',
    '12345': 'ch',
    '156': 'sh',
    '245': 'r',
    '1356': 'z',
    '14': 'c',
    '234': 's',
}

pinyin_ABG_SHENG = {
    # 二义声母
    '1245': 'g/j',
    '13': 'k/q',
    '125': 'h/x',
}

pinyin_PLN_SHENG = {
    # 普通声母
    '12': 'b',
    '1234': 'p',
    '134': 'm',
    '124': 'f',
    '145': 'd',
    '2345': 't',
    '1345': 'n',
    '123': 'l',
}

pinyin_SHENG = {
    **pinyin_SPE_SHENG,
    **pinyin_ABG_SHENG,
    **pinyin_PLN_SHENG,
}

pinyin_SPE_Y_YUN = {
    # 直接加 y
    '126': 'in',
    '16': 'ing',
    '23456': 've',
    '456': 'vn',    # yvn
    '12346': 'van',
    '346': 'v',
    '24': 'i',
}

pinyin_SPE_Y_DEL_FST_YUN = {
    # 去首加 y
    '1246': 'ia',
    '345': 'iao',
    '15': 'ie',
    '146': 'ian',
    '1346': 'iang',
    '1456': 'iong',
}

pinyin_SPE_Y_I_TO_O_YUN = {
    # 变 i 为 o 加 y
    '1256': 'iu',
}

pinyin_SPE_W_YUN = {
    '136': 'u',
}

pinyin_SPE_W_DEL_FST_YUN = {
    # 去首加 w
    '12456': 'uan',
    '2356': 'uang',
    '123456': 'ua',
    '13456': 'uai',
    '135': 'uo',
}

pinyin_SPE_W_FST_TO_E_YUN = {
    # 变首为 e 加 w
    '25': 'un',   # wen, kun
    '256': 'ong',
    '2456': 'ui',
}

pinyin_SPE_SIG_YUN = {
    '1236': 'an',
    '236': 'ang',
    '356': 'en',
    '3456': 'eng',
    '1235': 'er',
    '246': 'ai',
    '235': 'ao',
    '2346': 'ei',
    '12356': 'ou',
    '35': 'a',
    '26': 'e',  # e/0
}

pinyin_YUN = {
    **pinyin_SPE_Y_YUN,
    **pinyin_SPE_Y_DEL_FST_YUN,
    **pinyin_SPE_Y_I_TO_O_YUN,
    **pinyin_SPE_W_YUN,
    **pinyin_SPE_W_DEL_FST_YUN,
    **pinyin_SPE_W_FST_TO_E_YUN,
    **pinyin_SPE_SIG_YUN,
}

pinyin_CN = {
    # 韵母
    **pinyin_YUN,

    # 声母
    **pinyin_SHENG,
}

# Codes for dicts
letter_dicts = {
    'SYM': sym_map,
    'RU': alpha_map_RU,
    'EN': alpha_map_EN,
    'GR': alpha_map_GR,
    'LV': alpha_map_LV,
    'PL': alpha_map_PL,
    'UZ': alpha_map_UZ,
    'UZL': alpha_map_UZL,
    'NUM': num_map,
    'NUM_DENOMINATOR': num_denominator_map,
    'MATH_RU': math_RU,
    'CN_PINYIN': pinyin_CN,
}



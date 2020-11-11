from braille_utils import label_tools as lt
from braille_utils import liblouis as louis
from braille_utils.postprocess  import lines_to_text, text_to_lines, interpret_text_louis, lines_to_unicode_braille

# for i in range(64):
#     s = chr(0x2800+i)
#     print(s, lt.int_to_label010(i), lt.int_to_letter(i,['RU', 'SYM']))
# s = louis.backTranslateString([r"D:\Programming\Braille\3rd_party\liblouis\tables\ru.ctb"], "\u2820\u281b \u2811  \u281e\u281e\u280a\n\u281d\u281b")
# print(s)

tables = [
r"ru.ctb",
 r"ru.tbl",
 r"ru-compbrl.ctb",
 r"ru-litbrl.ctb",
 #r"ru-litbrl.utb",
 r"ru-ru-g1.utb",
]

def validate_postprocess(in_text, out_text):
    res_text = lines_to_text(text_to_lines(in_text))
    assert res_text == out_text, (res_text, out_text)
    print(in_text, res_text)
    print(lines_to_unicode_braille(text_to_lines(in_text)))
    res_text2 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    for t in tables:
        res_text_ = interpret_text_louis(text_to_lines(in_text), [t])
        if res_text2 != res_text_:
            res_text2 = res_text_
            print(res_text2)


if __name__ == '__main__':
    #OK
    validate_postprocess('''абвг1234''', '''абвгабцд''')
    validate_postprocess('''~##~1234567890 +~##~23 =~##~17''', '''1234567890+23=17''')
    validate_postprocess('''аб«~6~и»вг''', '''аб«i»вг''')
    validate_postprocess('''~46~и вг''', '''I вг''')
    validate_postprocess('''~##~2))~6~r9n7o''', '''2))ringo''')

    validate_postprocess('''(~##~1) =~##~1''', '''(1)=1''')
    validate_postprocess('''а ~((~б~))~,''', '''а (б),''')
    validate_postprocess('''~((~в~))~,''', '''(в),''')
    validate_postprocess('''~()~~##~1~()~,''', '''(1),''')
    validate_postprocess('''~##~1,ма,''', '''1, ма,''')
    validate_postprocess('''~##~20-х годах''', '''20-х годах''')
    validate_postprocess('''~##~1\n0''', '''1\nж''')

    validate_postprocess('''ab  c

d e f''', '''аб  ц

д е ф''')

    validate_postprocess('''~1~b  c~##~34

d e f''', '''аб  ц34

д е ф''')


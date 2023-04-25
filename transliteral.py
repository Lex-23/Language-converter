import unicodedata

georgian_alphabet = []
for i in range(0x10D0, 0x10F1):
    char = chr(i)
    name = unicodedata.name(char, '')
    if 'GEORGIAN' in name:
        georgian_alphabet.append(char)

GE = georgian_alphabet

EN = ['a', 'b', 'g', 'd', 'e', 'v', 'z', 't', 'i', 'k`', 'l', 'm', 'n', 'o', 'p`', 'zh', 'r',
      's', 't`', 'u', 'p', 'k', 'gh', 'q`', 'sh', 'ch', 'ts', 'dz', 'ts`', 'ch`', 'kh', 'j', 'h']

RU = ['а', 'б', 'г', 'д', 'е', 'в', 'з', 'тэ', 'и', 'кэ', 'л', 'м', 'н', 'о', 'п', 'ж', 'р',
      'с', 'т', 'у', 'пэ', 'к', 'гэ', 'к`', 'ш', 'ч', 'тс', 'дз', 'ц', 'ч`', 'х', 'дж', 'х`']


def get_transliter_data():
    if len(GE) == len(EN) == len(RU):
        return {GE[ind]: (EN[ind], RU[ind]) for ind in range(len(GE))}


LANG_DATA = get_transliter_data()

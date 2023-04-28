from collections import namedtuple
from base.utilities.custom_exceptions import WrongLangKeyForTranscriptor


def transcript(text, lang_key, langs_map: dict, transcript_data):
    result = ''
    if lang_key in langs_map.keys():
        for char in text:
            if char in transcript_data:
                result += f'{transcript_data[char][langs_map[lang_key]]} '
            else:
                result += char
        return result
    else:
        raise WrongLangKeyForTranscriptor


def create_converted_data_namedtuple_object(first_key, second_key):
    return namedtuple(
        'ConvertedData',
        [
            'original',
            f'{first_key}_transcript',
            f'{second_key}_transcript',
            f'{first_key}_translate',
            f'{second_key}_translate'
        ]
    )

import unicodedata
from base.utilities.custom_exceptions import TranscriptDataMismatchLenError


def get_transcript_dict(original_unicode_range: range, original_name: str, first_lang: list, second_lang: list) -> dict:
    """
    :param original_unicode_range: range of letters of original alphabet in unicode (only lower case).
    example: range(0x10D0, 0x10F1)
    :param original_name: name of original language in upper case. example: 'ENGLISH'
    :param first_lang: list of transcript of each letter from original alphabet to this language
    :param second_lang: list of transcript of each letter from original alphabet to this language
    :return: dict, where keys is letters from original and values are tuple of transcript first and second
    """

    original_alphabet = []
    for i in original_unicode_range:
        char = chr(i)
        name = unicodedata.name(char, '')
        if original_name in name:
            original_alphabet.append(char)

    if len(original_alphabet) == len(first_lang) == len(second_lang):
        return {
            original_alphabet[ind]: (first_lang[ind], second_lang[ind])
            for ind in range(len(original_alphabet))
        }
    else:
        raise TranscriptDataMismatchLenError

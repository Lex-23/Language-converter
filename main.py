from transliteral import LANG_DATA
from deep_translator import GoogleTranslator as trns
from collections import namedtuple


ConvertedData = namedtuple(
    'ConvertedData',
    [
        'original',
        'en_transcript',
        'ru_transcript',
        'en_translate',
        'ru_translate'
    ]
)


class LanguageConverter:
    """
    Class for transliterating text from georgian language to english and russian (main purpose).
    As an optional feature, there is feature for translating text to english and russian.
    Main goal: get text in georgian language and return transcript and translated text.
    """

    def __init__(self, text: str):
        self._text = text.lower()

    def __str__(self):
        return self._text

    def _transcript_to(self, key):
        """
        get text in georgian and return transcript of text (to chosen language)
        :param key: 'en' | 'ru'
        :return: transcript text
        """
        lang = {'en': 0, 'ru': 1}
        result = ''
        for char in self._text:
            if char in LANG_DATA:
                result += f'{LANG_DATA[char][lang[key]]} '
            else:
                result += char
        return result

    def _translate_to(self, key):
        """
        get text in georgian and return translated text (to chosen language)
        :param key: 'en' | 'ru'
        :return: translated text
        """
        return trns(source='ka', target=key).translate(self._text)

    @property
    def convert(self):
        return ConvertedData(
            self._text,
            self._transcript_to("en"),
            self._transcript_to("ru"),
            self._translate_to('en'),
            self._translate_to('ru')
        )

    def display(self):
        data = self.convert
        print(
            data.original,
            data.en_transcript,
            data.ru_transcript,
            data.en_translate,
            data.ru_translate,
            sep='\n', end=''
        )

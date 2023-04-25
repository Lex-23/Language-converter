from base.base_converter import BaseLanguageConverter
from georgian_en_ru.services import transcript_georgian, translate_georgian, ConvertedData, translate_to_georgian


class GeorgianEnRuConverter(BaseLanguageConverter):
    """
    Class for convert georgian language to english and russian (transcript and translate).
    """

    def _transcript_to(self, key):
        return transcript_georgian(text=self._text, lang_key=key)

    def _translate_to(self, key):
        return translate_georgian(text=self._text, key=key)

    @property
    def convert(self):
        return ConvertedData(
            self._text,
            self._transcript_to("en"),
            self._transcript_to("ru"),
            self._translate_to('en'),
            self._translate_to('ru')
        )

    @classmethod
    def translate_to_ge(cls, text):
        return translate_to_georgian(text)

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

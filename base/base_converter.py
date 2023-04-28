class BaseLanguageConverter:
    """
    Class for transcript text from original language to other two (main purpose).
    As an optional feature, there is feature for translating text to other two.
    Main goal: get text in original language and return transcript and translated text.
    """

    def __init__(self, text: str):
        self._text = text.lower()

    def __str__(self):
        return self._text

    def _transcript_to(self, key):
        """
        Does transcript from init text to key language text
        :param key: key language for target transcript (example format: 'en')
        :return: transcript text
        """

    def _translate_to(self, key):
        """
        Does translate from init text to key language text
        :param key: key language for target transcript (example format: 'en')
        :return: translated text
        """

    def convert(self):
        """
        :return: converted (include transcript and translated text) data
        """

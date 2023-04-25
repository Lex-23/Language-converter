from base.transcript_data import get_transcript_dict
from base.transcriptors import create_converted_data_namedtuple_object, transcript
from base.translaters import google_translate
from base.utilities.transcript_data import EN_KA, RU_KA

GEORGIAN_DATA = get_transcript_dict(
    original_unicode_range=range(0x10D0, 0x10F1),
    original_name='GEORGIAN',
    first_lang=EN_KA,
    second_lang=RU_KA
)

LANGS_MAP = {'en': 0, 'ru': 1}


def transcript_georgian(text, lang_key, langs_map=LANGS_MAP, transcript_data=GEORGIAN_DATA):
    return transcript(text, lang_key, langs_map, transcript_data)


def translate_georgian(text, key):
    return google_translate(source_key='ka', target_key=key, text=text)


def translate_to_georgian(text):
    return google_translate(source_key='auto', target_key='ka', text=text)


ConvertedData = create_converted_data_namedtuple_object('en', 'ru')

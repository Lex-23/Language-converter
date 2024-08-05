from georgian_en_ru.converter import GeorgianEnRuConverter as Converter


def create_dict_to_response(converted_data):
    return {
        'ge':  converted_data.original,
        'en_transcript': converted_data.en_transcript,
        'ru_transcript': converted_data.ru_transcript,
        'en_translate': converted_data.en_translate,
        'ru_translate': converted_data.ru_translate,

    }


def convert_data_to_georgian(text):
    converted_data = Converter(Converter.translate_to_ge(text)).convert
    return create_dict_to_response(converted_data)


def convert_data_from_georgian(text):
    converted_data = Converter(text).convert
    return create_dict_to_response(converted_data)

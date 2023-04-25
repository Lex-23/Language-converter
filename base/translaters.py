from deep_translator import GoogleTranslator as ggltrn


def google_translate(source_key, target_key, text):
    return ggltrn(source=source_key, target=target_key).translate(text)

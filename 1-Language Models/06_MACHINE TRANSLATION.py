from translate import Translator 

translator = Translator(to_lang="es")

text = 'Hello, how are you?'

translation = translator.translate(text)

print('Translated text:', translation)

import string

text = "Hello, World! How are you today?"
translator = str.maketrans('', '', string.punctuation)
no_punct = text.translate(translator)
print(no_punct)
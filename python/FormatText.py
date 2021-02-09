import nltk

#nltk.download('punkt')

def format_text(text):
    sentences = text.split('.')
    formatted_text = [('.'.join([sentences[i-1], sentence]) + '.') for i, sentence in enumerate(sentences) if i % 2 == 1 and len(sentence) != 0]
    if len(sentences) % 2 == 1:
        formatted_text.append(sentences[-1])
    return formatted_text

def format_text2(text):
    sentences = text.split('.')
    formatted_text = []
    for i, sentence in enumerate(sentences):
       if i % 2 == 1:
           if len(sentence) != 0:
               formatted_text.append('.'.join([sentences[i-1], sentence]) + '.')
    if len(sentences) % 2 == 1:
        formatted_text.append(sentences[-1])
    return formatted_text

def test(text):
    tokens = nltk.sent_tokenize(text)
    text2 = nltk.Text(tokens)
    return text2

text = ""
with open('test_soup.txt') as file:
    text = "".join(file.readlines())
for token in nltk.sent_tokenize(text):
    print(token)
    print()

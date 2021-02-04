def format_text(text):
    sentences = text.split('.')
    formatted_text = []
    for i in range(len(sentences)):
        if i % 2 == 1:
            if len(sentences[i]) != 0:
                if sentences[i][0] == ' ':
                    formatted_text.append('.'.join([sentences[i-1], sentences[i]]))
                else:
                    formatted_text.append('. '.join([sentences[i-1], sentences[i]]))
    if len(sentences) % 2 == 1:
        formatted_text.append(sentences[-1])
    return formatted_text
with open ('referat.txt', 'r', encoding = 'utf-8') as ref:
    content = ref.read()
    content_length = len(content)
    print (f'The text length is {content_length} characters.')

    content_words = content.split()
    words_no = len(content_words)
    print (f'The text contains {words_no} words.')

content2 = content.replace('.', '!')

with open ('referat2.txt', 'w', encoding = 'utf-8') as ref2:
    ref2.write(content2)








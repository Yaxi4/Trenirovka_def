def longest_word_in_file(file_name):
    file=open('file_name',encoding='utf-8')
    max_word=''
    for line in file:
        words=line.split()
        for word in words:
            #print(word) - напечатает слова в нашем файле
            word_with_punc=remove_punc(word) #уберет пунктуацию
            if len(word_with_punc)> len(max_word):
                max_word=word_with_punc
    return max_word

def remove_punc(word):
    from string import punctuation
    for punc in punctuation:
        if punc in word:
            word = word.replace(punc,'')
    return word



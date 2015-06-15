# more_functions.py

def break_words (stuff):
    '''This function will break up words for us.'''
    words = stuff.split(' ')
    '''string.split(str=' ',num=string.count(str)):　　
以str为分隔，符切片string，如果num有指定值，则仅分隔num个子字符串。'''
    return words

def sort_words (words):
    '''Sorts the words.'''
    return sorted (words)

def print_first_word (words):
    '''Prints the first word after popping it off.'''
    word = words.pop (0)
    print (word)
    return

def print_last_word (words):
    '''Prints the last word after popping it off.pop()函数'''
    word = words.pop (-1)
    print (word)
    return

def sort_sentence (sentence):
    '''Takes in a full sentence and returns the sorted words.'''
    words = break_words (sentence)
    return sort_words (words)

def print_first_and_last (sentence):
    '''Print the first and last words of the sentence.'''
    words = break_words (sentence)
    print_first_word (words)
    print_last_word (words)
    return

def print_first_and_last_sorted (sentence):
    '''sorts the words then prints the first and the last one'''
    words = sort_sentence (sentence)
    print_first_word (words)
    print_last_word (words)
    return

 

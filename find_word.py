# find_word.py

def find_word(search_term, word_list):  # 两个参数
    matching_words = [] # 空表
    for element in word_list: # 对于输入字符串中每个元素
        if search_term in element: # 加入字符包含在元素中
            matching_words.append(element) # 添加进表
    return matching_words # 返回包含有输入字符的元素的表

mystrings = ['frog', 'fox', 'foxtrot', 'toad']

search_term = input('Enter a word to search for:')

words_found = find_word(search_term, mystrings)
print("I found:", words_found, "my search term was:", search_term)

myotherlist = ['bang', 'thump', 'biff']
print("Searched for 'b'", find_word('b', myotherlist))

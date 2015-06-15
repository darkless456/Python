# re.py

import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print(regex.findall(text))   #查找所有包含'oo'的单词
print(regex.sub(lambda m: '[' + m.group(0) + ']', text))
print(re.sub(r'\s+', '-', text))


 
phonePattern = re.compile(r'''
    # don't match beginging of string
(\d{3}) # 3 digits
\D*     #any number of non-digits
(\d{3}) # 3 digits
\D*     #any number of non-digits
(\d{4}) # 4 digits
\D*     #any number of non-digits
(\d*)   #any number of digits
''',re.VERBOSE)
print(phonePattern.search('work 1-(800)555.1212 #1234').groups()) #('800', '555', '1212', '1234')

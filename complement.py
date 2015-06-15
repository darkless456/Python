# complement.py

def complement(dna_string):                 # 定义函数

    dna_complement = { 'a' : 't',           # 定义dict 键值{'key':'value'}
                       'g' : 'c',
                       't' : 'a',
                       'c' : 'g'}
    comp_string = '' # 建立空字符串

    for base in dna_string:           # 对于输入的每个字符
        comp_string += dna_complement.get(base, 'n') # 输入每个字符加到空字符串
        #if base in dna_complement:
            #comp_string += dna_complement[base]
        #else:
            #comp_string += 'n'
    return comp_string # 返回最后字符串值

dna_string = input('Enter a DNA string: ') # 输入函数参数key
comp_strings = complement(dna_string) # 实例化
print("Complement is: ", comp_strings)

# 实现功能
# 将输入的键转换为对应的值

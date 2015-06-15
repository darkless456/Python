# complement_from_file.py

def complement(dna_string):
    dna_complement = {'a':'b' , 'b':'c' , 'c':'d' , 'd':'d'}

    comp_string = ''

    for base in dna_string:
        comp_string += dna_complement.get(base, 'n')
    return comp_string

dna_string = input('Enter a DNA string file name: ') # 读取一个文件
han = open(dna_string,'r').read()
comp_string = complement(han)
print("Complement is: ", comp_string)

# 输出结果a所对应不正确。

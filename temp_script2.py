# temp_script2.py

def complement(dna_string):
    string = {'a':'b' , 'b':'c' , 'c':'d' , 'd':'e'}

    comp_string = ''

    for base in dna_string:
        comp_string += string.get(base, 'n')

    return comp_string

dna_string = input("The Enter is: ")
string2 = complement(dna_string)
print("The Output is ", string2)
        

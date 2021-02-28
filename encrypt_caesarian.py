def encrypt(str_input,shift):
    str_output  =  ""
    shift       %= 26
    for i in str_input:
        if   i.isupper():
            str_output += chr(((ord(i)-65+shift))%26+65)
        elif i.islower():
            str_output += chr(((ord(i)-97+shift))%26+97)
        else:
            str_output += i
    return str_output

def decrypt(str_input):
    strs_output = []
    for i in range(0,26):
        strs_output.append("+" +str(i) +": " + encrypt(str_input,-i))
    return strs_output
        

print(encrypt("Sphinx of Jade Quartz, judge my Vow.",8))
samp=decrypt("Sphinx of Jade Quartz, judge my Vow.")
for i in samp:
    print(i)

print(encrypt("Axpqvf wn Rilm Ycizbh, rclom ug Dwe.", -8))

import base64

def encode_b64():

    input1 = input("ponha aqui a sua frase:")
    encode = input1.encode("ascii") #Mete em ASCII
    bytes1 = base64.b64encode(encode) #Mete em 8bits(1byte)
    decode = bytes1.decode("ascii") #Tira o ASCII
    print("frase codificada" , decode)


def decode_b64():

    input2 = input("meta aqui o texto:")
    encode2 = input2.encode("ascii") #Mete em ASCII
    bytes2 = encode2.b64decode(encode) #Mete em 8bits(1byte)
    decode2 = bytes2.decode("ascii") #tira ASCII
    print("decode completo: " , decode2 )

pergunta = int(input("1-base64"))

if pergunta == 1:
    pergunta2 = int(input("1-encode      " \
                          "2-decode"))
if pergunta2 == 1:
    encode_b64()

else:
    decode_b64()
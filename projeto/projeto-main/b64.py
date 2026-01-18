import base64

def encode_b64():

    text = input("ponha aqui a sua frase:")
    text_bytes = text.encode("ascii") #Mete em ASCII
    encoded_bytes = base64.b64encode(text_bytes) #Mete em 8bits(1byte)
    encoded_str = encoded_bytes.decode("ascii") #Tira o ASCII
    print("frase codificada" , encoded_str)


def decode_b64():

    encoded_text = input("mete aqui o texto:")
    encoded_bytes = encoded_text.encode("ascii") #Mete em ASCII
    decoded_bytes = base64.b64decode(encoded_bytes) #Mete em 8bits(1byte)
    decoded_text = decoded_bytes.decode("ascii") #tira ASCII
    print("decode completo: " , decoded_text )

choice = int(input("1-base64"))

if choice == 1:
    sub_choice = int(input("1-encode     2-decode:"))
    if sub_choice == 1:
        encode_b64()
    else:
        decode_b64()
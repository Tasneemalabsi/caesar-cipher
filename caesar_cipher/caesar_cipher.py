import nltk
import re
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
name_list = names.words()

def encrypt(text:str, shift):
    """
    this function takes an english sentence and shifts it depending on the given shift
    Arguments:
    text: string, the given sentence
    shift: the amount of shift in the returned sentence
    Returns: encrypted sentence

    """
    arr = text.split()
    offset = 65
    cipher_list =[]
    for i in arr:
        cipher = ""
        for char in i:
            if char.isalpha(): 
                shifted_order= ord(char.upper())+ shift - offset
                shifted_char = chr(shifted_order % 26 + offset)
                if char.isupper():
                    cipher += shifted_char
                elif char.islower():
                    cipher += shifted_char.lower()  
            else:
                cipher+=char
        cipher_list.append(cipher)            
    return " ".join(cipher_list)


def decrypt(text, shift):
    """
    this function takes an encrypted sentence and an integer and removes the amount of shift given to the original sentence
    Arguments:
    text: string, the encrypted sentence
    shift: the amount of shift removed from the encrypted version
    Returns: string, decrypted sentence
     
    """
    return encrypt(text, -shift)    

   
def crack(text):
    """
    this function takes an encrypted sentence and decrypt it without knowing the key(the shift in the encrypted sentence)
    Arguments:
    text: string, the encrypted sentence
    Returns: string, decrypted sentence
     
    """
    decrypted_text = ''
    for i in range(27):
        arr = decrypt(text, i).split()
        counter = 0
        for word in arr:
            clean_word = re.sub(r'[^A-Za-z]','',word)
            if clean_word.lower() in word_list or clean_word in name_list:
                counter += 1
        total_words = len(arr)
        ratio =  counter / total_words

        percentage = ratio * 100
        threshold = 50
        if percentage > threshold:
            decrypted_text= " ".join(arr)
    return decrypted_text        
      

# if __name__ == "__main__":
#     print(encrypt("It was the best of times, it was the worst of times.", 13))
#     print(decrypt("Nz obnf 11 jt Ubtoffn", 1)) 
#     print(crack("Nz obnf 11 jt Ubtoffn"))

    
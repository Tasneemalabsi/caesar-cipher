from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import decrypt, encrypt, crack
import pytest


def test_version():
    assert __version__ == '0.1.0'

# test encrypt a string with a given shift
def test_encrypt_string():
    #Arrange
    expected = "Nz obnf 11 jt Ubtoffn"
    #Act
    actual = encrypt("My name 11 is Tasneem", 1)
    #Assert
    assert actual == expected

# test decrypt a previously encrypted string with the same shift    
def test_decrypt_encrypted_text():
    #Arrange
    expected = "My name 11 is Tasneem"
    #Act 
    actual = decrypt("Nz obnf 11 jt Ubtoffn", 1)
    #Assert
    assert actual == expected

# test encryption should handle upper and lower case letters
def test_encryption_returns_upper_and_lower():
    #Arrange
    expected = "Nz ObNf Jt UbToffN"
    #Act 
    actual = encrypt("My NaMe Is TaSneeM", 1)
    #Assert
    assert actual == expected

# test encryption should allow non-alpha characters but ignore them, including white space 
def test_encryption_handles_non_alpha_letters():
    #Arrange
    expected = "Nz,, ObNf13"
    #Act 
    actual = encrypt("My,, NaMe13", 1)
    #Assert
    assert actual == expected 

# test decrypt encrypted version of "It was the best of times, it was the worst of times." WITHOUT knowing the shift used.
def test_decrypt_without_key():
    #Arrange
    expected = "It was the best of times, it was the worst of times."
    #Act 
    actual = crack("Vg jnf gur orfg bs gvzrf, vg jnf gur jbefg bs gvzrf.") # this sentence is the encrypted version of the sentence above, when the shift = 13
    #Assert
    assert actual == expected

    
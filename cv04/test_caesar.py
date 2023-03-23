'''
Test suite pro cviceni 4

@author: Jiri Vrany
'''
import caesar


def test_encrypt_text_s_mezerami():
    '''
    original text To bolt or not to be
    offset 7
    '''
    original = 'to bolt or not to be'
    vzor = 'av ivsa vy uva av il'
    vysledek = caesar.encrypt(original, 7)
    assert vzor == vysledek


def test_encrypt_large_offset():
    '''
    offset 27
    vysledek by mel byt stejny jako pri offset 1
    '''
    original = 'flaxa'
    vzor = 'gmbyb'
    vysledek = caesar.encrypt(original, 27)
    assert vzor == vysledek


def test_encrypt_velka_mala():
    '''
    offset 19
    velka pismena se musi zachovat
    '''
    original = 'VeLkA MaLa'
    vzor = 'OxEdT FtEt'
    vysledek = caesar.encrypt(original, 19)
    assert vzor == vysledek


def test_decrypt_text_s_mezerami():
    '''
    original text To bolt or not to be
    offset 7
    '''
    vzor = 'to bolt or not to be'
    original = 'av ivsa vy uva av il'
    vysledek = caesar.decrypt(original, 7)
    assert vzor == vysledek


def test_decrypt_large_offset():
    '''
    offset 27
    vysledek by mel byt stejny jako pri 1
    '''
    vzor = 'flaxa'
    original = 'gmbyb'
    vysledek = caesar.decrypt(original, 27)
    assert vzor == vysledek


def test_decrypt_velka_mala():
    '''
    offset 19
    velka pismena se musi zachovat
    '''
    vzor = 'VeLkA MaLa'
    original = 'OxEdT FtEt'
    vysledek = caesar.decrypt(original, 19)
    assert vzor == vysledek

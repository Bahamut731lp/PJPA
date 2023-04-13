'''
Test suite pro cviceni 6

@author: Kevin Danek
'''
import search

def test_dve_souhlasky_bear():
    '''
    original text To bolt or not to be
    offset 7
    '''
    counter = search.create_counter()
    search.match_regexes("bear", counter)

    assert counter["two_vowels"] == 1

def test_tri_souhlasky_atomic():
    '''
    original text To bolt or not to be
    offset 7
    '''
    counter = search.create_counter()
    search.match_regexes("atomic", counter)

    assert counter["three_vowels"] == 1

def test_delka_sest():
    '''
    original text To bolt or not to be
    offset 7
    '''
    counter = search.create_counter()
    search.match_regexes("terrible", counter)

    assert counter["six_characters"] == 1

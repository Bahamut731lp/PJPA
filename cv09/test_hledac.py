"""
    Modul pro testování cvičení 9
"""
import hledac

def test_no_arguments():
    """
       Test, že program vrátí nápovědu, pokud nebyl předán žádný parametr. 
    """
    code = hledac.main()
    assert code == -1

def test_no_pattern_value():
    """
       Test, že program vrátí nápovědu, pokud nebyla předána hodnota vzoru. 
    """
    code = hledac.main(["-f", "./lipsum.txt", "-s"])
    assert code == -1

def test_no_pattern_argument():
    """
       Test, že program vrátí nápovědu, pokud nebyla předán argument vzoru
    """
    code = hledac.main(["-f", "./lipsum.txt"])
    assert code == 0

def test_with_pattern_argument():
    """
       Test, že program skončí správně při jednom vzoru 
    """
    code = hledac.main(["-f", "./lipsum.txt", "-s", "orem"])
    assert code == 1

def test_with_multiple_pattern_argument():
    """
       Test, že program skončí správně při více vzorech 
    """
    code = hledac.main(["-f", "./lipsum.txt", "-s", "dolor", "amet"])
    assert code == 1

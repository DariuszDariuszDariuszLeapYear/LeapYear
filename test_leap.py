from leap import custom_isleap

def test_custom_isleap():
    assert custom_isleap(2001) == False
    assert custom_isleap(2002) == False
    assert custom_isleap(2003) == False
    assert custom_isleap(2004) == True
    assert custom_isleap(2004.345345) == False
    assert custom_isleap(1700) == False
    assert custom_isleap(1800) == False
    assert custom_isleap(1900) == False
    assert custom_isleap(1600) == True
    assert custom_isleap(2000) == True
    assert custom_isleap("2004") == False
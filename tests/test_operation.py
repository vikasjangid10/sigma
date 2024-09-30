from src.operation import multi, devide
def test_multi():
    assert multi(2,3) == 6
    assert multi(5,9) == 45

def test_devide():
    assert devide(10,2) == 5
    assert devide(21,7) == 3
    assert devide(80,10) == 8
    assert devide(28,7) == 4
from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci():
    Num1=fibonacci(2)
    actual=1
    assert Num1==actual

def test_lucas():
    Num1=lucas(6)
    actual=18
    assert Num1==actual


def test_sum_series():
    Num1=sum_series(2,4,9)
    actual=13
    assert Num1==actual
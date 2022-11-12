import solution

def test_reverseString() -> None:
    i='test'
    o='tset'
    assert solution.reverseStringMeth(i) == o
    assert solution.reverseStringSlice(i) == o
    assert solution.reverseStringRecursive(i) == o
    assert solution.reverseStringReduce(i) == o
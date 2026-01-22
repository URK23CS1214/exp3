from app import add

def test_add():
    # Indent these statements to belong to the function
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

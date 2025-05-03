from p03 import get

def test_get():
    r = get()
    assert r.status_code == 200

# tests/test_hello.py

from src.hello import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"
# tests/test_hello.py

from src.hello import hello_world, hello_universe

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_hello_universe():
    assert hello_universe() == "Hello, Universe!"

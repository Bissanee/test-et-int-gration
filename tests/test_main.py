from main import hello_world


def test_true_equals_true():
    assert True == True


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

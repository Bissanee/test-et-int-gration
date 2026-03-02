def hello_world():
    print("Hello, World!")


def test_true_equals_true():
    assert True == True, "Le test a échoué : True devrait être égal à True"
    print("Test passé : True == True")


if __name__ == "__main__":
    hello_world()
    test_true_equals_true()

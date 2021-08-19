import images_functions
import images


def test_one_by_one():
    """
    Test a group of images one by one.
    """
    weights = images_functions.return_weights()
    imgs = images.return_images()

    testing = images_functions.unit_test(weights, imgs)

    """
    If you test any value number you gonna take values bigger than 849.99 to one and other values to zero. If you change
    the values of check_error() you gonna take other from zero and one.
    """
    for i in testing:
        if i > 849.99:
            print(1)
        else:
            print(0)


def test_cracking_images():
    weights = images_functions.return_weights()

    tests = ["images_tests/teste.png",
             "images_tests/teste2.png",
             "images_tests/teste3.png",
             "images_tests/teste4.png",
             "images_tests/teste5.png"]

    for adress in tests:
        crack = images_functions.cracking(adress)

        testing = images_functions.multiple_test(weights, crack)
        print('BINARY VALUE: ', end='')
        result = []
        for i in testing:
            if i > 849.99:
                result.append(1)
                print(1, end='')
            else:
                result.append(0)
                print(0, end='')

        print(f'\nDECIMAL VALUE:: {images_functions.bin_to_dec(result)}')
        print()


if __name__ == '__main__':
    test_one_by_one()
    print()
    print()
    test_cracking_images()

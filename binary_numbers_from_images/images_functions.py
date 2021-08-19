import random
from matplotlib.image import imread
import numpy as np


def counting(image_name, show=False):
    """
    :param image_name: name of the image with his way, like : 'imagens/um1.png'
    :param show: if you want to see the values from matrix.
    :return: the width and height.
    """
    image = imread(image_name)
    count_line = 0
    count_column = 0

    for lines in image:  # Passing for the lines
        for element in lines:  # Passing any element of lines
            if show:
                print(element, end=' ')
            if count_line == 0:
                count_column += 1
        count_line += 1
        if show:
            print()

    return count_line, count_column


def start_weights(count_line, count_column):
    """
    :param count_line: amount of lines.
    :param count_column: amount of columns.
    :return: a numpy array with length of lines and columns given with random numbers.
    """
    new_weights = []
    for line in range(count_line):
        for column in range(count_column):
            new_weights.append(random.random())

    return np.array(new_weights)


def check_error(weights, images):
    """
    Function to test the model after try new values
    :param weights: weights of IA.
    :param images: a list with matrix of images.
    :return: the absolute value of error.
    """
    index_weight = 0
    error = 0
    index = 0
    for image in images:  # Passing for images
        if index % 2 == 0:
            error -= 7200  # This value and 5500 is to differentiate zeros from ones.
        else:
            error += 5500

        index += 1
        for line in image:  # Passing for any line
            for pixel in line:  # Passing for any pixel in any line one by one
                error += pixel[0] * weights[index_weight]
                index_weight += 1

        index_weight = 0

    return abs(error)


def update_weights(weights, images):
    """
    Here is the function to modify the weights to find the best set to the model with a group of images.

    :param weights: List of weights.
    :param images: List of matrix of images.
    """

    for index_weight in range(len(weights)):
        old_weight = weights[index_weight]
        error_before = check_error(weights, images)
        weights[index_weight] = random.random() * random.choice([1, -1]) + random.choice([1, 0])
        error_after = check_error(weights, images)

        if error_after > error_before:
            weights[index_weight] = old_weight
            print(error_before)
        else:
            print(error_after)
        index_weight += 1


def unit_test(weights, images):
    """
    Function to test the values one by one.

    :param weights: A list of weights finded on training.
    :param images: A group of images that you want to test.
    :return: A real value, this value can be related with one and zero
    """
    count = 0
    value = 0
    results = []
    for image in images:  # Passing for images
        for line in image:  # Passing for any line
            for pixel in line:  # Passing for any pixel in any line one by one
                value += pixel[0]*weights[count]

                count += 1

        results.append(value)
        count = 0
        value = 0

    return results


def return_weights():
    """
    :return: return weights that I find for people who don't want to run hours of training =D
    """
    with open('weights.txt', 'r') as archive:
        weights = archive.readlines()
        weights = str(weights).split(',')
        weights[0] = weights[0][2:-1]
        weights[-1] = weights[-1][0:-2]

    count = 0
    for weight in range(len(weights)):
        weights[weight] = float(weights[weight])
        count += 1

    return weights


def cracking(image):
    """
    Take a image 50x50*k and make k images 50x50.
    :param image: The name with directory of a function.
    :return: A list with new values
    """
    image = imread(image)

    # Couting how many pixels are in the image:
    count_pixels = 0
    for lines in image:
        for _ in lines:
            count_pixels += 1

    new_images = []
    numbers_of_pics = int(count_pixels/2500)

    for _ in range(numbers_of_pics):
        new_images.append([])

    # cracking the main image in others images
    count_pixels = 0
    img = 0
    for lines in image:
        for pixels in lines:
            new_images[img].append(pixels[0])
            count_pixels += 1

            if count_pixels == 50:
                img += 1
                count_pixels = 0
        img = 0

    return new_images


def multiple_test(weights, images_cracked):
    """
    :param weights: weights from the training.
    :param images_cracked: a list of images cracked after use the function 'cracking'
    :return:
    """
    results = []
    result = 0
    for image in images_cracked:
        for index in range(len(weights)):
            result += image[index]*weights[index]

        results.append(result)
        result = 0

    return results


def bin_to_dec(binary):
    """
    Pass a binary number to decimal number.
    :param binary: A list with binary values one by one.
    :return: corresponding decimal number of binary number.
    """
    binary.reverse()
    dec = 0
    count = 0
    for value in binary:
        dec += 2**count * value
        count += 1

    return dec

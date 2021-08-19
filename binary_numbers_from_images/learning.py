import images_functions
import images


if __name__ == '__main__':
    images = images.return_images()
    lines, columns = images_functions.counting('images_training/um1.png')
    weights = images_functions.start_weights(lines, columns)

    for i in range(3):
        images_functions.update_weights(weights, images)
        with open('new_weights', 'w') as archive:
            for weight in weights:
                archive.write(f'{weight},')  # Remove the ',' in the final!

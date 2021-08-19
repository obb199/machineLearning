from matplotlib.image import imread


def return_images():
    """
    Function to return the images applied to 'imread' that I used to train the model.
    'imread' is used to transform images png to matrix.

    """
    imgs = [imread('images_training/um1.png'),  imread('images_training/zero1.png'),
            imread('images_training/um2.png'),  imread('images_training/zero2.png'),
            imread('images_training/um3.png'),  imread('images_training/zero3.png'),
            imread('images_training/um4.png'),  imread('images_training/zero4.png'),
            imread('images_training/um5.png'),  imread('images_training/zero5.png'),
            imread('images_training/um6.png'),  imread('images_training/zero6.png'),
            imread('images_training/um7.png'),  imread('images_training/zero7.png'),
            imread('images_training/um8.png'),  imread('images_training/zero8.png'),
            imread('images_training/um9.png'),  imread('images_training/zero9.png'),
            imread('images_training/um10.png'), imread('images_training/zero10.png'),
            imread('images_training/um11.png'), imread('images_training/zero11.png'),
            imread('images_training/um12.png'), imread('images_training/zero12.png'),
            imread('images_training/um13.png'), imread('images_training/zero13.png'),
            imread('images_training/um14.png'), imread('images_training/zero14.png'),
            imread('images_training/um15.png'), imread('images_training/zero15.png'),
            imread('images_training/um16.png'), imread('images_training/zero16.png'),
            imread('images_training/um17.png'), imread('images_training/zero17.png'),
            imread('images_training/um18.png'), imread('images_training/zero18.png'),
            imread('images_training/um19.png'), imread('images_training/zero19.png'),
            imread('images_training/um20.png'), imread('images_training/zero20.png'),
            imread('images_training/um21.png'), imread('images_training/zero21.png'),
            imread('images_training/um22.png'), imread('images_training/zero22.png'),
            imread('images_training/um23.png'), imread('images_training/zero23.png'),
            imread('images_training/um24.png'), imread('images_training/zero24.png'),
            imread('images_training/um25.png'), imread('images_training/zero25.png'),
            imread('images_training/um26.png'), imread('images_training/zero26.png'),
            imread('images_training/um27.png'), imread('images_training/zero27.png'),
            imread('images_training/um28.png'), imread('images_training/zero28.png'),
            imread('images_training/um29.png'), imread('images_training/zero29.png'),
            imread('images_training/um30.png'), imread('images_training/zero30.png'),
            imread('images_training/um31.png'), imread('images_training/zero31.png'),
            imread('images_training/um32.png'), imread('images_training/zero32.png'),
            imread('images_training/um33.png'), imread('images_training/zero33.png'),
            imread('images_training/um34.png'), imread('images_training/zero34.png'),
            imread('images_training/um35.png'), imread('images_training/zero35.png'),
            imread('images_training/um36.png'), imread('images_training/zero36.png'),
            imread('images_training/um37.png'), imread('images_training/zero37.png'),
            imread('images_training/um38.png'), imread('images_training/zero38.png'),
            imread('images_training/um39.png'), imread('images_training/zero39.png'),
            imread('images_training/um40.png'), imread('images_training/zero40.png'),
            imread('images_training/um41.png'), imread('images_training/zero41.png'),
            imread('images_training/um42.png'), imread('images_training/zero42.png'),
            imread('images_training/um43.png'), imread('images_training/zero43.png'),
            imread('images_training/um44.png'), imread('images_training/zero44.png'),
            imread('images_training/um45.png'), imread('images_training/zero45.png'),
            imread('images_training/um46.png'), imread('images_training/zero46.png'),
            imread('images_training/um47.png'), imread('images_training/zero47.png'),
            imread('images_training/um48.png'), imread('images_training/zero48.png'),
            imread('images_training/um49.png'), imread('images_training/zero49.png'),
            imread('images_training/um50.png'), imread('images_training/zero50.png'),
            ]

    return imgs

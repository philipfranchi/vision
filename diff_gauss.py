from gaussian import gauss

import PIL.Image
import helpers

gb_kernel = [
    [1, 4, 7, 4, 1],
    [4, 16, 24, 26, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 24, 26, 4],
    [1, 4, 7, 4, 1]
]


gs_kernel = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]


def diff_gauss(pixels, width, height):

    bigGauss = gauss(pixels, width, height, gb_kernel).load()
    smallGauss = gauss(pixels, width, height, gs_kernel).load()

    image = PIL.Image.new('RGB', (width, height))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            pixels[x, y] = helpers.subtract(bigGauss[x, y], smallGauss[x, y])

    return image


def main():
    image = helpers.load_image("test.png")
    pixels = image.load()
    width, height = image.size
    result = diff_gauss(pixels, width, height)
    helpers.finish(result)


if __name__ == "__main__":
    main()

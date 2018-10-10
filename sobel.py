import PIL.Image
import math
import helpers


h_kernel = [
    [1,  0, -1],
    [2,  0, -2],
    [1,  0, -1]
]


v_kernel = [
    [1,  2,  1],
    [0,  0,  0],
    [-1, -2, -1]
]


def sobel(pixels, width, height):
    result = PIL.Image.new('RGB', (width, height))
    result_pixels = result.load()
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            new_pixel_h = helpers.apply_kernel(pixels, x, y, h_kernel)
            new_pixel_v = helpers.apply_kernel(pixels, x, y, v_kernel)
            new_pixel = int(math.sqrt(new_pixel_h[1]**2 + new_pixel_v[1]**2))
            result_pixels[x, y] = (new_pixel, new_pixel, new_pixel)

    return result


def main():
    image = helpers.load_image("test.png")
    pixels = image.load()
    width, height = image.size

    result = sobel(pixels, width, height)
    helpers.finish(result)


if __name__ == "__main__":
    main()

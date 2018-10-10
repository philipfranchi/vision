import PIL.Image
import helpers


g_kernel = [
    [1, 4, 7, 4, 1],
    [4, 16, 24, 26, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 24, 26, 4],
    [1, 4, 7, 4, 1]
]


def gauss(pixels, width, height, kernel, norm=None):
    if norm is None:
        norm = sum([sum(x) for x in kernel])

    result = PIL.Image.new('RGB', (width, height))
    result_pixels = result.load()

    for y in range(2, height - 2):
        for x in range(2, width - 2):
            result_pixels[x, y] = helpers.apply_kernel(pixels, x, y, kernel, norm=norm)

    return result


def main():
    image = helpers.load_image("test.png")
    pixels = image.load()
    width, height = image.size

    result = gauss(pixels, width, height, g_kernel)
    helpers.finish(result)


if __name__ == "__main__":
    main()

import helpers, palettes


def add_error(color, error):
    return int(color[0] + error), int(color[1] + error), int(color[2] + error)


def compute_error(old_pixel, new_pixel):
    return (old_pixel[0] - new_pixel[0]) + (old_pixel[1] - new_pixel[1]) + (old_pixel[2] - new_pixel[2])


def dither(image, width, height, palette):
    result = image.copy()
    pixels = result.load()

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            old_pixel = pixels[x, y]
            new_pixel = helpers.find_closest_palette_color(old_pixel, palette)
            quant_error = compute_error(old_pixel, new_pixel)

            pixels[x + 1, y] = add_error(pixels[x + 1,  y], quant_error * 7 / 16)
            pixels[x - 1, y + 1] = add_error(pixels[x - 1, y + 1], quant_error * 3 / 16)
            pixels[x, y + 1] = add_error(pixels[x, y + 1], quant_error * 5 / 16)
            pixels[x + 1, y + 1] = add_error(pixels[x + 1, y + 1], quant_error * 1 / 16)
            pixels[x, y] = new_pixel

    return result


def main():
    image = helpers.load_image("test.png")
    width, height = image.size

    result = dither(image, width, height, palettes.sixteen)
    helpers.finish(result, "dither")


if __name__ == "__main__":
    main()

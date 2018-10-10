import PIL.Image
import helpers
import palettes


def closest_color(pixels, width, height, palette):

    result = PIL.Image.new('RGB', (width, height))
    result_pixels = result.load()

    for y in range(height):
        for x in range(width):
            result_pixels[x, y] = helpers.find_closest_palette_color(pixels[x, y], palette)

    return result


def main():
    image = helpers.load_image("test.png")
    pixels = image.load()
    width, height = image.size

    result = closest_color(pixels, width, height, palettes.sixteen)
    helpers.finish(result, "closest")


if __name__ == "__main__":
    main()

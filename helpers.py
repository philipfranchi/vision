import PIL.Image
import math


def load_image(path):
    return PIL.Image.open(path)


def kernel_bounds(l):
    s = -(l//2)
    e = l//2 + 1
    return s, e


def apply_kernel(pixels, x, y, kernel, norm=1):
    pixel_val = [0, 0, 0]
    s, e = kernel_bounds(len(kernel))

    for i in range(s, e, 1):
        for j in range(s, e, 1):
            cur_val = pixels[x + j, y + i]
            kernel_val = kernel[i + (len(kernel) // 2)][j + (len(kernel) // 2)]
            for idx, c in enumerate(cur_val):
                pixel_val[idx] = int((c * kernel_val / norm) + pixel_val[idx])

    return tuple(pixel_val)


def finish(image, name):
    image.save("result.png")
    image.show(title=name)


def distance(c1, c2):
    dist = 0
    for idx in range(len(c1)):
        dist += (c1[idx] - c2[idx])**2

    return math.sqrt(dist)


def subtract(c1, c2):
    return tuple([x-y for x, y in zip(c1, c2)])


def find_closest_palette_color(pixel, palette):
    best_dist = 99999
    best_col = pixel

    for c in palette:
        cur_dist = distance(pixel, c)
        if cur_dist < best_dist:
            best_dist = cur_dist
            best_col = c

    return best_col
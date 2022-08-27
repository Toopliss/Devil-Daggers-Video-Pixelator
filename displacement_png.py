#ORIGINAL: https://gist.github.com/darka/061cfac5e95b80b078b769eaae7adf84
#Modified for the purposes of outputting pixelating displacement map pngs.

import struct
import zlib
import math
from typing import BinaryIO, List, Tuple

Pixel = Tuple[int, int, int]
Image = List[List[Pixel]]

BLACK_PIXEL: Pixel = (0, 0, 0)
WHITE_PIXEL: Pixel = (255, 255, 255)

HEADER = b'\x89PNG\r\n\x1A\n'


def generate_checkerboard_pattern(width: int, height: int) -> Image:
    out = []
    max_val = 128 + (math.floor(width/2) * ((3*width)+1))
    print("max_val = ", max_val, " = 128 + (math.floor(", width/2, ") * (", width+1, "+1))")
    for i in range(height):
        # Generate a single row of white/black pixels
        row = []
        for j in range(width):
            
            bruhX = (max_val-(((3*width)+1)*j))
            bruhY = (max_val-(((3*width)+1)*i))
            row.append((bruhX,bruhY,0))
            print("put pixel at ", i, ", ", j, " with colours ", bruhX, bruhY)
            
        out.append(row)
    return out


def get_checksum(chunk_type: bytes, data: bytes) -> int:
    checksum = zlib.crc32(chunk_type)
    checksum = zlib.crc32(data, checksum)
    return checksum


def chunk(out: BinaryIO, chunk_type: bytes, data: bytes) -> None:
    out.write(struct.pack('>I', len(data)))
    out.write(chunk_type)
    out.write(data)

    checksum = get_checksum(chunk_type, data)
    out.write(struct.pack('>I', checksum))


def make_ihdr(width: int, height: int, bit_depth: int, color_type: int) -> bytes:
    return struct.pack('>2I5B', width, height, bit_depth, color_type, 0, 0, 0)


def encode_data(img: Image) -> List[int]:
    ret = []

    for row in img:
        ret.append(0)

        color_values = [
            color_value
            for pixel in row
            for color_value in pixel
        ]
        ret.extend(color_values)

    return ret


def compress_data(data: List[int]) -> bytes:
    data_bytes = bytearray(data)
    return zlib.compress(data_bytes)


def make_idat(img: Image) -> bytes:
    encoded_data = encode_data(img)
    compressed_data = compress_data(encoded_data)
    return compressed_data


def dump_png(out: BinaryIO, img: Image) -> None:
    out.write(HEADER)  # start by writing the header

    assert len(img) > 0  # assume we were not given empty image data
    width = len(img[0])
    height = len(img)
    bit_depth = 8  # bits per pixel
    color_type = 2  # pixel is RGB triple

    ihdr_data = make_ihdr(width, height, bit_depth, color_type)
    chunk(out, b'IHDR', ihdr_data)

    compressed_data = make_idat(img)
    chunk(out, b'IDAT', data=compressed_data)

    chunk(out, b'IEND', data=b'')


def save_png(img: Image, filename: str) -> None:
    with open(filename, 'wb') as out:
        dump_png(out, img)


if __name__ == '__main__':
    width = 2
    height = 2
    img = generate_checkerboard_pattern(width, height)

    save_png(img, 'out.png')

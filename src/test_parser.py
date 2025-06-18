from parser import Parser


def test_parser():
    byte_codes = [
        b"\x01\x00\x00\x00",
        b"\xff\xff\xff\xff",
        b"\x00\x00\x00\x80",
        b"\xff\xff\xff\x7f",
    ]

    ints = [1, -1, -2147483648, 2147483647]

    parser = Parser()

    for i in range(len(byte_codes)):
        parser.parse_bytes(byte_codes[i])
        assert parser.parsed_bytes == ints[i]

from parser import Parser


def main():
    parser = Parser(b"\xff\xff\xff\x7f")
    parser.parse_bytes()
    print(parser.parsed_bytes)


if __name__ == "__main__":
    main()

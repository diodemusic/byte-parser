class Parser:
    def __init__(self):
        self.byte_code = 0
        self.parsed_bytes = 0

    def parse_bytes(self, byte_code):
        b0 = byte_code[0]
        b1 = byte_code[1] << 8
        b2 = byte_code[2] << 16
        b3 = byte_code[3] << 24

        self.parsed_bytes = b0 + b1 + b2 + b3

        if self.parsed_bytes >= 2**31:
            self.parsed_bytes -= 2**32

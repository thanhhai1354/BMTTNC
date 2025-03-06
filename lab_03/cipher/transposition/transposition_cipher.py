import math

class TranspositionCipher:
    def encrypt_text(self, plain_text, key):
        plain_text = plain_text.replace(" ", "")
        num_cols = len(key)
        num_rows = math.ceil(len(plain_text) / num_cols)
        grid = []
        index = 0
        for r in range(num_rows):
            row = []
            for c in range(num_cols):
                if index < len(plain_text):
                    row.append(plain_text[index])
                    index += 1
                else:
                    row.append("X")
            grid.append(row)
        order = sorted(range(num_cols), key=lambda i: key[i])
        cipher_text = ""
        for c in order:
            for r in range(num_rows):
                cipher_text += grid[r][c]
        return cipher_text

    def decrypt_text(self, cipher_text, key):
        num_cols = len(key)
        num_rows = math.ceil(len(cipher_text) / num_cols)
        L = len(cipher_text)
        num_full_cols = L % num_cols
        if num_full_cols == 0:
            num_full_cols = num_cols
        order = sorted(range(num_cols), key=lambda i: key[i])
        grid = [[''] * num_cols for _ in range(num_rows)]
        index = 0
        for pos, col in enumerate(order):
            col_height = num_rows if pos < num_full_cols else num_rows - 1
            for r in range(col_height):
                grid[r][col] = cipher_text[index]
                index += 1
        plain_text = "".join("".join(row) for row in grid)
        return plain_text.rstrip("X")

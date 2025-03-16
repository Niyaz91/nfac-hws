def build_banner(banner_data, text):

    characters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    ascii_map = {characters[i]: banner_data[i].split("\n") for i in range(len(characters))}

    banner_lines = ['' for _ in range(8)]

    for char in text:
        if char == ' ':
            space_art = ['      ' for _ in range(8)]
            for i in range(8):
                banner_lines[i] += space_art[i] + ' '

        elif char in ascii_map:
            char_art = ascii_map[char]
            for i in range(8):
                banner_lines[i] += char_art[i]

    return "\n".join(banner_lines)

def process_text(text):
    text = text.replace(r"\n\n", "\n")
    text = text.replace(r"\n", "\n")
    return text

from argparse import ArgumentParser


def load_banner_file(filename):
    with open(filename, 'r') as file:
        banner_content = file.read().split("\n\n")
    return banner_content


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

def main():
    filename = "standard.txt"
    standard_banner = load_banner_file(filename)

    parser = ArgumentParser()
    parser.add_argument('text', type=str)
    args=parser.parse_args()

    text = process_text(args.text)

    parts= text.split("\n")

    banner = ""
    for part in parts:
        banner += build_banner(standard_banner, part) + "\n"

    print(banner)


if __name__ == "__main__":
    main()
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    word_count(file_contents)
    character_count(file_contents)
    book_report(file_contents)


def word_count(file_contents):
    words = file_contents.split()
    num_of_words = len(words)
    return num_of_words

def character_count(file_contents):
    char_count_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    lowered_text = file_contents.lower()
    for character in lowered_text:
        if character in char_count_dict:
            char_count_dict[character] += 1
    return char_count_dict

def book_report(file_contents):
    print("========================================")
    print("-- Beginning of report on Frakenstein --")
    print(f"There is a total of {word_count(file_contents)} words in Frankenstein.")
    report_char_count_dict = character_count(file_contents)
    print(f"The letter a appears {report_char_count_dict["a"]} times in the text.")
    print(f"The letter b appears {report_char_count_dict["b"]} times in the text.")
    print(f"The letter c appears {report_char_count_dict["c"]} times in the text.")
    print(f"The letter d appears {report_char_count_dict["d"]} times in the text.")
    print(f"The letter e appears {report_char_count_dict["e"]} times in the text.")
    print(f"The letter f appears {report_char_count_dict["f"]} times in the text.")
    print(f"The letter g appears {report_char_count_dict["g"]} times in the text.")
    print(f"The letter h appears {report_char_count_dict["h"]} times in the text.")
    print(f"The letter i appears {report_char_count_dict["i"]} times in the text.")
    print(f"The letter j appears {report_char_count_dict["j"]} times in the text.")
    print(f"The letter k appears {report_char_count_dict["k"]} times in the text.")
    print(f"The letter l appears {report_char_count_dict["l"]} times in the text.")
    print(f"The letter m appears {report_char_count_dict["m"]} times in the text.")
    print(f"The letter n appears {report_char_count_dict["n"]} times in the text.")
    print(f"The letter o appears {report_char_count_dict["o"]} times in the text.")
    print(f"The letter p appears {report_char_count_dict["p"]} times in the text.")
    print(f"The letter q appears {report_char_count_dict["q"]} times in the text.")
    print(f"The letter r appears {report_char_count_dict["r"]} times in the text.")
    print(f"The letter s appears {report_char_count_dict["s"]} times in the text.")
    print(f"The letter t appears {report_char_count_dict["t"]} times in the text.")
    print(f"The letter u appears {report_char_count_dict["u"]} times in the text.")
    print(f"The letter v appears {report_char_count_dict["v"]} times in the text.")
    print(f"The letter w appears {report_char_count_dict["w"]} times in the text.")
    print(f"The letter x appears {report_char_count_dict["x"]} times in the text.")
    print(f"The letter y appears {report_char_count_dict["y"]} times in the text.")
    print(f"The letter z appears {report_char_count_dict["z"]} times in the text.")
    print("-- End of report on Frankenstein --")
    print("========================================")

main()
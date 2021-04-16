import sys
import re


def delete_empty_lines(content):
    lines = content.split("\n")
    non_empty_lines = ""
    for i in range(len(lines) - 1):
        if lines[i].strip() == "":
            if lines[i - 1] != "\\" and lines[i + 1] != "\\":
                non_empty_lines += lines[i] + "\n"
        else:
            non_empty_lines += lines[i] + "\n"
    return non_empty_lines


def delete_square_brackets_lines(content):
    lines = content.split("\n")
    non_square_brackets_lines = [line for line in lines if "[" not in line]
    content = ""
    for line in non_square_brackets_lines:
        content += line + "\n"
    return content


def delete_parentheses(content):
    result = re.sub(r"\([^()]*\)", "", content)
    return result


def to_array(string):
    array = string.split("\\")
    return array


def create_lyrics_files(file_name):
    try:
        file = open(file_name, "r", encoding="utf8")
    except IOError:
        print('Error: File "', file_name, '" does not appear to exist.')
        return -1
    file_content = file.read()
    lyrics_no_empty_lines = delete_empty_lines(file_content)
    lyrics_parentheses = delete_square_brackets_lines(lyrics_no_empty_lines)
    lyrics_no_parentheses = delete_parentheses(lyrics_parentheses)
    file_parentheses = open("lyrics_parentheses.txt", "w", encoding="utf8")
    file_parentheses.write(lyrics_parentheses)
    file_parentheses.close()
    file_no_parentheses = open("lyrics_no_parentheses.txt", "w", encoding="utf8")
    file_no_parentheses.write(lyrics_no_parentheses)
    file_no_parentheses.close()
    return lyrics_parentheses


def parse(file_name):
    valid_chars = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó',
                   'p', 'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z', '.', '¿', '?', ',', '\'', ':', '¡', '!',
                   ';', '"', "\n"]

    # load ascii text and covert to lowercase
    try:
        raw_text = open(file_name, "r", encoding="utf8").read().lower().replace("--", ";")
    except IOError:
        print('Error: File "', file_name, '" does not appear to exist.')
        return -1

    wordlist = []
    s = ""

    # split the raw text into valid "words" (punctuation are words in this case)
    for i in range(0, len(raw_text)):
        x = i
        # space or return -> store word
        # or raw_text[x] == '\n'
        if raw_text[x] == ' ':
            if len(s) > 0:
                wordlist.append(s)
            s = ""
        # include only valid characters
        elif raw_text[x] in valid_chars:
            if raw_text[x].isalpha():
                s += raw_text[x]
            else:
                # for I'll, don't, alice's, etc...
                especial_valid_chars = ['s', 't', 'm', 'l']
                if raw_text[x] == '\'' and raw_text[x + 1] in especial_valid_chars:
                    s += raw_text[x]
                else:
                    if len(s) > 0:
                        wordlist.append(s)
                    wordlist.append(raw_text[x])
                    s = ""
    return wordlist


def generated_lyric(filename, data):
    file_no_parentheses = open(filename, "w", encoding="utf8")
    file_no_parentheses.write(data)
    file_no_parentheses.close()


# args = sys.argv
# if len(args) == 2:
#    lyrics = create_lyrics_files(args[1])
#   if lyrics != -1:
#       lyrics_array = to_array(lyrics)
#        lyrics_parse = parse(lyrics_array)
# else:
#   print('Error: Incorrect arguments number')

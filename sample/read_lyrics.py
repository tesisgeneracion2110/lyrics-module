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


args = sys.argv
if len(args) == 2:
    lyrics = create_lyrics_files(args[1])
    if lyrics != -1:
        lyrics_array = to_array(lyrics)
else:
    print('Error: Incorrect arguments number')

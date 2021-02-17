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


def create_lyrics_files():
    file = open("lyrics.txt", "r", encoding="utf8")
    file_content = file.read()
    lyrics_no_empty_lines = delete_empty_lines(file_content)
    lyrics_parentheses = delete_square_brackets_lines(lyrics_no_empty_lines)
    lyrics_no_parentheses = delete_parentheses(lyrics_parentheses)
    f = open("lyrics_parentheses.txt", "w", encoding="utf8")
    f.write(lyrics_parentheses)
    f.close()
    f = open("lyrics_no_parentheses.txt", "w", encoding="utf8")
    f.write(lyrics_no_parentheses)
    f.close()
    return lyrics_parentheses


lyrics = create_lyrics_files()
lyrics_array = to_array(lyrics)
print(lyrics_array)

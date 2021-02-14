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


def delete_all_brackets(content):
    result = re.sub(r"\([^()]*\)", "", content)
    return result


def to_array(string):
    array = string.split("\\")
    return array


file = open("lyrics.txt", "r", encoding="utf8")
file_content = file.read()
lyrics = delete_empty_lines(file_content)
lyrics = delete_square_brackets_lines(lyrics)
lyrics_two = delete_all_brackets(lyrics)
f = open("lyrics1.txt", "w", encoding="utf8")
f.write(lyrics)
f.close()
f = open("lyrics2.txt", "w", encoding="utf8")
f.write(lyrics_two)
f.close()
lyrics_array = to_array(lyrics)
print(lyrics_array)

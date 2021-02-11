import re

def delete_empty_lines(content):
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    content = ""
    for line in non_empty_lines:
        content += line + "\n"
    return content


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

def to_array(lyrics):
    array = lyrics.split("\n\n")
    return array

file = open("lyrics.txt", "r", encoding="utf8")
file_content = file.read()
lyrics = delete_empty_lines(file_content)
lyrics = delete_square_brackets_lines(lyrics)
lyrics_one = lyrics.replace("\\", "")
lyrics_two = delete_all_brackets(lyrics_one)
lyrics_three = delete_all_brackets(file_content)
lyrics_three = delete_square_brackets_lines(lyrics_three)
f = open("lyrics1.txt", "w", encoding="utf8")
f.write(lyrics_one)
f.close()
f = open("lyrics2.txt", "w", encoding="utf8")
f.write(lyrics_two)
f.close()
f = open("lyrics3.txt", "w", encoding="utf8")
f.write(lyrics_three)
f.close()

print('Hi')
lyrics_array = to_array(lyrics_one)

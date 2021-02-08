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


file = open("lyrics.txt", "r", encoding="utf8")
file_content = file.read()
lyrics = delete_empty_lines(file_content)
lyrics = delete_square_brackets_lines(lyrics)
lyrics_one = lyrics.replace("\\", "")
lyrics_two = delete_all_brackets(lyrics)
lyrics_three = delete_all_brackets(file_content)
f = open("lyrics1.txt", "w", encoding="utf8")
f.write(lyrics_three)
f.close()

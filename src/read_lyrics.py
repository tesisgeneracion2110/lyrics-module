def delete_empty_lines(content):
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    content = ""
    for line in non_empty_lines:
        content += line + "\n"
    return content


def adapt_lyrics(content):
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if "[" not in line]
    content = ""
    print(non_empty_lines)
    for line in non_empty_lines:
        content += line + "\n"
    return content


file = open("lyrics.txt", encoding="utf8")
file_content = file.read()
lyrics = delete_empty_lines(file_content)
print(lyrics)
adapt_lyrics(lyrics)

# print(file_content)

def emoji_converter(message):

    result = ''
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "☹️",
        ";)": "😉",
        ":'(": "😢"
    }

    for word in words:
        result += emojis.get(word, word) + " "

    return result


message = input(">")
print(emoji_converter(message))
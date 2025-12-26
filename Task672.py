def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

user_text = input("Введіть текст: ")

print(reverse_words(user_text))
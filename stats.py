from operator import itemgetter


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    return len(text.split())


def count_character(text):
    dict_text = {}
    for character in text:
        if character.lower() in dict_text.keys():
            dict_text[character.lower()] += 1
        else:
            dict_text[character.lower()] = 1
    return dict_text


def character_dict_sort(text):
    dict_text = count_character(text)
    character_list = []
    for character, count in dict_text.items():
        character_list.append({
            "character": character,
            "count": count
        })
    return sorted(character_list, key=itemgetter("count"), reverse=True)

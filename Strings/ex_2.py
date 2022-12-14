articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    articles_list = []
    sentence = ''
    for i in articles_dict:
        for j in i:
            # print(i[j])
            if letter_case == False:
                key = key.lower()
                if not isinstance(i[j], int):
                    sentence = i[j].lower()
                    # print(sentence)
            else:
                sentence = i[j]

            if not isinstance(i[j], int):
                if key in sentence and (i not in articles_list):
                    articles_list.append(i)
    # print(articles_list)

    return articles_list
def strings(document):
    with open(document,  encoding='utf8') as f:
        strings = 0
        for line in f:
            strings += 1
        return strings


def right(documents):
    right_name_list = []
    right_dic = {}
    for doc in documents:
       right_dic.setdefault(strings(doc), doc)
    for lines in sorted(right_dic):
        right_name_list.append(right_dic.get(lines))
    return right_name_list


def sorted_doc(doc_list, new_doc):
    right_doc_list = right(doc_list)
    full_text = ''
    for doc in right_doc_list:
        with open(doc, encoding='utf8') as f:
            text = f'{doc}\n{strings(doc)}\n{f.read()}\n'
            full_text += text
    with open(new_doc, 'w', encoding='utf8') as file:
        file.write(full_text)


sorted_doc(['1.txt', '2.txt', '3.txt'], 'sort_doc.txt')






























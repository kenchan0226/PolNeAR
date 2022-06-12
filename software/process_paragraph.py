from polnear import data


def split_to_paragraphs(split):
    article_tokens_paragraphs_splitted = []
    print("dev")
    for article in split:
        print("art")
        annotated_article = article.annotated()
        #annotated_article.tokens[0]["attributions"]
        #annotated_article.tokens[0]["word"]
        all_paragraphs = []
        paragraph_tokens = []
        j = 0
        while j < len(annotated_article.tokens):
            print(j)
            token = annotated_article.tokens[j]
            if token["word"] == "\n" and annotated_article.tokens[j+1]["word"] == "\n":
                all_paragraphs.append(paragraph_tokens)
                paragraph_tokens = []
                j += 2
                continue
            paragraph_tokens.append(token)
            j += 1

        for para in all_paragraphs:
            para_word_list = []
            for token in para:
                para_word_list.append(token["word"])
            print(" ".join(para_word_list))
            print()
        exit()
        article_tokens_paragraphs_splitted.append(all_paragraphs)


def main():
    train = data.train()
    dev = data.dev()
    test = data.test()
    split_to_paragraphs(dev)


if __name__ == "__main__":
    main()

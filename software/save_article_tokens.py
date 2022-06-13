from polnear import data
import pickle as pkl
from tqdm import tqdm


def split_to_paragraphs(split):
    article_all = []
    for article in tqdm(split):
        annotated_article = article.annotated()
        #annotated_article.tokens[0]["attributions"]
        #annotated_article.tokens[0]["word"]
        #article_tokens = [token for token in annotated_article.tokens]
        #article_tokens_all.append(article_tokens)
        article_all.append({"text": article.text, "token_annotations": annotated_article.tokens})
    return article_all


def main(split_name):
    if split_name == "train":
        split = data.train()
    elif split_name == "dev":
        split = data.dev()
    elif split_name == "test":
        split = data.test()
    else:
        raise ValueError
    sample_list = split_to_paragraphs(split)
    with open(split_name, "wb") as f_out:
        pkl.dump(sample_list, f_out)


if __name__ == "__main__":
    for split_name in ["train", "dev", "test"]:
        main(split_name)

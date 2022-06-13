from polnear import data
#import pickle as pkl
from tqdm import tqdm
import json
import io
import codecs


def split_to_paragraphs(split):
    article_all = []
    error_count = 0
    for article in tqdm(split):
        try:
            annotated_article = article.annotated()
            #annotated_article.tokens[0]["attributions"]
            #annotated_article.tokens[0]["word"]
            #article_tokens = [token for token in annotated_article.tokens]
            #article_tokens_all.append(article_tokens)
            attributions_for_sentences = []
            for sent in annotated_article.sentences:
                sent_tokens_annotations = [{"word": token["word"], "attributions": list(token["attributions"])} for token in sent.tokens]
                attributions_for_sentences.append(sent_tokens_annotations)
            #token_annotations = [{"word": token["word"], "attributions": list(token["attributions"])} for token in annotated_article.tokens]
            article_all.append({"text": article.text(), "attributions_for_sentences": attributions_for_sentences})
        except:
            error_count += 1
    print("error count: {}".format(error_count))
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
    sample_list = split_to_paragraphs(split[0:2])
    #io.open('filename', 'w', encoding='utf8')
    #split_name + ".json"
    #with io.open(split_name + ".json", 'w', encoding='utf8') as f_out:
        #json.dump(sample_list, f_out, ensure_ascii=False)
    with open(split_name + "_sent.json", 'w') as f_out:
        json.dump(sample_list, f_out)

if __name__ == "__main__":
    for split_name in ["dev", "train", "test"]:
        main(split_name)

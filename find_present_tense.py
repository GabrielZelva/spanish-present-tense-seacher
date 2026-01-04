import dill
import regex as re

def search(corpus, text_type):

    normal_text_pattern = r"[A-ZÁÉÍÓÚÑ][^.]*\." # This may need to be improved
    preseea_text_pattern = r"[A-Z]{1}:.+\.$" # And this as well 

    present_pattern = r"[a-záéíóúñA-ZÁÉÍÓÚÑ]+((?<!(ad)|(id)|(and))o|(?<!(ab)|(í)|(ar))as|(?<!(ab)|(í)|(ar))a|(?<!(ab)|(í)|(ár))amos|áis|(?<!(ab)|(í)|(ar))an|[^s]es|[^s]e|[^rs]emos|[^r]éis|[^s]en|imos|ís|y){1}$"
    interest = []

    with open("hmm_model.pkl", "rb") as f:
        model_data = dill.load(f)
        tagger = model_data["tagger"]
        vocab = model_data["vocab"]

    if text_type == "normal":

        sentences = re.findall(normal_text_pattern, corpus)

    elif text_type == "preseea":

        sentences = re.findall(preseea_text_pattern, corpus)

    for sentence in sentences:

        tokens = re.findall(r'\w+|[^\w\s]', sentence)

        tokens = [w if w in vocab else "UNK_TOKEN" for w in tokens]
        tagged_tokens = tagger.tag(tokens)

        for token, tag in tagged_tokens:
            if tag == "VERB" and re.fullmatch(present_pattern, token):
                try:
                    if sentence != interest[-1]:
                        interest.append(sentence)

                except IndexError:

                    interest.append(sentence)


    output = "\n".join(interest)

    return output

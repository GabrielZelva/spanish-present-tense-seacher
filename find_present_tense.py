import dill
import regex as re

with open("hmm_model.pkl", "rb") as f:
    model_data = dill.load(f)
    tagger = model_data["tagger"]
    vocab = model_data["vocab"]

original_sentence = "El perro corre por la escalera."
sentence = re.findall(r'\w+|[^\w\s]', original_sentence)

sentence = [w if w in vocab else "UNK_TOKEN" for w in sentence]
tagged_sentence = tagger.tag(sentence)

interest = []

pattern = r"[a-záéíóúñA-ZÁÉÍÓÚÑ]+((?<!(ad)|(id)|(and))o|(?<!(ab)|(í)|(ar))as|(?<!(ab)|(í)|(ar))a|(?<!(ab)|(í)|(ár))amos|áis|(?<!(ab)|(í)|(ar))an|[^s]es|[^s]e|[^rs]emos|[^r]éis|[^s]en|imos|ís|y){1}$"

for token, tag in tagged_sentence:
    if tag == "VERB":
        if re.fullmatch(pattern, token):

            interest.append(original_sentence)

print(interest)

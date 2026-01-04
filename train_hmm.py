import numpy as np
from conllu import parse
import nltk
from nltk.tag import hmm
from collections import Counter
import dill
from sklearn.metrics import classification_report, f1_score

def preprocess_data(sentences, vocab = None, threshold = 1):
    data = []
    
    if vocab is None:
        all_words = []
        for sentence in sentences:
            for token in sentence:
                all_words.append(token["form"])
        
        word_counts = Counter(all_words)
        vocab = {word for word, count in word_counts.items() if count > threshold}
        vocab.add("UNK_TOKEN")  
    
    for sentence in sentences:
        sent_pairs = []
        for token in sentence:
            word = token["form"]
            tag = token["upos"]
            
            if word not in vocab:
                word = "UNK_TOKEN"
            
            sent_pairs.append((word, tag))
        data.append(sent_pairs)
    
    return data, vocab

def load_treebank(path):
    with open(path, "r", encoding="utf8") as f:
        data = f.read()
    sentences = parse(data)
    return sentences

train_sentences = load_treebank("data/es_ancora-ud-train.conllu")
train_data, vocab = preprocess_data(train_sentences, vocab = None, threshold = 1)

trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_data)

test_sentences = load_treebank("data/es_ancora-ud-test.conllu")
test_data, _ = preprocess_data(test_sentences, vocab = vocab, threshold = 1)

new_sentence = ["El", "perro", "corre", "."]

new_sentence_processed = [w if w in vocab else "UNK_TOKEN" for w in new_sentence]
predicted_tags = tagger.tag(new_sentence_processed)
print(predicted_tags)

accuracy = tagger.accuracy(test_data)
print(f"Accuracy: {accuracy:.4f}")

all_gold_tags = []
all_pred_tags = []

for sentence in test_data:
    words = [word for word, tag in sentence]
    gold_tags = [tag for word, tag in sentence]

    pred_tags = [tag for word, tag in tagger.tag(words)]

    all_gold_tags.extend(gold_tags)
    all_pred_tags.extend(pred_tags)

verb_f1 = f1_score(all_gold_tags, all_pred_tags, labels=['VERB'], average='micro')
print(f"F1 for VERB: {verb_f1:.4f}")

# Save
with open("hmm_model.pkl", "wb") as f:
    dill.dump({"tagger": tagger, "vocab": vocab}, f)

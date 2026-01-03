import requests


for split in ["train", "dev", "test"]:

    url = f"https://raw.githubusercontent.com/UniversalDependencies/UD_Spanish-AnCora/b72525824c1988b7abe6b91a17eef0a88d79753a/es_ancora-ud-{split}.conllu"
    response = requests.get(url)

    with open(f"data/es_ancora-ud-{split}.conllu", "wb") as f:
        f.write(response.content)

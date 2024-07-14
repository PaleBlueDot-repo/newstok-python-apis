from transformers import pipeline


# Load the model and tokenizer
MODEL = "jy46604790/Fake-News-Bert-Detect"
clf = pipeline("text-classification", model=MODEL, tokenizer=MODEL)

def indentify_fake_news(text):
    result = clf(text)

    return result
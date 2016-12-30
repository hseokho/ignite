def clean_text(name):
    name = name.replace("-", " ").replace(",", " ").replace("-", " ").replace("/", " ").replace("(", " ").replace(")", " ")
    name = name.replace('. ', " ").lower()
    return ' '.join(name.split())

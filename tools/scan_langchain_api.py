import langchain
import os

root = langchain.__path__[0]
print('langchain root:', root)
keywords = ['ChatOpenAI', 'ChatOpenAI(', 'class ChatOpenAI', 'OpenAI(' ,'class OpenAI', 'chat_models.openai']
matches = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if not fn.endswith('.py'):
            continue
        path = os.path.join(dirpath, fn)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                txt = f.read()
        except Exception:
            continue
        for kw in keywords:
            if kw in txt:
                matches.append((path, kw))
                break

if not matches:
    print('No matches for keywords in langchain package files')
else:
    print('Matches found:')
    for p,kw in matches:
        print(p, '->', kw)

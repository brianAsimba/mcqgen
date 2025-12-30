import importlib
import sys

def try_import(path):
    try:
        mod = importlib.import_module(path)
        names = [n for n in dir(mod) if 'Chat' in n or 'OpenAI' in n]
        print('OK', path, '->', names[:20])
    except Exception as e:
        print('ERR', path, '->', e)

def main():
    try:
        import langchain
        print('langchain version:', getattr(langchain, '__version__', 'unknown'))
    except Exception as e:
        print('Failed to import langchain:', e)
        sys.exit(1)

    import os
    root = langchain.__path__[0]
    print('langchain package dir:', root)
    try:
        print('langchain package contents:', os.listdir(root))
    except Exception as _:
        pass

    paths = [
        'langchain.chat_models',
        'langchain.chat_models.openai',
        'langchain.chat_models.azure_openai',
        'langchain.llms',
    ]
    for p in paths:
        try_import(p)

    # Attempt direct imports
    try:
        from langchain.chat_models.openai import ChatOpenAI
        print('Imported ChatOpenAI from langchain.chat_models.openai')
    except Exception as e:
        print('Could not import ChatOpenAI from langchain.chat_models.openai:', e)

    try:
        from langchain.chat_models import ChatOpenAI
        print('Imported ChatOpenAI from langchain.chat_models')
    except Exception as e:
        print('Could not import ChatOpenAI from langchain.chat_models:', e)

if __name__ == '__main__':
    main()

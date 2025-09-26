import tiktoken

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

tokens = encoding.encode("this is a test for tiktoken.")
print(len(tokens))
print(tokens)
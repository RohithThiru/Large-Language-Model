from src.tokenizer.tokenizer import Tokenizer


text = "hello world"

tokenizer = Tokenizer()

tokenizer.train(text)

encoded = tokenizer.encode("hello")
decoded = tokenizer.decode(encoded)
assert decoded == "hello"

print("Vocabulary:", tokenizer.char_to_id)
print("Encoded:", encoded)
print("Decoded:", decoded)
print("Vocabulary size:", tokenizer.vocab_size())
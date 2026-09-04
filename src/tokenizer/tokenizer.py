class Tokenizer:

    def __init__(self):
        self.char_to_id = {}
        self.id_to_char = {}

    def train(self, text):
        characters = sorted(set(text))

        for index, character in enumerate(characters):
            self.char_to_id[character] = index
            self.id_to_char[index] = character

    def encode(self, text):
        return [self.char_to_id[character] for character in text]

    def decode(self, tokens):
        return "".join(self.id_to_char[token] for token in tokens)

    def vocab_size(self):
        return len(self.char_to_id)
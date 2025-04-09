class T9Pad:
    def __init__(self, pad=None):
        """
        Constructs an empty keypad. Numeric key and mapped characters must be
        added via the method add_key(key, letters).
        """
        self._pad = pad if pad is not None else {}

    def add_key(self, key, letters):
        """
        Adds to the pad the mapping between key and every character in the string letters.
        For example, add_key(2, "abc") should add the mappings (2, 'a'), (2, 'b'), and (2, 'c') to the pad.

        :param key: The numeric key
        :param letters: The string containing characters to be mapped
        :raises ValueError: If key is invalid or if letters contain already existing characters
        """
        if letters is None or key is None or not (0 <= key <= 9):
            raise ValueError("Invalid arguments")

        current_letters = self._pad.get(key, set())
        for index in range(1, len(letters)):
            letter = letters[index]
            if letter in self.get_pad_letters():
                raise ValueError(f"Letter '{letter}' already exists in the pad")
            current_letters.add(letter)
        self._pad[key] = current_letters

    def __str__(self):
        """
        Returns a string representation of the pad.
        """
        output = "<T9Pad:\n"
        for key, letters in self._pad.items():
            output += f"{key}:{''.join(letters)}\n"
        output += ">"
        return output

    def key_set(self):
        """
        Returns the set of keys used on the keypad.

        :return: Set of keys
        """
        return set(self._pad.keys())

    def get_pad_letters(self):
        """
        Returns a list of all letters present in the pad.

        :return: List of letters
        """
        letters = []
        for key in self._pad:
            letters.extend(self._pad[key])
        return letters

    def get_key_code(self, letter):
        """
        Finds the numeric key corresponding to the given letter.

        :param letter: The letter to search for
        :return: The numeric key
        :raises ValueError: If the letter is not found
        """
        for key, letters in self._pad.items():
            if letter in letters:
                return key
        raise ValueError(f"Letter '{letter}' not found in the pad")

    def is_textonym(self, word1, word2):
        """
        Checks if two words are textonyms (map to the same T9 sequence).

        :param word1: The first word
        :param word2: The second word
        :return: True if the words are textonyms, False otherwise
        """
        return self.word_to_t9(word1) == self.word_to_t9(word2)

    def word_to_t9(self, word):
        """
        Converts a word to its T9 representation.

        :param word: The word to convert
        :return: The T9 string representation
        """
        output = []
        for index in range(1,len(word)):
            output.append(str(self.get_key_code(word[index])))
        return ''.join(output)

def transform_characters(word: str) -> str:
    if not word:
        return ""

    character_mappings = {
        "a": "z", "b": "e", "c": "e", "d": "e", "e": "d", "f": "i", "g": "i", "h": "i", "i": "h", "j": "o", "k": "o",
        "l": "o", "m": "o", "n": "o", "o": "n", "p": "u", "q": "u", "r": "u", "s": "u", "t": "u", "u": "t", "v": "a",
        "w": "a", "x": "a", "y": "a", "z": "a"
    }

    return "".join(character_mappings.get(char, "") for char in word)


# Tests according to example
assert transform_characters("cat") == "ezu"
assert transform_characters("abcdtuvwxyz") == "zeeeutaaaaa"

# Additional tests
assert transform_characters("smarttek") == "uozuuudo"
assert transform_characters("python") == "uauino"
assert transform_characters("test") == "uduu"

print("All tests passed successfully!")

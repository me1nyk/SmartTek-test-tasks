def alphabetical_order(word: str) -> str:
    if len(word) == 0:
        return ""

    replacements = {
        "a": "z", "b": "e", "c": "e", "d": "e", "e": "d", "f": "i", "g": "i", "h": "i", "i": "h", "j": "o", "k": "o",
        "l": "o", "m": "o", "n": "o", "o": "n", "p": "u", "q": "u", "r": "u", "s": "u", "t": "u", "u": "t", "v": "a",
        "w": "a", "x": "a", "y": "a", "z": "a"
    }

    return "".join(replacements[char] for char in word)


# Tests according to example
assert alphabetical_order("cat") == "ezu"
assert alphabetical_order("abcdtuvwxyz") == "zeeeutaaaaa"

# Additional tests
assert alphabetical_order("smarttek") == "uozuuudo"
assert alphabetical_order("python") == "uauino"
assert alphabetical_order("test") == "uduu"

print("All tests passed successfully!")

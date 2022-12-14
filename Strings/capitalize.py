from string import ascii_lowercase, ascii_uppercase

# TODO: Need to capitalize first letter of each sentence, not first letter of input.
def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word.
    """
    if not sentence:
        return ""
    lower_to_upper = {lc: uc for lc, uc in zip(ascii_lowercase, ascii_uppercase)}
    return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]

if __name__ == "__main__":
    from doctest import testmod
    testmod()
import re

def convert_to_salted(text: str) -> str:
    """
    Converts text from Russian into so called salted language

    Arguments:
        text(str): path to the input file

    Returns:
        str: converted text
    """
    vowels = r"[аеёиоуыэюяАЕЁИОУЭЮЯ]"

    def replace_vowel(match):
        vowel = match.group()
        return(vowel + 'с' + vowel)
    return(re.sub(vowels, replace_vowel, text))

def char_replacer(input, char_to_replace, replace_char):
    """Replaces char_to_replace with replace_char every time it appears in input."""

    output = ""
    for i in input:
        if i == char_to_replace:
            output += replace_char
        else:
            output += i

    return output

def halopediaLinkBuilder(input):
    """Takes the full name of a Halo game and turns it into a string that can be inserted
        into a Halopedia link after https://halopedia.org/
        
    """
    return char_replacer(input, " ", "_")


# Dealing with dates

def print_date(month, day, year):
    print(f"{month}\\{day}\\{year}")

# Dealing with user input
def clean_input(input):
    return input.strip()

def get_code():
    return clean_input(input())

import helper

# Maps Halo game codes to the names of the games
halo_names = {
    "1" : "Halo: Combat Evolved",
    "2" : "Halo 2",
    "3" : "Halo 3",
    "4" : "Halo 4",
    "R" : "Halo Reach",
    "5" : "Halo 5",
    "1A" : "Halo CE Anniversary",
    "2A" : "Halo 2 Anniversary",
    "I" : "Halo Infinite"
}

# Maps Halo game codes to their release dates
# As a tuple (MM, DD, YYYY)
halo_release_dates = {
    "1" : (11, 15, 2001),
    "2" : (11, 9, 2004),
    "3" : (9, 25, 2007),
    "4" : (11, 6, 2012),
    "5" : (11, 27, 2015),
    "R" : (9, 14, 2010),
    "1A" : (11, 15, 2011),
    "2A" : (11, 11, 2014),
    "I" : (12, 8, 2021)  
}

def check_code_valid(code):
    """Returns a boolean of whether or not the passed string is in the keys of halo_names"""
    return code in halo_names.keys()

def print_keys():
    """Prints all the keys in halo_names dict"""
    for key in halo_names.keys():
        print(key, end = " ")
    print()

# Prints the info about a Halo game based on a code being inputted
def printhalo(code):
    """Prints info about a Halo game and a Halopedia link based on a code that is passed to it."""

    # Print name
    print(f"{halo_names[code]}")

    # Print release date
    month, day, year = halo_release_dates[code]
    print("Released ", end = "")
    helper.print_date(month, day, year)

    # Print Halopedia link
    print(f"https://halopedia.org/{helper.halopediaLinkBuilder(halo_names[code])}")

# Testing this module
if(__name__ == "__main__"):
    code = input()
    print(check_code_valid(code))
    printhalo(code)




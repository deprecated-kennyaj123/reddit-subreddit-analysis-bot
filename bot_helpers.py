# This module contains methods that are either too clunky or niche for the main py file


def simplify_ratio(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return numer, denom, reduced_num
    elif common_divisor == 1:
        return numer, denom
    else:
        return reduced_num, reduced_den


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a


def keyword_count(keyword, the_comments):
    """Returns the number of comments in @p the_comments contain the @p keyword"""
    count = 0
    for comment in the_comments:
        if keyword.lower() in comment.body.lower():
            count += 1
    return count


def get_keywords_from_stupid_txt_file(file_name):
    """Gets the keywords from a stupid text file I made. You can largely ignore"""
    result = []
    with open(file_name) as file:
        for line in file:
            sep_index02 = line.rfind(' ')
            result.append(line[:sep_index02])
    return result


def get_keywords_from_file(file_name):
    """Gets keywords from txt file
    :precondition: each keyword is on a separate line
    """
    with open(file_name) as file:
        results = [line for line in file]
        return results


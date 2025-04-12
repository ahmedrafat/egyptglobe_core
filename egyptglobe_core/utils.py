import re

def scrub_fallback(text):
    """
    Converts a string to lowercase and replaces non-alphanumeric characters
    with underscores. A safe alternative to frappe's scrub function.
    """
    return re.sub(r'\W+', '_', text.strip().lower())
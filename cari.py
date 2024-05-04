def display_search_form():
    search_form = """
    +--------------------------------+
    |         Search Form             |
    +--------------------------------+
    | Search for: [keyword]          |
    | Press 'Enter" to submit.        |
    +--------------------------------+
    """
    print(search_form)

def handle_input():
    user_input = input("cari > ").strip()
    if user_input.lower() == "cari":
        display_search_form()
    else:
        print(f"You entered: {user_input}")

# Example usage
handle_input()
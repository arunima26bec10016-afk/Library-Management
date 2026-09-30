# validation.py
# Small helper functions to make sure the user types proper input


def get_text(prompt):
    # keeps asking until the user types something (not blank)
    while True:
        text = input(prompt).strip()
        if text == "":
            print("This can't be empty. Try again.")
        else:
            return text


def get_number(prompt, allow_zero=False):
    # keeps asking until the user types a whole number
    while True:
        text = input(prompt).strip()
        if not text.isdigit():
            print("Please enter a number (digits only).")
            continue
        number = int(text)
        if number == 0 and not allow_zero:
            print("Number must be more than 0.")
            continue
        return number

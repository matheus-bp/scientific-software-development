# print a hello world message in english or in portuguese


def hello_world(language="en"):
    """
    Print a hello world message in the specified language.
    Supported languages: 'en' for English, 'pt' for Portuguese.
    Args:
        language (str): The language code for the message. Default is 'en'.
    Returns:
        None
    """
    if language == "en":
        print("Hello, World!")
    elif language == "pt":
        print("Olá, Mundo!")
    else:
        print("Language not supported.")

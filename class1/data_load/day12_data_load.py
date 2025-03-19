import os


def load_text_data(filepath: str):
    """
    Loads text data from a text file.
    filepath: str
        Path to the file
    """
    if not os.path.exists(filepath):
        content = ""
        # log
        status = False
    else:
        with open(filepath, "r") as file:
            content = file.read()
            status = True
    return status, content

    # try:
    #     with open(filepath, "r") as file:
    #         content = file.read()
    #     status = True
    # except FileNotFoundError as e:
    #     content = ""
    #     status = False

    # return status, content


def load_excel_data(filepath: str):
    return ""

"""Functions that may not be appropiate to put in server.py"""

import requests

def get_language_options() -> list[str]:
    """Get all of the languages available in bible.com

    Returns:
        list[str]: A list of the available languages in ISO-639-3 format
    """
    languages = requests.get("https://www.bible.com/api/bible/configuration")
    langs = languages.json()
    lang_versions = langs["response"]["data"]["default_versions"]

    def gen_name(lang_version):
        local_name = lang_version["local_name"]
        name = lang_version["name"]
        return local_name if local_name == name else f"{local_name} ({name})"

    prompt_options = {gen_name(x): x["iso_639_3"] for x in lang_versions }
    return prompt_options.values()

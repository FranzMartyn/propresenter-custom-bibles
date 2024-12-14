"""Functions that may not be appropiate to put in server.py"""

import os

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


# Partially copied from bible_import.move_rvbible_propresenter_folder
def get_sideload_folder():
    if system_str == 'Windows':
        program_data = os.getenv('PROGRAMDATA')
        propresenter_bible_location = os.path.join(program_data,
                                                   'RenewedVision\ProPresenter\Bibles\sideload')
        os.makedirs(propresenter_bible_location, exist_ok=True)
    elif system_str == 'Darwin':
        propresenter_bible_location = '/Library/Application Support/RenewedVision/RVBibles/v2/'
    return propresenter_bible_location

import tkinter
from tkinter import ttk
import json

import bible_import
import requests


def get_language_options() -> list[str]:
    languages = requests.get("https://www.bible.com/api/bible/configuration")
    langs = languages.json()
    lang_versions = langs["response"]["data"]["default_versions"]

    def gen_name(lang_version):
        local_name = lang_version["local_name"]
        name = lang_version["name"]
        return local_name if local_name == name else f"{local_name} ({name})"

    prompt_options = {gen_name(x): x["iso_639_3"] for x in lang_versions }
    return list(prompt_options.values())

LANGUAGE_OPTIONS = get_language_options()


COMBOBOX_WIDTH = 35
PADDING = 5
PADDING_LEFT = 10

window = tkinter.Tk()
window.title("Bible import")
window.geometry("400x200")

lbl_languages = tkinter.Label(text="Language:")
lbl_languages.grid(column=0, row=0)

langs_string = tkinter.StringVar()
cmb_languages = ttk.Combobox(width=COMBOBOX_WIDTH, textvariable=langs_string)
cmb_languages.grid(padx=(PADDING, PADDING), pady=(PADDING_LEFT, PADDING),
                   column=1, row=0)
cmb_languages["values"] = sorted(LANGUAGE_OPTIONS)

def cmb_languages_changed(event: tkinter.Event, idk: str, permissions: str):
    print("translation combobox changed")
    if langs_string.get() not in LANGUAGE_OPTIONS:
        cmb_translations.set("")
        return
    available_bibles = bible_import.retrieve_bibles_for_language(langs_string.get())
    values = [f"{x['id']}: {x['local_title']} ({x['local_abbreviation']})" for x in available_bibles.values()]
    cmb_translations["values"] = values
    cmb_translations.set(values[0])

langs_string.trace_add("write", cmb_languages_changed)

lbl_translations = tkinter.Label(text="Bible translations:")
lbl_translations.grid(padx=(PADDING, PADDING), pady=(PADDING_LEFT, PADDING),
                      column=0, row=1)

translation_string = tkinter.StringVar()
cmb_translations = tkinter.ttk.Combobox(width=COMBOBOX_WIDTH, textvariable=translation_string)
cmb_translations.grid(padx=(PADDING, PADDING), pady=(PADDING, PADDING),
                      column=1, row=1)

def btn_install_click():
    print("Installing bibles... (not really)")

btn_install = tkinter.Button(master=window, text="Install translation",
                             command=btn_install_click)
btn_install.grid(padx=(PADDING, PADDING), pady=(PADDING_LEFT, PADDING),
                 column=0, row=5)


if __name__ == "__main__":
    try:
        window.mainloop()
    except KeyboardInterrupt:
        exit(0)

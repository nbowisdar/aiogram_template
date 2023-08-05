import json

from src.config import language_file_path

with open(language_file_path, "r", encoding="utf-8") as f:
    translations = json.load(f)
    # triggers = {}
    # for lang_k, btn_dict in translations["buttons"].items():
    #     for key, value in btn_dict.items():
    #         if key in triggers.keys():
    #             triggers[key].extend(value)
    #         else:
    #             triggers[key] = value
    # print(triggers)
    # triggers = [t for t in translations["buttons"].values()]

import logging
import playsound
import json
import os

logging.basicConfig(filename='logging.log', filemode='w', format='%(asctime)s - %(message)s')


def get_input(text):
    inp = input(text)
    if inp == 'c' or inp == 'n':
        return inp
    else:
        return get_input("Please insert correct answer('n' or 'c')\n")


try:
    path = "audiofiles"
    files = os.listdir(path)
    export_data = {}
    for i in files:
        file = path + "/" + i
        print("Please listen to audio till the end")
        playsound.playsound(file)
        export_data[file] = get_input("If the audio was noisy type-'n', if it was clear-'c'\n")
    with open("audiodata.json", "w") as outfile:
        json.dump(export_data, outfile, ensure_ascii=False, indent=4)
except Exception as e:
        logging.error(e)


print("Thank you!")

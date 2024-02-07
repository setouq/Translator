from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def translate_text():
    src_lang = source_lang_combo.get()
    dest_lang = dest_lang_combo.get()
    text_to_translate = source_text.get(1.0, END).strip()

    if text_to_translate:
        translator = Translator()
        translated_text = translator.translate(text_to_translate, src=src_lang, dest=dest_lang).text
        dest_text.delete(1.0, END)
        dest_text.insert(END, translated_text)
    else:
        dest_text.delete(1.0, END)
        dest_text.insert(END, "Please enter text to translate.")


root = Tk()
root.title("Google Translator")
root.geometry("500x600")
root.config(bg="#F0F0F0")

# Header
header_label = Label(root, text="Google Translator", font=("Helvetica", 24, "bold"), bg="#F0F0F0")
header_label.pack(pady=20)

# Source Text
source_label = Label(root, text="Source Text:", font=("Helvetica", 14), bg="white")
source_label.pack()
source_text = Text(root, font=("Helvetica", 12), height=6, width=50)
source_text.pack()

# Source Language
source_lang_label = Label(root, text="Source Language:", font=("Helvetica", 14), bg="#F0F0F0")
source_lang_label.pack(pady=10)
source_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Helvetica", 12), state="readonly",
                                 width=20)
source_lang_combo.set("english")
source_lang_combo.pack()

# Destination Language
dest_lang_label = Label(root, text="Destination Language:", font=("Helvetica", 14), bg="#F0F0F0")
dest_lang_label.pack(pady=10)
dest_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Helvetica", 12), state="readonly",
                               width=20)
dest_lang_combo.set("kannada")
dest_lang_combo.pack()

# Translate Button
translate_button = Button(root, text="Translate", font=("Helvetica", 14), relief=RAISED, command=translate_text)
translate_button.pack(pady=20)

# Destination Text
dest_label = Label(root, text="Translated Text:", font=("Helvetica", 14), bg="white")
dest_label.pack()
dest_text = Text(root, font=("Helvetica", 12), height=6, width=50)
dest_text.pack()

root.mainloop()

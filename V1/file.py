import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import Text


def saveAsFile(text):
    newFile = open("splitted_file.txt", 'w')
    newFile.write(text)
    newFile.close()
    messagebox.showinfo("Sentence Splitter",
                        "Sentence splitted and saved as file. Thank you.")


def splitText(text, inputValue):
    new_input = ""
    for i, letter in enumerate(text):
        if i % int(inputValue) == 0:
            new_input += '\n'
        new_input += letter

    new_input = new_input[1:]
    saveAsFile(new_input)


def readFile(filename, inputValue):
    f = open(filename, 'r')
    text = f.read()
    splitText(text, inputValue)
    f.close()


def buttonHandler(inputValue):
    filename = askopenfilename()
    readFile(filename, inputValue)


def retrieve_input():
    inputValue = textBox.get("1.0", "end-1c")
    buttonHandler(inputValue)


window = tk.Tk()
window.geometry('400x200')
window.title("Sentence Splitter")

textBox = Text(window, height='1', width='20')
textBox.pack(padx=15, pady=10)

button = tk.Button(window, text="Select file",
                   command=lambda: retrieve_input(), bg='blue', height="1", width="20", justify='center', fg='white')

button.pack(padx=15, pady=5)

window.mainloop()

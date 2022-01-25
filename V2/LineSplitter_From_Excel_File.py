#!/usr/bin/python3
import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename
from tkinter import Label, messagebox
from tkinter import Text
import xlsxwriter
import xlrd


def splitText(text, inputValue):
    new_line = ""
    fullString = ""

    count = 0
    for i, letter in enumerate(text):
        if i % inputValue == 0:
            if count != 0:
                new_line += "<br>"
                new_line = new_line.strip()

                if new_line[0] == ',':
                    temp = list(new_line)
                    temp[0] = ""
                    new_line = "".join(temp)

                if new_line[len(new_line)-1] == ',':
                    temp = list(new_line)
                    temp[len(new_line)-1] = ""
                    new_line = "".join(temp)

                fullString += new_line.strip()
                new_line = ""
            count += 1
        new_line += letter
    fullString += new_line

    return fullString


def readFile(filename, inputValue):

    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows

    finalOutput = xlsxwriter.Workbook('SplittedTextFileOutput.xlsx')
    finalSheet = finalOutput.add_worksheet()
    outputRow = 0

    for row_idx in range(0, rows):
        rowvalue = (sheet.cell(row_idx, 0)).value
        splittedTex = splitText(rowvalue, inputValue)
        finalSheet.write(outputRow, 0, splittedTex)
        outputRow += 1

    finalOutput.close()
    messagebox.showinfo("Success",
                        "Sentence splitted and saved as file named 'SplittedTextFileOutput.xlsx'. Thank you.")


def buttonHandler(inputValue):
    filename = askopenfilename()
    readFile(filename, inputValue)


def retrieve_input(textBox):
    inputValue = textBox.get("1.0", "end-1c")
    if(inputValue == ""):
        messagebox.showinfo("Invalid Input",
                            "Input is invalid. Please type correct input and try again")
    else:
        try:
            val = int(inputValue)
            buttonHandler(val)
        except ValueError:
            messagebox.showinfo("Invalid Input",
                                "Input is not integer. Please type correct input and try again")


def main():
    window = tk.Tk()
    window.geometry('400x130')
    window.resizable(False, False)
    window.title("Sentence Splitter")

    tk.Label(window,
             text="Enter No. of characters: ", font="Helvetica 14 bold").pack()

    textBox = Text(window, height='2', width='30', font="14")
    textBox.pack(padx=15, pady=5)

    button = tk.Button(window, text="Select xlsx file",
                       command=lambda: retrieve_input(textBox), bg='blue', height="1", width="20", justify='center', fg='white')

    button.pack(padx=15, pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()

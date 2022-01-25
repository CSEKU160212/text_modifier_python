import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename
from tkinter import Label, messagebox
from tkinter import Text
import xlsxwriter
import xlrd
from datetime import datetime


def textNormalization(text):
    text = text.replace(",", " , ")
    text = text.replace(".", " . ")
    return text


def outputNormalization(text):
    newLine = text.replace(" .", ".")
    newLine = text.replace(". ", ".")
    newLine = newLine.replace(" ,", ",")
    newLine = newLine.replace(", ", ",")
    newLine = newLine.replace(" ;", ";")
    newLine = newLine.replace(" :", ":")
    newLine = newLine.replace(" <br>", "<br>")
    newLine = newLine.replace(",<br>", "<br>")
    newLine = newLine.replace("<br>,", "<br>")
    newLine = newLine.replace("<br> ", "<br>")
    return newLine


def splitText(text, inputValue):
    textAsList = textNormalization(text).split()
    newLine = ""
    currentLength = 0

    for word in textAsList:
        currentLength = currentLength+len(word)
        if(currentLength <= inputValue):
            newLine += word
        else:
            newLine += "<br>"+word
            currentLength = len(word)
        newLine += " "
        currentLength += 1

    return outputNormalization(newLine)


def readFile(filename, inputValue):

    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows

    OUTPUTFILE_NAME = "Formated_output_"+datetime.now().strftime(
        "%d-%m-%Y_%H-%M-%S")+".xlsx"

    finalOutput = xlsxwriter.Workbook(OUTPUTFILE_NAME)
    finalSheet = finalOutput.add_worksheet()
    outputRow = 0

    for row_idx in range(0, rows):
        rowvalue = (sheet.cell(row_idx, 0)).value
        splittedTex = splitText(rowvalue, inputValue)
        finalSheet.write(outputRow, 0, splittedTex)
        outputRow += 1

    finalOutput.close()
    messagebox.showinfo("Success",
                        "Sentence splitted and saved as file named "+OUTPUTFILE_NAME+". Thank you.")


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
    window.title("SENTENCE FORMATTER")

    tk.Label(window,
             text="Enter No. of characters: ", font="Helvetica 12 bold").pack()

    textBox = Text(window, height='2', width='30', font="14",
                   background="white", foreground="black")
    textBox.pack(padx=15, pady=5)

    button = tk.Button(window, text="Select xlsx file",
                       command=lambda: retrieve_input(textBox), bg='blue', height="1", width="20", justify='center', fg='white')

    button.pack(padx=15, pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()

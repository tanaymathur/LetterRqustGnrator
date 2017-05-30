__author__ = 'knight'
import fileinput

fileInput='test.java'
textToSearch='public static void '
textToReplace='private void main'

with fileinput.FileInput(fileInput, inplace=True) as file:
    for line in file:
        print(line.replace(textToSearch, textToReplace), end='')
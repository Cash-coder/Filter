# without this when you open FILTER_OUTPUT file and want to check an ebay product, you have to select the cell, enter, copy, search in google.
# this puts a link, blue text, instead of plain text, so now you click and go to the link

# you have to open the target file
# set the cursor in the 1º cell you want to activate
# run this code
# back to the file with Alt Sh, so the cursor drops in the 1º cell you want to activate
# stop with Cn+C


import pyautogui


def activate_cell():

    pyautogui.press('f2')
    pyautogui.press('enter')


# for _ in range(10):
while True:
    activate_cell()

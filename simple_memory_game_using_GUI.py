import PySimpleGUI as gui
from random import randint
from time import sleep

# Function to get the game difficulty settings
def getDifficulty():
    layout = [
        [gui.Text("Speed:")],
        [gui.Radio("Easy","DiffRadio"),gui.Radio("Medium","DiffRadio",default=True),gui.Radio("Hard","DiffRadio"),gui.Radio("Extreme","DiffRadio")],
        [gui.Text("Initial Size:")],
        [gui.Slider(range=(1,100),default_value=5,orientation='h',size=(50,10))],
        [gui.OK()]
    ]

    window = gui.Window("Difficulty", layout, keep_on_top=True, font=(None, 15))
    event , values = window.read()
    window.close()

    if values[0]: return (2.00, values[4])
    if values[1]: return (1.00, values[4])
    if values[2]: return (0.50, values[4])
    if values[3]: return (0.25, values[4])

# Function to display a number in the grid
def showNumber():
    global pos, nums, window
    window[pos]('')
    pos = 'box'+ randNum()
    newNumber = randDigit()
    nums.append(newNumber)
    window[pos](newNumber)


# Function to display numbers for a certain amount of time
def showTime(window,sec,limit):
    
    if limit == 0:
        return
    
    showNumber()
    window.finalize()
    sleep(sec)
    showTime(window,sec,limit-1)

# Generate a random two-digit number as a string
def randNum():
    return str(randint(0, 99))

# Generate a random single-digit number as a string
def randDigit():
    return str(randint(0, 9))

# Disable GUI controls
def disableControls(window):
    window["Quit"].Update(disabled=True)
    window["OK"].Update(disabled=True)
    window["input"].Update(disabled=True)


# Enable GUI controls
def enableControls(window):
    window["Quit"].Update(disabled=False)
    window["OK"].Update(disabled=False)
    window["input"].Update(disabled=False)

# Set the PySimpleGUI theme
gui.ChangeLookAndFeel('Dark Amber')



# Create the layout for the grid of Text elements
layout = [[gui.Text('PYTHON MEMORY GAME')]]

for row in range(10):
    row_layout = []
    for col in range(10):
        text_key = f'box{row * 10 + col}'
        row_layout.append(gui.Text(' ', key=text_key, size=(5, 1), pad=(1, 10)))
    layout.append(row_layout)

layout += [
    [gui.Text('Press START to begin', pad=(1, 10), key="info", size=(50, 1))],
    [gui.In(size=(40, 1), disabled=True, background_color='white', key="input", text_color='black'),
     gui.Submit('START', key="OK", size=(5, 1)), gui.CloseButton('Quit', button_color=('white', 'red'), key="Quit",size=(5, 1))]
]


# Create the game window
window = gui.Window('Memory Game', layout, keep_on_top=True, font=(None, 15))

# Initialize variables
nums = []  # List to store displayed numbers
pos = 'box0'  # Current position in the grid

isStart = 1  # Flag to indicate the start of the game
isWaiting = 0 # Flag to indicate waiting for player input

# Get game difficulty settings
temp = getDifficulty()

# Set the default values for game speed and initial size
if temp == None:
    sec = 1
    level = 5
else:
    sec , level = temp

print(level)
print(sec)

while True:
    
    event, values = window.read()
    print('Event:',event, values)
    
    # Exit the game if the window is closed or Quit is clicked
    if event in (None, 'Quit'):
        break
    
    # If the game has started and the player has submitted their input
    if not isStart:
        
        # Display a correct popup
        if values["input"].split() == nums:
            gui.PopupAutoClose("CORRECT",title='',keep_on_top=True,background_color='Dark Green',text_color='White',auto_close_duration=1,button_type=5)
        else:
            # Display a wrong popup with the correct answer
            gui.Popup("WRONG\n\nBetter Luck Next Time!\nCorrect Answer:\n" +" ".join(nums),title='',keep_on_top=True,background_color='Dark Red',text_color='White',font=("Helvetica",15))
            
            break
        
         # Clear the number list and input field
        nums.clear()
        window["input"]('')
        isWaiting = 1
        window["info"]("Round "+ str(level - 4) +" >> Press START for next round")
        window["OK"].Update('START')
        window.finalize()
        level += 1
        isWaiting = 1
        isStart = 1
        
    # If the game is not waiting for input
    if not isWaiting:
        window["info"]("Round "+ str(level - 4) +" >> Memorise Them!")
        window.finalize()
        disableControls(window)
        showTime(window,sec,level)
        enableControls(window)
        window[pos]('')
        window["info"]("Round "+ str(level - 4) +" Enter Ans(Include spaces between each number)")
        window["OK"].Update('OK')
        window.finalize()
        isStart = 0
    else:
        isWaiting = 0
        

    print('nums',nums)

window.close()

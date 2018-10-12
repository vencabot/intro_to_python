import tkinter as tk
from tkinter import Tk
from tkinter import Menu
from tkinter import Button
from tkinter import Label
from tkinter import filedialog
from tkinter import Frame
from tkinter import StringVar
from tkinter import IntVar
from tkinter import OptionMenu

##############################################
##### Initialize Variables and Functions #####
##############################################

# Program Details
programName = "3rd Strike Palette Editor"
verNum = "0.1"

# Character Palette Start Addresses
ALEX_PAL_ADDR   = 0x700600
RYU_PAL_ADDR    = 0x700980
YUN_PAL_ADDR    = 0x700D00
DUD_PAL_ADDR    = 0x701080
NECRO_PAL_ADDR  = 0x701400
HUGO_PAL_ADDR   = 0x701782
IBUKI_PAL_ADDR  = 0x701B00
ELENA_PAL_ADDR  = 0x701E80
ORO_PAL_ADDR    = 0x702200
YANG_PAL_ADDR   = 0x702580
KEN_PAL_ADDR    = 0x702900
SEAN_PAL_ADDR   = 0x702C80
URIEN_PAL_ADDR  = 0x703000
GOUKI_PAL_ADDR  = 0x703380
SHING_PAL_ADDR  = 0x703700
CHUN_PAL_ADDR   = 0x703800
MAK_PAL_ADDR    = 0x703B80
Q_PAL_ADDR      = 0x703F00
TWELVE_PAL_ADDR = 0x704280
REMY_PAL_ADDR   = 0x704600

# Offsets for a single character's 7 different color palettes
CHAR_PAL_BTN_OFFSET = [0,0x80,0x100,0x180,0x200,0x280,0x300]     

# Character List as it appears in the rom file for the palettes
srcCharList = ["Alex", 
            "Ryu", 
            "Yun", 
            "Dudley", 
            "Necro", 
            "Hugo", 
            "Ibuki", 
            "Elena", 
            "Oro", 
            "Yang", 
            "Ken",
            "Sean",
            "Urien",
            "Gouki",
            "Shin Gouki", 
            "Chun Li", 
            "Makoto", 
            "Q", 
            "Twelve", 
            "Remy"]

# Character List in Alphabetical Order
srcCharListABC = ["Alex", 
            "Chun Li", 
            "Dudley", 
            "Elena", 
            "Gouki",
            "Hugo",
            "Ibuki", 
            "Ken",
            "Makoto", 
            "Necro",
            "Oro", 
            "Q", 
            "Remy",
            "Ryu",  
            "Sean",
            "Shin Gouki", 
            "Twelve", 
            "Urien",
            "Yang",
            "Yun"]

# List for the IntVar later to select the column and row for which color in the palette you have selected
palSelect = [0, 1, 2, 3, 4, 5, 6 ,7]



##########################
##### Define Classes #####
##########################

# Palette Class - Individual Color Palette containing 64 Colors
class colorPalette:

    def __init__(self, singlePal):
        self.redColorArray = []                  # Initialize three arrays for each color
        self.greenColorArray = []
        self.blueColorArray = []

        self.loadColors(singlePal)               # Calls function to get the color values for the arrays

    # Arguments: Opened bytearray read from the file, the starting address of where the colors are
    def loadColors(self, p):
        # For loop to add to the start address for each new color (2 bytes per color, 64 colors)
        for x in range(0,128,2):
            self.redColorArray.append(self.getColor(p, x, "red"))
            self.greenColorArray.append(self.getColor(p, x, "green"))
            self.blueColorArray.append(self.getColor(p, x, "blue"))

    # Returns the color from the bytes provided
    def getColor(self, p, addr, color):
        largeByte = self.getByte(p, addr)
        smallByte = self.getByte(p, addr+1)
        word = (largeByte << 8) + smallByte

        if (color == "red"):
            return self.getFiveBitColor(word, word>>5)
        elif (color == "green"):
            return self.getFiveBitColor(word>>5, word>>10)
        elif (color == "blue"):
            return self.getFiveBitColor(word>>10, word>>15)

    # Returns the individual 5-bit R, B, or G value based on the 2 bytes passed to it
    def getFiveBitColor(self, origNum, subt):
        return (origNum-(subt<<5))

    # Takes a file address location and returns the value at that address
    def getByte(self, f, fileAddr):
        return f[fileAddr]

    # Takes the RGB colors and converts to a hex string usable for setting colors to widgets
    def outputColor(self, colorNumber):
        colorR = round(self.redColorArray[colorNumber]/31*255)
        colorG = round(self.greenColorArray[colorNumber]/31*255)
        colorB = round(self.blueColorArray[colorNumber]/31*255)
        hexValue = "#%02x%02x%02x" % (colorR, colorG, colorB)
        return hexValue

    

# Character Class - Contains 2-7 palette classes for each character
class charPalettes:
    
    def __init__(self, charPalArr, name):
        self.charName = name
        if ((len(charPalArr)/0x80) == 7):
            self.LP = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[0]))
            self.MP = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[1]))
            self.HP = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[2]))
            self.LK = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[3]))
            self.MK = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[4]))
            self.HK = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[5]))
            self.Special = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[6]))
        elif ((len(charPalArr)/0x80) == 2):
            self.LP = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[0]))
            self.MP = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[1]))
            self.HP = None
            self.LK = None
            self.MK = None
            self.HK = None
            self.Special = None
        updateSB("%s's palette has been initialized" % name)
    
    # Returns a list 80 bytes long to return a single palette instead of needing to pass the whole file
    def getSinglePalArray(self, fullPalArray, offset):
        arr = bytearray()
        for x in range(0,0x80):
            addy = offset + x
            arr.append(fullPalArray[addy])
        return arr



# PaletteEditor Class - Houses functions for reading the opened file and initializes all character's classes
class PaletteEditor:
    
    # Defines the palettes dictionary
    def __init__(self):
        self.palettes = {}
        
    # Defines the function to open the file selected and initialize the character classes
    def openFileCmd(self):
        openFilePath = filedialog.askopenfilename(title="Select File",filetypes=(("3s Character Palette (51) File","51"),("All Files","*.*")))
        if openFilePath != "":
            updateSB("Loaded %s into memory!" % openFilePath)
            openFile = open(openFilePath,"rb").read()
            self.initCharPalClasses(openFile)
            updateFrameColor()
            updateSB("Character Palettes Initialized!")
            
            

    # Defines all of the character classes and sends the needed data to be parsed for the individual palettes
    def initCharPalClasses(self, f):
        self.palettes["Alex"] = charPalettes(self.charPalDataArray(f, ALEX_PAL_ADDR, 7), "Alex")
        self.palettes["Ryu"] = charPalettes(self.charPalDataArray(f, RYU_PAL_ADDR, 7), "Ryu")
        self.palettes["Yun"] = charPalettes(self.charPalDataArray(f, YUN_PAL_ADDR, 7), "Yun")
        self.palettes["Dudley"] = charPalettes(self.charPalDataArray(f, DUD_PAL_ADDR, 7), "Dudley")
        self.palettes["Necro"] = charPalettes(self.charPalDataArray(f, NECRO_PAL_ADDR, 7), "Necro")
        self.palettes["Hugo"] = charPalettes(self.charPalDataArray(f, HUGO_PAL_ADDR, 7), "Hugo")
        self.palettes["Ibuki"] = charPalettes(self.charPalDataArray(f, IBUKI_PAL_ADDR, 7), "Ibuki")
        self.palettes["Elena"] = charPalettes(self.charPalDataArray(f, ELENA_PAL_ADDR, 7), "Elena")
        self.palettes["Oro"] = charPalettes(self.charPalDataArray(f, ORO_PAL_ADDR, 7), "Oro")
        self.palettes["Yang"] = charPalettes(self.charPalDataArray(f, YANG_PAL_ADDR, 7), "Yang")
        self.palettes["Ken"] = charPalettes(self.charPalDataArray(f, KEN_PAL_ADDR, 7), "Ken")
        self.palettes["Sean"] = charPalettes(self.charPalDataArray(f, SEAN_PAL_ADDR, 7), "Sean")
        self.palettes["Urien"] = charPalettes(self.charPalDataArray(f, URIEN_PAL_ADDR, 7), "Urien")
        self.palettes["Gouki"] = charPalettes(self.charPalDataArray(f, GOUKI_PAL_ADDR, 7), "Gouki")
        self.palettes["Shin Gouki"] = charPalettes(self.charPalDataArray(f, SHING_PAL_ADDR, 2), "Shin Gouki")
        self.palettes["Chun Li"] = charPalettes(self.charPalDataArray(f, CHUN_PAL_ADDR, 7), "Chun Li")
        self.palettes["Makoto"] = charPalettes(self.charPalDataArray(f, MAK_PAL_ADDR, 7), "Makoto")
        self.palettes["Q"] = charPalettes(self.charPalDataArray(f, Q_PAL_ADDR, 7), "Q")
        self.palettes["Twelve"] = charPalettes(self.charPalDataArray(f, TWELVE_PAL_ADDR, 7), "Twelve")
        self.palettes["Remy"] = charPalettes(self.charPalDataArray(f, REMY_PAL_ADDR, 7), "Remy")

    # Takes the full file, character offset address, and the number of palettes, and returns only the bytes relevent to that character
    def charPalDataArray(self, f, startAddr, numPal):
        arr = bytearray()
        size = numPal * 0x80
        for x in range(0,size):
            arr.append(f[startAddr+x])
        return arr


class SortableCharacterMenu:
    src_char_list = [
            "Alex", "Ryu", "Yun", "Dudley", "Necro", "Hugo", "Ibuki",
            "Elena", "Oro", "Yang", "Ken", "Sean", "Urien", "Gouki",
            "Shin Gouki", "Chun Li", "Makoto", "Q", "Twelve", "Remy"]

    abc_char_list = sorted(src_char_list, key=str.lower)

    def __init__(self, tk_root, char_list_str):
        self.tk_root = tk_root
        self.char_list_str = char_list_str
        self.tk_menu = None
        self.sort_src()

    def _create_and_repack_menu(self, char_list):
        if self.tk_menu:
            self.tk_menu.pack_forget()
        self.tk_menu = OptionMenu(
                self.tk_root, self.char_list_str, *char_list,
                command=updateFrameColor)
        self.tk_menu.config(width=10, bd=1)
        self.tk_menu.pack()

    def sort_abc(self):
        self._create_and_repack_menu(self.abc_char_list)

    def sort_src(self):
        self._create_and_repack_menu(self.src_char_list)

    
# Creates the base object for the palette editor to allow for some variables to have a state
palEdit = PaletteEditor()



# *******************
# *****START GUI*****
# *******************

# Create main object for GUI
root = Tk()
root.geometry("320x240+350+150")
root.title(programName + " - Version " + verNum)

# Define updateStatBar function to update the statusbar
def updateSB(t):
    statusBar.config(text=t)

# Define button focus function
def setFocusOnButton(event):
    event.widget.focus()

# Define Menu Mouseover Events - Updates the status bar when mousing over items in the File Menu
def mOver_File(event):
    # Event list
    # 0 = Open
    # 2 = Exit
    calledEvent = root.call(event.widget, "index", "active")
    if (calledEvent == 0):
        updateSB("Open a file")
    elif (calledEvent == 2):
        updateSB("Exit the program")
    elif (calledEvent == "none"):
        updateSB("")

# Define Menu Mouseover Events - Updates the status bar when mousing over items in the Options Menu
def mOver_Options(event):
    # Event list
    # 0 = Show Characters Alphabetically
    calledEvent = root.call(event.widget, "index", "active")
    if (calledEvent == 0):
        updateSB("Shows the character list in alphabetical order")
    elif (calledEvent == "none"):
        updateSB("")

# Define a small function to allow toggling between ABC and nonABC order while retaining it's call to update colors
def toggleABC(name):
    #print("Right Before toggleABC runs, charListStr is: %s" % charListStr.get())
    #print("ToggleABC: name passed: %s" % name)
    tk._setit(charListStr, name)
    updateFrameColor()

# Updates the character list between file order and alphabetical order - Prints a Debugger Line to show what character is selected
def updateCharList():
    print("updateCharList is running")
    if (charABCOrder.get() == 0):
        print("trying to sort by src order")
        sortable_character_menu.sort_src()
    else:
        print("trying to sort by abc order")
        sortable_character_menu.sort_abc()

    print("Current selected character is %s" % charListStr.get())

# Updates the frame color using the selected character name, column, and row - ONLY DOES LP COLORS CURRENTLY
def updateFrameColor(*args):
    charName = charListStr.get()
    row = selectedPaletteRowVar.get() * 8
    col = selectedPaletteColumnVar.get()
    numColor = row + col
    palFrame.config(bg=palEdit.palettes[charName].LP.outputColor(numColor))
    updateSB("Displaying color %d of %s's LP Palette" % (numColor+1, charName))



#######################
##### DEBUG STUFF #####
#######################

def mOver_Test(event):
    # Event list
    print(str(event))
    #calledEvent = root.call(event.widget, "index", "active")
    #print(calledEvent)
    #if (calledEvent == 0):
    #    updateSB("Shows the character list in alphabetical order")
    #elif (calledEvent == "none"):
    #    updateSB("")


########################
##### MENU BAR GUI #####
########################

# Config to set mainMenuBar as the menu bar
mainMenuBar = Menu(root)
root.config(menu=mainMenuBar)

# Create object for the File and Options dropdown bar, tearoff=0 removes the dashes at the top of the cascade menu
fileDropDown = Menu(mainMenuBar, tearoff=0)
optionDropDown = Menu(mainMenuBar, tearoff=0)

# Add the File cascade to the mainMenuBar
mainMenuBar.add_cascade(label="File", menu=fileDropDown)
mainMenuBar.add_cascade(label="Options", menu=optionDropDown)

# Variable for alphabetical char list order
charABCOrder = tk.IntVar()
charABCOrder.set(0)

# Add options to the mainFileDropDown Cascade
fileDropDown.add_command(label="Open", command=palEdit.openFileCmd)
fileDropDown.add_separator()
fileDropDown.add_command(label="Quit", command=root.quit)

# Add options to the Options Cascade
optionDropDown.add_checkbutton(label="Show Characters Alphabetically", onvalue=1, offvalue=0, variable=charABCOrder, command=updateCharList)

# Bind MouseOver events
fileDropDown.bind("<<MenuSelect>>", mOver_File)
optionDropDown.bind("<<MenuSelect>>", mOver_Options)



#######################
##### MAIN WINDOW #####
#######################

# Add in buttons to perform tasks
buttonTestCalc = Button(root, text="Update Frame Color", command=updateFrameColor)
buttonTestCalc.pack()


palFrame = Frame(height=100, width=100, bd=1, relief=tk.SUNKEN, bg="red")
palFrame.pack()

# Creates StringVar object with srcCharList to select character
charListStr = StringVar(root)
charListStr.set(srcCharList[0])       # Sets default value for dropdown menu

# Creating dropdown menus for selecting Columns and Rows for the palette
selectedPaletteColumnVar = IntVar(root)
selectedPaletteColumnVar.set(palSelect[0])

selectedPaletteRowVar = IntVar(root)
selectedPaletteRowVar.set(palSelect[0])

selectedPalCol = OptionMenu(root, selectedPaletteColumnVar, *palSelect, command=updateFrameColor)
selectedPalRow = OptionMenu(root, selectedPaletteRowVar, *palSelect, command=updateFrameColor)

selectedPalCol.pack()
selectedPalRow.pack()

# Create the Vencabot example sortable drop-down menu.
sortable_character_menu = SortableCharacterMenu(root, charListStr)



##########################
##### STATUS BAR GUI #####
##########################

statusBar = Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusBar.pack(side=tk.BOTTOM, fill=tk.X)



##########################
##### GUI LOOP START #####
##########################

# Run window infinitely until close
root.mainloop()

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
from tkinter import Scale

##############################################
##### Initialize Variables and Functions #####
##############################################

# Program Details
programName = "3rd Strike Palette Editor"
verNum = "1.0"

# Character Palette Start Addresses
ALEX_PAL_ADDR   = 0x700600
RYU_PAL_ADDR    = 0x700980
YUN_PAL_ADDR    = 0x700D00
DUD_PAL_ADDR    = 0x701080
NECRO_PAL_ADDR  = 0x701400
HUGO_PAL_ADDR   = 0x701780
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

# Made a variable for the default value for the srcCharList variable
START_CHAR = "Alex"


# List for the IntVar later to select the column and row for which color in the palette you have selected
palSelect = [0, 1, 2, 3, 4, 5, 6 ,7]
buttonSelect = ["LP", "MP", "HP", "LK", "MK", "HK", "EX"]



##########################
##### Define Classes #####
##########################

# Palette Class - Individual Color Palette containing 64 Colors
class colorPalette:

    def __init__(self, singlePal):
        self.redColorArray = []                  # Initialize three arrays for each color
        self.greenColorArray = []
        self.blueColorArray = []

        self.redColorArrayBackup = []            # Backup arrays just in case we need a return to default option
        self.greenColorArrayBackup = []
        self.blueColorArrayBackup = []

        self.loadColors(singlePal)               # Calls function to get the color values for the arrays

    # Arguments: Opened bytearray read from the file, the starting address of where the colors are
    def loadColors(self, p):
        # For loop to add to the start address for each new color (2 bytes per color, 64 colors)
        for x in range(0,128,2):
            self.redColorArray.append(self.getColor(p, x, "red"))
            self.greenColorArray.append(self.getColor(p, x, "green"))
            self.blueColorArray.append(self.getColor(p, x, "blue"))
        self.redColorArrayBackup = self.redColorArrayBackup
        self.greenColorArrayBackup = self.greenColorArrayBackup
        self.blueColorArrayBackup = self.blueColorArrayBackup

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

    # Takes in the index of the color of the palette and returns the hex for red, green, or blue
    def outputRed(self, colorNumber):
        return self.redColorArray[colorNumber]

    def outputGreen(self, colorNumber):
        return self.greenColorArray[colorNumber]

    def outputBlue(self, colorNumber):
        return self.blueColorArray[colorNumber]
    
    # Takes the RGB colors and converts to a hex string usable for setting colors to widgets
    def outputColor(self, colorNumber):
        colorR = round(self.redColorArray[colorNumber]/31*255)
        colorG = round(self.greenColorArray[colorNumber]/31*255)
        colorB = round(self.blueColorArray[colorNumber]/31*255)
        hexValue = "#%02x%02x%02x" % (colorR, colorG, colorB)
        return hexValue

    def writeNewColorValue(self, pos, rc, gc, bc):
        self.redColorArray[pos] = rc
        self.greenColorArray[pos] = gc
        self.blueColorArray[pos] = bc

    def returnColorBytes(self, pos):
        rc = self.redColorArray[pos]
        gc = self.greenColorArray[pos]
        bc = self.blueColorArray[pos]
        return (bc<<10) + (gc<<5) + rc

    def returnPaletteColorBytes(self, a):
        tempArr = a
        for i in range(0,len(self.redColorArray)):
            word = self.returnColorBytes(i)
            bigByte = word >> 8
            littleByte = word - (bigByte<<8)
            tempArr.append(bigByte)
            tempArr.append(littleByte)
        return tempArr


    

# Character Class - Contains 2 or 7 palette classes for each character - Shin Gouki is the only character with 2 palettes
class charPalettes:
    
    def __init__(self, charPalArr, name):
        self.button = {}
        self.charName = name
        if ((len(charPalArr)/0x80) == 7):
            self.button["LP"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[0]))
            self.button["MP"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[1]))
            self.button["HP"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[2]))
            self.button["LK"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[3]))
            self.button["MK"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[4]))
            self.button["HK"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[5]))
            self.button["EX"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[6]))
        elif ((len(charPalArr)/0x80) == 2):
            self.button["LP"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[0]))
            self.button["MP"] = colorPalette(self.getSinglePalArray(charPalArr, CHAR_PAL_BTN_OFFSET[1]))
            self.button["HP"] = None
            self.button["LK"] = None
            self.button["MK"] = None
            self.button["HK"] = None
            self.button["EX"] = None
        updateSB("%s's palette has been initialized" % name)
    
    # Returns a list 80 bytes long to return a single palette instead of needing to pass the whole file
    def getSinglePalArray(self, fullPalArray, offset):
        arr = bytearray()
        for x in range(0,0x80):
            addy = offset + x
            arr.append(fullPalArray[addy])
        return arr

    def returnCharPalettes(self, a):
        tempArr = a
        if self.charName != "Shin Gouki":
            btn = ["LP", "MP", "HP", "LK", "MK", "HK", "EX"]
        else:
            btn = ["LP", "MP"]
        for i in btn:
            tempArr = self.button[i].returnPaletteColorBytes(tempArr)
        return tempArr


# PaletteEditor Class - Houses functions for reading the opened file and initializes all character's classes
class PaletteEditor:
    
    # Defines the palettes dictionary
    def __init__(self):
        self.palettes = {}
        self.srcFile = bytearray
        self.destFile = bytearray
        
    # Defines the function to open the file selected and initialize the character classes
    def openFileCmd(self):
        openFilePath = filedialog.askopenfilename(title="Select File",filetypes=(("3s Character Palette (51) File","51"),("All Files","*.*")))
        if openFilePath != "":
            updateSB("Loaded %s into memory!" % openFilePath)
            self.srcFile = open(openFilePath,"rb").read()
            fileDropDown.entryconfig("Save As...", state="normal")
            
            vencabot_frame.grid(row=0, column=0)
            buttonSelectFrame.grid(row=0, column=1)
            selectedButtonColorPalette.pack()
            
            self.initCharPalClasses(self.srcFile)
            palGrid.updateGrid()
            updateColors()
            updateSB("Character Palettes Initialized!")

    def saveFileCmd(self):
        saveFilePath = filedialog.asksaveasfilename(defaultextension="", initialfile="51", filetypes=(("3s Character Palette (51) File","51"),("All Files","*.*")))
        if saveFilePath:
            self.destFile = bytearray(self.buildNewFileArray())

            f=open(saveFilePath,"wb+")
            f.write(self.destFile)
            f.close()
            

    def buildNewFileArray(self):
        newArray = bytearray
        newArray = self.buildPrePaletteFile()
        newArray = self.buildPalettes(newArray)
        newArray = self.buildPostPaletteFile(newArray)
        return newArray

    def buildPrePaletteFile(self):
        tempArr = []
        for i in range(0,ALEX_PAL_ADDR):
            tempArr.append(self.srcFile[i])
        return tempArr

    def buildPalettes(self, a):
        tempArr = a
        chrlist = [
            "Alex", "Ryu", "Yun", "Dudley", "Necro", "Hugo", "Ibuki", 
            "Elena", "Oro", "Yang", "Ken", "Sean", "Urien", "Gouki",
            "Shin Gouki", "Chun Li", "Makoto", "Q", "Twelve", "Remy"]
        for i in chrlist:
            tempArr = self.palettes[i].returnCharPalettes(tempArr)
        return tempArr

    def buildPostPaletteFile(self, a):
        tempArr = a
        lenSrcFile = len(self.srcFile)
        startPt = len(a)
        dist = lenSrcFile-startPt
        for i in range(0, dist):
            tempArr.append(self.srcFile[startPt+i])
        return tempArr

            
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


# Vencabot's Sortable Menu Character Class - Creates a class that allows us to destroy 
# and re-create the character menu so it can be switched between ROM order and 
# ABC order --- NEAT! <3 <3 <3
class SortableCharacterMenu:
    src_char_list = [
            "Alex", "Ryu", "Yun", "Dudley", "Necro", "Hugo", "Ibuki",
            "Elena", "Oro", "Yang", "Ken", "Sean", "Urien", "Gouki",
            "Shin Gouki", "Chun Li", "Makoto", "Q", "Twelve", "Remy"]

    # Sorts the above character list into ABC order
    abc_char_list = sorted(src_char_list, key=str.lower)

    # initializes important variables
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
                command=updateColors)
        self.tk_menu.config(width=10, bd=1)
        self.tk_menu.pack()
        

    def sort_abc(self):
        self._create_and_repack_menu(self.abc_char_list)

    def sort_src(self):
        self._create_and_repack_menu(self.src_char_list)


class PaletteGrid:
    def __init__(self, tk_root):
        self.tk_root = tk_root
        self.palGrid = {}
        self.selectedItem = -1
        self.palLoaded = False
        self.setupGrid()

    def clickCapture(self, event, pos):
        if self.palLoaded:
            if self.selectedItem >= 0:
                self.palGrid[self.selectedItem].config(relief=tk.FLAT, highlightthickness=1, 
                                                        highlightcolor="black", highlightbackground="black")
            event.widget.config(relief=tk.SUNKEN, highlightthickness=2, 
                                    highlightcolor="red", highlightbackground="red")
            self.selectedItem = pos
            updateColors()

    def onEnter(self, event, pos):
        self.palGrid[pos].config(highlightthickness=2, highlightcolor="blue", highlightbackground="blue")
        updateSB("Mousing Over Position (%d, %d)" % (self.getCol(pos), self.getRow(pos)))
    
    def onLeave(self, event, pos):
        if self.selectedItem != pos:
            self.palGrid[pos].config(highlightthickness=1, highlightcolor="black", highlightbackground="black")
        else:
            self.palGrid[pos].config(highlightthickness=2, highlightcolor="red", highlightbackground="red")
        updateSB("")

    def getCol(self, loc):
        pos = loc % 8
        return pos

    def getRow(self, loc):
        pos = loc
        rem = loc % 8
        newPos = (pos-rem)/8
        return newPos
        
    def getPos(self):
        if self.selectedItem >= 0:
            return self.selectedItem
        else:
            return 0

    def setupGrid(self):
        for row in range(0, 8):
            for col in range(0, 8):
                pos = row*8 + col
                self.palGrid[pos] = Frame(self.tk_root, bd=1, highlightthickness=1, 
                                        highlightcolor="black", highlightbackground="black", 
                                        width=20, height=20, padx=0, pady=0)
                self.palGrid[pos].bind("<1>", lambda x, y=pos: self.clickCapture(x, y), add="+")
                self.palGrid[pos].bind("<Enter>", lambda x, y=pos: self.onEnter(x, y), add="+")
                self.palGrid[pos].bind("<Leave>", lambda x, y=pos: self.onLeave(x, y), add="+")
                self.palGrid[pos].grid(row=row, column=col)

    def updateGrid(self):
        if self.palLoaded == False:    
            self.palLoaded = True
            self.palGrid[0].config(highlightthickness=2, highlightcolor="red", highlightbackground="red")
            self.selectedItem = 0
        for row in range(0, 8):
            for col in range(0, 8):
                pos = row*8 + col
                charName = charListStr.get()
                btn = selectedButtonColorPaletteVar.get()
                bgColor = palEdit.palettes[charName].button[btn].outputColor(pos)
                self.palGrid[pos].config(bg=bgColor)

    def updateGridPositionColor(self, rc, gc, bc, hexValue):
        if self.palLoaded:
            pos = self.selectedItem
            charName = charListStr.get()
            btn = selectedButtonColorPaletteVar.get()
            palEdit.palettes[charName].button[btn].writeNewColorValue(pos, rc, gc, bc)            
            self.palGrid[self.selectedItem].config(bg=hexValue)
    
    

    
# Creates the base object for the palette editor to allow for some variables to have a state
palEdit = PaletteEditor()



###############################
##### START GUI FUNCTIONS #####
###############################

# Define updateStatBar function to update the statusbar
def updateSB(t):
    statusBar.config(text=t)

def updateColorRGBLabel(color, t):
    if color == "red":
        redRGBValueLabel.config(text=t)
    elif color == "green":
        greenRGBValueLabel.config(text=t)
    elif color == "blue":
        blueRGBValueLabel.config(text=t)

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

def updateSliders(charName, btn, pos):
    redSlider.set(palEdit.palettes[charName].button[btn].outputRed(pos))
    greenSlider.set(palEdit.palettes[charName].button[btn].outputGreen(pos))
    blueSlider.set(palEdit.palettes[charName].button[btn].outputBlue(pos))
    updatePreviewFromSliders()

def updatePreviewFromSliders(*_):
    if palGrid.palLoaded:
        rc = redSlider.get()
        gc = greenSlider.get()
        bc = blueSlider.get()
        
        colorR = round(rc/31*255)
        colorG = round(gc/31*255)
        colorB = round(bc/31*255)
        updateColorRGBLabel("red", str(colorR))
        updateColorRGBLabel("green", str(colorG))
        updateColorRGBLabel("blue", str(colorB))
        hexValue = "#%02x%02x%02x" % (colorR, colorG, colorB)
        palFrame.config(bg=hexValue)
        palGrid.updateGridPositionColor(rc, gc, bc, hexValue)

# Updates the frame color using the selected character name, column, and row
#def updatePreviewColor(*_):
#    charName = charListStr.get()
#    row = selectedPaletteRowVar.get() * 8
#    col = selectedPaletteColumnVar.get()
#    btn = selectedButtonColorPaletteVar.get()
#    numColor = row + col
#    redSlider.set(palEdit.palettes[charName].button[btn].outputRed(numColor))
#    greenSlider.set(palEdit.palettes[charName].button[btn].outputGreen(numColor))
#    blueSlider.set(palEdit.palettes[charName].button[btn].outputBlue(numColor))
#    palFrame.config(bg=palEdit.palettes[charName].button[btn].outputColor(numColor))
#    updateSB("Displaying color %d of %s's %s Palette" % (numColor+1, charName, btn))

# Updates the frame color using the selected character name, column, and row
def updateColors(*_):
    charName = charListStr.get()
    btn = selectedButtonColorPaletteVar.get()
    pos = palGrid.getPos()
    updateSliders(charName, btn, pos)
    palGrid.updateGrid()
    updateSB("Displaying color %d out of 64 for %s's %s Palette" % (pos+1, charName, btn))



#######################
##### DEBUG STUFF #####
#######################

def mOver_Test(event):
    # Event list
    print(str(event))
    calledEvent = root.call(event.widget, "index", "active")
    print(calledEvent)
    #if (calledEvent == 0):
    #    updateSB("Shows the character list in alphabetical order")
    #elif (calledEvent == "none"):
    #    updateSB("")


########################
##### MENU BAR GUI #####
########################

# Create main object for GUI
root = Tk()
root.geometry("440x680+350+150")
root.title(programName + " - Version " + verNum)

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
fileDropDown.add_command(label="Save As...", command=palEdit.saveFileCmd, state="disabled")
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
#buttonTestCalc = Button(root, text="Update Frame Color", command=updateFrameColor)
#buttonTestCalc.pack()

previewLabel = Label(root, text="Preview Color")
previewLabel.pack()
palFrame = Frame(height=100, width=100, bd=1, relief=tk.SUNKEN)
palFrame.pack()

# Creates StringVar object with srcCharList to select character
charListStr = StringVar(root)
charListStr.set(START_CHAR)       # Sets default value for dropdown menu

mainButtonsFrame = Frame(root)

vencabot_frame = Frame(mainButtonsFrame)
buttonSelectFrame = Frame(mainButtonsFrame)


# Create the Vencabot example sortable drop-down menu.
sortable_character_menu = SortableCharacterMenu(vencabot_frame, charListStr)





#######################################
##### REMOVING TO MOVE TO PALGRID #####
#######################################

# Creating dropdown menus for selecting Columns and Rows for the palette
#selectedPaletteColumnVar = IntVar(root)
#selectedPaletteColumnVar.set(palSelect[0])

#selectedPaletteRowVar = IntVar(root)
#selectedPaletteRowVar.set(palSelect[0])

#selectedPalCol = OptionMenu(root, selectedPaletteColumnVar, *palSelect, command=updatePreviewColor)
#selectedPalRow = OptionMenu(root, selectedPaletteRowVar, *palSelect, command=updatePreviewColor)

#selectedPalCol.pack()
#selectedPalRow.pack()

#######################################
##### REMOVING TO MOVE TO PALGRID #####
#######################################





# Create dropdown menu to select the button that's associated with the specific color palette you want
selectedButtonColorPaletteVar = StringVar(root)
selectedButtonColorPaletteVar.set(buttonSelect[0])

selectedButtonColorPalette = OptionMenu(buttonSelectFrame, selectedButtonColorPaletteVar, *buttonSelect, command=updateColors)

# Creates a Frame to contain all of the slider bars and labels
sliderFrame = Frame(root)
sliderFrame.pack()

# Creates color labels for the sliders
redLabel = Label(sliderFrame, text="Red: ")
greenLabel = Label(sliderFrame, text="Green: ")
blueLabel = Label(sliderFrame, text="Blue: ")

redRGBValueLabel = Label(sliderFrame, text="0", width=3)
greenRGBValueLabel = Label(sliderFrame, text="0", width=3)
blueRGBValueLabel = Label(sliderFrame, text="0", width=3)

# Create 3 "Scale" slider bars from 0 - 31 (32 values / 5 bits) to handle R, G, and B colors
redSlider = Scale(sliderFrame, from_=0, to=31, orient=tk.HORIZONTAL, command=updatePreviewFromSliders)
greenSlider = Scale(sliderFrame, from_=0, to=31, orient=tk.HORIZONTAL, command=updatePreviewFromSliders)
blueSlider = Scale(sliderFrame, from_=0, to=31, orient=tk.HORIZONTAL, command=updatePreviewFromSliders)

redLabel.grid(row=3, column=0)
greenLabel.grid(row=7, column=0)
blueLabel.grid(row=11, column=0)

redSlider.grid(row=0, column=1, rowspan=4, columnspan=4)
greenSlider.grid(row=4, column=1, rowspan=4, columnspan=4)
blueSlider.grid(row=8, column=1, rowspan=4, columnspan=4)

redRGBValueLabel.grid(row=3, column=5, columnspan=2)
greenRGBValueLabel.grid(row=7, column=5, columnspan=2)
blueRGBValueLabel.grid(row=11, column=5, columnspan=2)


palGridFrame = Frame(root, border=1, relief=tk.SUNKEN)
palGridFrame.pack()


palGrid = PaletteGrid(palGridFrame)


mainButtonsFrame.pack()



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
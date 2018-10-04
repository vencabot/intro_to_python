import tkinter as tk
from tkinter import Tk
from tkinter import Menu
from tkinter import Button
from tkinter import Label
from tkinter import filedialog


# ***** Initialize Variables and Functions *****

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

CHAR_PAL_BTN_OFFSET = [0,0x80,0x100,0x180,0x200,0x280,0x300]     # Offsets for a single character's 7 different color palettes



# **************************
# ***** Define Classes *****
# **************************

# Palette Class - Individual Color Palette containing 64 Colors
class colorPalette:

    def __init__(self, f, startAddr, offset):
        self.redColorArray = []                 # Initialize three arrays for each color
        self.greenColorArray = []
        self.blueColorArray = []
        newStartAddr = startAddr + offset       # Gets the correct address based on the character's 
                                                # address in the file plus the corresponding offset
                                                # based on the color of the button pressed

        self.loadColors(f, newStartAddr)        # Calls function to get the color values for the arrays


    # Arguments: Opened bytearray read from the file, the starting address of where the colors are
    def loadColors(self, f, startAddr):
        # For loop to add to the start address for each new color (2 bytes per color, 64 colors)
        for x in range(0,128,2):
            colorAddr = startAddr + x
            self.redColorArray.append(self.getColor(f, colorAddr, "red"))
            self.greenColorArray.append(self.getColor(f, colorAddr, "green"))
            self.blueColorArray.append(self.getColor(f, colorAddr, "blue"))

    # Returns the color from the bytes provided
    def getColor(self, f, addr, color):
        largeByte = self.getByte(f, addr)
        smallByte = self.getByte(f, addr+1)
        word = (largeByte << 8) + smallByte

        if (color == "red"):
            return self.getSingleColor(word, word>>5)
        elif (color == "green"):
            return self.getSingleColor(word>>5, word>>10)
        elif (color == "blue"):
            return self.getSingleColor(word>>10, word>>15)

    # Returns the individual R, B, or G value based on the 2 bytes passed to it
    def getSingleColor(self, origNum, subt):
        return (origNum-(subt<<5))

    # Takes a file address location and returns the value at that address
    def getByte(self, f, fileAddr):
        return f[fileAddr]


class charPalettes:
    
    def __init__(self, f, startAddr, numPal, name):
        self.charName = name
        if (numPal == 7):
            self.colPalLP = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[0])
            self.colPalMP = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[1])
            self.colPalHP = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[2])
            self.colPalLK = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[3])
            self.colPalMK = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[4])
            self.colPalHK = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[5])
            self.colPalSpecial = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[6])
        elif (numPal == 2):
            self.colPalLP = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[0])
            self.colPalMP = colorPalette(f, startAddr, CHAR_PAL_BTN_OFFSET[1])
            self.colPalHP = None
            self.colPalLK = None
            self.colPalMK = None
            self.colPalHK = None
            self.colPalSpecial = None
        updateSB("%s's palette has been initialized" % name)


def initCharPalClasses(f):
    AlexPal = charPalettes(f, ALEX_PAL_ADDR, 7, "Alex")
    RyuPal = charPalettes(f, RYU_PAL_ADDR, 7, "Ryu")
    YunPal = charPalettes(f, YUN_PAL_ADDR, 7, "Yun")
    DudPal = charPalettes(f, DUD_PAL_ADDR, 7, "Dudley")
    NecroPal = charPalettes(f, NECRO_PAL_ADDR, 7, "Necro")
    HugoPal = charPalettes(f, HUGO_PAL_ADDR, 7, "Hugo")
    IbukiPal = charPalettes(f, IBUKI_PAL_ADDR, 7, "Ibuki")
    ElenaPal = charPalettes(f, ELENA_PAL_ADDR, 7, "Elena")
    OroPal = charPalettes(f, ORO_PAL_ADDR, 7, "Oro")
    YangPal = charPalettes(f, YANG_PAL_ADDR, 7, "Yang")
    KenPal = charPalettes(f, KEN_PAL_ADDR, 7, "Ken")
    SeanPal = charPalettes(f, SEAN_PAL_ADDR, 7, "Sean")
    UrienPal = charPalettes(f, URIEN_PAL_ADDR, 7, "Urien")
    GoukiPal = charPalettes(f, GOUKI_PAL_ADDR, 7, "Gouki")
    ShinGoukiPal = charPalettes(f, SHING_PAL_ADDR, 2, "Shin Gouki")
    ChunPal = charPalettes(f, CHUN_PAL_ADDR, 7, "Chun Li")
    MakPal = charPalettes(f, MAK_PAL_ADDR, 7, "Makoto")
    QPal = charPalettes(f, Q_PAL_ADDR, 7, "Q")
    TwelvePal = charPalettes(f, TWELVE_PAL_ADDR, 7, "Twelve")
    RemyPal = charPalettes(f, REMY_PAL_ADDR, 7, "Remy")



# *******************
# *****START GUI*****
# *******************

# Create main object for GUI
root = Tk()
root.geometry("800x600+350+150")

# Define updateStatBar function to update the statusbar
def updateSB(t):
    statusBar.config(text=t)

# Define button focus function
def setFocusOnButton(event):
    event.widget.focus()

# Define Menu Mouseover Events
def mOver_File(event):
    # Event list
    # 0 = Open
    # 2 = Exit
    calledEvent = root.call(event.widget, "index", "active")
    print(calledEvent)
    if (calledEvent == 0):
        updateSB("Open a file")
    elif (calledEvent == 2):
        updateSB("Exit the program")
    elif (calledEvent == "none"):
        updateSB("")


# Define Menu Functions
def openFileCmd():
    openFilePath = filedialog.askopenfilename(title="Select File",filetypes=(("3s Character Palette (51) File","51"),("All Files","*.*")))
    if openFilePath != "":
        updateSB("Loaded %s into memory!" % openFilePath)
        openFile = open(openFilePath,"rb").read()
        initCharPalClasses(openFile)
        updateSB("Character Palettes Initialized!")


   
def testClasses():
    print(AlexPal.charName)
    

##### MENU BAR GUI #####

# Config to set mainMenuBar as the menu bar
mainMenuBar = Menu(root)
root.config(menu=mainMenuBar)

# Create object for the File dropdown bar, tearoff=0 removes the dashes at the top of the cascade menu
mainFileDropDown = Menu(mainMenuBar, tearoff=0)
# Add the File cascade to the mainMenuBar
mainMenuBar.add_cascade(label="File", menu=mainFileDropDown)

# Add Options to the mainFileDropDown Cascade
mainFileDropDown.add_command(label="Open", command=openFileCmd)
mainFileDropDown.add_separator()
mainFileDropDown.add_command(label="Quit", command=root.quit)

# Bind MouseOver events
mainFileDropDown.bind("<<MenuSelect>>", mOver_File)

# Add in buttons to perform tasks
buttonTestCalc = Button(root, text="Test Calc", command=testClasses)
buttonTestCalc.pack()








##### STATUS BAR GUI #####

statusBar = Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusBar.pack(side=tk.BOTTOM, fill=tk.X)




# Run window infinitely until close
root.mainloop()
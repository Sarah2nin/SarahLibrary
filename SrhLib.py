#----===|  LICENSE  |===----#

# SarahLibrary
# Copyright (C) 2025 Sarahtonin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

#----===|LAST UPDATED|===----#

#Last updated by: Sarahtonin
#Last updated at: ~11:00 30.09.25

#----===|  START  |===----#

from num2words import num2words
from word2number import w2n
import re

#----===|VARIABLES|===----#

SpecialCharacters = '"!@#$%^&*()-+?_=,''<>/"'

#----===|  LISTS  |===----#

#----===|FUNCTIONS|===----#

def SrhLib(InpType = "Nothing."):
    """
    SrhLib() prints out all currently available items which matches InpType.
    (e.g. SrhLib("Functions") would print all available functions)
    >InpType has three values to choose from;
    >- 'Variables': Which will list all currently available Variables in SrhLib,
    >- 'Lists': Which will list all currently available Lists in SrhLib, and
    >- 'Functions': Which will list all currently available Functions in SrhLib.
    """

    if not isinstance(InpType, str):
        print("Sorry, you didn't input a string into SrhLib()!")

    else:
        if InpType.capitalize() == "Variables":
            print("The variables in SrhLib are:")
            print(" SpecialCharacters")
        elif InpType.capitalize() == "Lists":
            print("Sorry, Sarah hasn't made any lists, yet!")
        elif InpType.capitalize() == "Functions":
            print("The functions in SrhLib are:")
            print(" Simplify()")
            print(" Complexify()")
            print(" CheckType()")
            print(" PrettyPrint()")
        else:
            print("Sorry, SrhLib() didn't recognise what you typed! Check the description of SrhLib() by hovering over the function with your cursor, in your code.")



def Simplify(InpString = "Sorry, you didn't add any args to simplify()!", InpPriority = "Num", InpSymbols = False, /):
    """
    Simplify() relies on num2words, and word2number. Make sure to install those via pip first.
    >Simplify() simplifies a string to the bare minimum, while still retaining some logic.
    >(e.g. "Hi, there!" into "HiThere")
    >
    >- InpString: The string you want to Simplify(). Make sure that it's a string.
    >
    >- InpPriority: Has two values to choose from; 
    >        - 'Num': Which will make words into numbers (e.g. 'Two' into 2), and 
    >        - 'Str': Which will make numbers into words (e.g. 2 into 'Two').
    >
    >- InpSymbols: If this is True or 1, it will keep symbols. Otherwise, symbols are removed.
    """

    if not isinstance(InpString, str) or not isinstance(InpPriority, str):
        return("Sorry, you didn't input a string into Simplify()!")
    else:
        InpPriority = InpPriority.capitalize()
        if InpSymbols:
            InpSymbols = 1

        LongString = str(InpString)
        SplitString = LongString.split()

    #   print(f"LongString: {LongString}\nSplitString: {SplitString}\nLetterString: {LetterString}")

        FixedString = ""

        for Count in range(len(SplitString)):
            CurWord = ""
            for CurLetter in SplitString[Count]:
                if CurLetter == "." and InpSymbols == 0:
                    CurWord += "_"
                elif CurLetter not in SpecialCharacters or InpSymbols == 1:
                    CurWord += CurLetter

            if InpPriority == "Num":
                try:
                    CurWord = w2n.word_to_num(CurWord)
                except ValueError:
                    CurWord = CurWord.capitalize()

            elif InpPriority == "Str":
                if CurWord.isdigit():
                    CurWord = num2words(CurWord)
                CurWord = CurWord.capitalize()

            FixedString += str(CurWord)
                
        return FixedString



def Complexify(InpString = "Sorry,YouDidn'tAddAnyArgsToComplexify()!", InpPriority = "Str", /):
    """
    Complexify() relies on num2words, and word2number. Make sure to install those via pip first.
    >Complexify() tries to Complexifyes a bare string as much as it can.
    >(e.g. "HiThere" into "Hi there.")
    >
    >- InpString: The string you want to Complexify(). Make sure that it's a string.
    >- InpPriority: Has two values to choose from; 
    >    - 'Num': Which will make words into numbers (e.g. 'Two' into 2), and 
    >    - 'Str': Which will make numbers into words (e.g. 2 into 'Two').
    """

    if not isinstance(InpString, str) or not isinstance(InpPriority, str):
        return("Sorry, you didn't input a string into Simplify()!")
    else:
        InpPriority = InpPriority.capitalize()

        LongString = str(InpString)
        SplitString = re.split(r'(?<=[a-z])(?=[A-Z])', LongString)

        Capitalise = True

        FixedString = ""

        for Count in range(len(SplitString)):
            CurWord = ""
            for CurLetter in SplitString[Count]:
                CurLetter = CurLetter.lower()
                if CurLetter == "_":
                    CurWord += ". "
                    Capitalise = True
                elif CurLetter == ",":
                    CurWord += ", "

                elif InpPriority == "Str" and CurLetter.isdigit():
                        CurLetter = num2words(CurLetter)
                        CurWord += f" {CurLetter} "

                else:
                    if Capitalise:
                        CurLetter = CurLetter.upper()
                        Capitalise = False

                    CurWord += CurLetter

                if InpPriority == "Num":
                    try:
                        CurWord = w2n.word_to_num(CurWord)
                    except ValueError:
                        pass

            CurWord = str(CurWord)
            CurWord += " "
            FixedString += CurWord

        return FixedString[:-1]+"."



def CheckType(InpItem):
    """
    CheckType() checks the type of a variable and returns it.
    (e.g. "Hello" would return "Str")
    """

    if isinstance(InpItem, int):
        ItemType = "Int"
    elif isinstance(InpItem, str):
        ItemType = "Str"
    elif isinstance(InpItem, float):
        ItemType = "Float"
    elif isinstance(InpItem, list):
        ItemType = "List"
    elif isinstance(InpItem, dict):
        ItemType = "Dict"
    elif isinstance(InpItem, tuple):
        ItemType = "Tuple"
    elif isinstance(InpItem, bool):
        ItemType = "Bool"
    else:
        ItemType = "Unknown"
    return ItemType



def PrettyPrint(InpItem = "No variable was given in PrettyPrint()!", Name = ""):
    """
    PrettyPrint() prints out a variable in a more informative and pretty way.
    (e.g. "Test (Str): Hi" instead of "Test <class 'str'> Hi")
    
    >- Name: The name of the variable you want to write. Defaults to nothing.
    >- InpItem: The actual variable you want to print. 
    """

    ItemType = CheckType(InpItem)

    print(f"{Name} ({ItemType}): ",end='')
    try:
        if len(InpItem) > 1 and not ItemType == "Str":
            print()
            for Count in range(len(InpItem)):
                print(f"    {Count} ({CheckType(InpItem[Count])}): {InpItem[Count]}")
        else:
            print(InpItem)
    
    except:
        print(InpItem)



#----===|   END   |===----#
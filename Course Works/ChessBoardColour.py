# ChessBoardColour.py
#
# author: Kaoru
# date: 10.08.23

row = int(input("Enter number\n"))
column = input("Enter letter\n")

if (row % 2 == 0
    and column == "b" or "d" or "f" or "h"):
          print("White")
else:
    print("Black")
    

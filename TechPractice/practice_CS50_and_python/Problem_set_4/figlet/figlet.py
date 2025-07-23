from pyfiglet import Figlet
import sys
import random 

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" or sys.argv[1] != "--font" and sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")
    else:
        f = figlet.setFont(font=sys.argv[2])
elif len(sys.argv) == 2:
    sys.exit("Invalid Usage")
elif len(sys.argv) > 3:
    sys.exit("Invalid Usage")
else:
    f = figlet.setFont(font=(random.choice(fonts)))

U = input("Input: ")
print(figlet.renderText(U))

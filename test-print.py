import win32print
import win32ui
from PIL import Image, ImageWin

PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111

file_name = "IMG_2851.jpg"
img = Image.open(file_name)

printer_name = win32print.GetDefaultPrinter()

dc = win32ui.CreateDC()
dc.CreatePrinterDC(printer_name)

# Calculate the scaling factor to fit the image to the printable area
scaling_factor = min(dc.GetDeviceCaps(PHYSICALWIDTH)/img.width,dc.GetDeviceCaps(PHYSICALHEIGHT)/img.height)

# Calculate the position and size of the image on the page
x = (dc.GetDeviceCaps(PHYSICALWIDTH)-img.width * scaling_factor)/2
y = (dc.GetDeviceCaps(PHYSICALHEIGHT)-img.height * scaling_factor)/2
width = img.width * scaling_factor
height = img.height * scaling_factor

if img.size[0] < img.size[1]:
    img = img.rotate(90)

dc.StartDoc(file_name)
dc.StartPage()

dib = ImageWin.Dib(img)
dib.draw(dc.GetHandleOutput(), (int(x), int(y), int(x + width), int(y + height)))

dc.EndPage()
dc.EndDoc()
dc.DeleteDC()

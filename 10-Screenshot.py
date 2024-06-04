#Program to take screenshot
import pyscreenshot
image= pyscreenshot.grab()
#Display
image.show()
#save
image.save("screenshot.png")

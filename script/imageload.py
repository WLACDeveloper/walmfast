from PIL.ImageTk import PhotoImage
from settings import window_and_objects as winaobj

background = PhotoImage(file=winaobj.BACKGROUND)
frame = PhotoImage(file=winaobj.FRAME)
android = PhotoImage(file=winaobj.ANDROID)
menu = PhotoImage(file=winaobj.MENU)
volume_on = PhotoImage(file=winaobj.VOLUME_ON)
volume_off = PhotoImage(file=winaobj.VOLUME_OFF)
close = PhotoImage(file=winaobj.CLOSE)
install_firmware_complect = PhotoImage(file=winaobj.INSTALL_FIRMWARE_COMPLECT)
location_music = PhotoImage(file=winaobj.LOCATION_MUSIC)
tux = PhotoImage(file=winaobj.TUX)
debian = PhotoImage(file=winaobj.DEBIAN)
arch = PhotoImage(file=winaobj.ARCH)
windows = PhotoImage(file=winaobj.WINDOWS)
recovery = PhotoImage(file=winaobj.RECOVERY)
bootloader=PhotoImage(file=winaobj.BOOTLOADER)
fastbootd = PhotoImage(file=winaobj.FASTBOOTD)
system = PhotoImage(file=winaobj.SYSTEM)
adb = PhotoImage(file=winaobj.ADB)
unlock_bootloader = PhotoImage(file=winaobj.UNLOCK)
lock_bootloader = PhotoImage(file=winaobj.LOCK)
flash = PhotoImage(file=winaobj.FLASH)
approve_custom_load = PhotoImage(file=winaobj.APPROVE_CUSTOM_LOAD)
wipe_data = PhotoImage(file=winaobj.WIPE_DATA)
search_gsi = PhotoImage(file=winaobj.SEARCH_GSI)
product = PhotoImage(file=winaobj.PRODUCT)

def load_image(image_path):
    image = PhotoImage(file=image_path)
    return image
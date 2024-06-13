import qrcode as qr
qr_kod = qr.QRCode(
    version=1, 
    error_correction=qr.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4,  
)
qr_kod.add_data("https://www.palestinercs.org/ar")
qr_kod.make(fit=True)

qr_img = qr_kod.make_image(fill_color="red", back_color="white")
qr_img.save("filistin_kızılay.png")
qr_kod = qr.QRCode(
    version=1,  
    error_correction=qr.constants.ERROR_CORRECT_L,  
    box_size=10, 
    border=4,  
)
qr_kod.add_data("https://ihh.org.tr/filistin-gazze")
qr_kod.make(fit=True)
qr_img = qr_kod.make_image(fill_color="green", back_color="white")
qr_img.save("ihh_help.png")
qr_kod = qr.QRCode(
    version=1,  
    error_correction=qr.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=4, 
)
qr_kod.add_data("https://www.kktkizilayi.org/bagis-online/gazzede-insanlik-olmesin")
qr_kod.make(fit=True)
qr_img = qr_kod.make_image(fill_color="Orange", back_color="white")
qr_img.save("cyrps_red.png")
qr_kod = qr.QRCode(
    version=1,  
    error_correction=qr.constants.ERROR_CORRECT_L,  
    box_size=10,
    border=4,  
)
qr_kod.add_data("https://bagis.kizilay.org.tr/tr/bagis/bagisyap/32/filistin-genel-bagisi")
qr_kod.make(fit=True)
qr_img = qr_kod.make_image(fill_color="Blue", back_color="white")
qr_img.save("turkiyye_red.png")
qr_kod = qr.QRCode(
    version=1, 
    error_correction=qr.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  
)
qr_kod.add_data("https://www.egyptianrc.org/Arabic/ERC-Activities/Activities/ActivityDetails/84")
qr_kod.make(fit=True)
qr_img = qr_kod.make_image(fill_color="Brown", back_color="white")
qr_img.save("egypt_red.png")
#qrcode for websites#
"""
Egyptian Red Crescent
Turkey Red Crescent and IHH
Palastine Red Crescent
Cyrps Red Crescent
"""
###Free_Palastine###
###Love_Palastine###
#I'm from Turkey.#
"""
There is a massacre in Palestine.
I prepared this program so that
this massacre would not be forgotten.
Do not remain silent while there is a massacre!
Thank you for reviewing the program.
"""
##########################################################



























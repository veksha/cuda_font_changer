import os
import time
from cudatext import *
import cudax_lib as apx

FONTS = [font for font in app_proc(PROC_ENUM_FONTS, '') if not font.startswith('@')]

class Command:

    def __init__(self):
        pass

    def next_font(self):
        current_font = apx.get_opt('font_name')
        idx = FONTS.index(current_font)
        if idx+1 >= len(FONTS):
            return
        idx+=1
        font = FONTS[idx]
        ed.set_prop(PROP_FONT, font)
        apx.set_opt('font_name',font)
        print('{}. {}'.format(idx+1,font))
        time.sleep(0.01) # sleep to help saving config! important

    def previous_font(self):
        current_font = apx.get_opt('font_name')
        idx = FONTS.index(current_font)
        if idx == 0:
            return
        idx-=1
        font = FONTS[idx]
        ed.set_prop(PROP_FONT, font)
        apx.set_opt('font_name',font)
        print('{}. {}'.format(idx+1,font))
        time.sleep(0.01) # sleep to help saving config! important

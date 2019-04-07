init +1 python:
    #def emod_setup():
    #    global eui

    # Global var bto remember UI usage settings, such as options tab
    eui = EnhancementModUI()

    #emod_setup()
    #eui = EnhancementModUI()
    #show_sidemenu = False
    #option_show = 1
    #tty = -5000
    #english_battle_voices = True
    if persistent.eui_file_page == None:
        persistent.eui_file_page = 1
    config.thumbnail_width = 266
    config.thumbnail_height = 150
    #eui_english_battle_voices = True

    #eui = None
    #if not hasattr(store,'eui') or eui is None:
    #eui = EnhancementModUI()
    #if not hasattr(store,'eui'):
    #    eui = EnhancementModUI()
    #try:
    #    int(FilePageName())
    #    FilePage(int(persistent.eui_file_page))
    #except:
    #    pass

    #style.say_vbox.xfill = False

init +1:
    image ctc:
        "UI/ctc.png"
        xpos 1800 ypos 1000

### History Init

init python:
    #httx = 0
    #htty = -5000
    eui_history_box = 0
#init 100 python:
#    eui.setoptions_ypos(setoptions)
init +1 python:
    # Keep track of the old callback so it can still be called
    eui_original_label_callback = config.label_callback

    def eui_label_callback(label, abnormal):
        # Make sure to call the original label callback too
        if eui_original_label_callback != None:
            eui_original_label_callback(label, abnormal)

        # Update if the quick menu is visible or not
        eui.manage_quick_menu_visibility(label)

    config.label_callback = eui_label_callback

init +1 python:
    # Remember what file page we're on, even when we switch to "auto" or "quick" pages
    # We'll remember foreverandeverandeverandever-until you uninstall the mod(?)
    if persistent.eui_file_page == None:
        persistent.eui_file_page = 1

#init 100 python:
#    addon_scenes.append(BonusItem("cg_epi2_cg2","My Test Addon","start",1))

init +1:
    define eui_battle_voice_option = False
    define eui_battle_voice_object = None
    define eui_battle_voice_field = None

    image ctc:
        "UI/ctc.png"
        xpos 1800 ypos 1000

    style upgrade is default:
        font "Menu/euphemia.ttf"
        size 22
    style upgrade_label is label:
        font "Menu/euphemia.ttf"
        size 22
    style upgrade_text is text:
        font "Menu/euphemia.ttf"
        size 22
    style upgrade_textbutton is button:
        font "Menu/euphemia.ttf"
        #text_size 22
    style upgrade_button_text is button_text:
        font "Menu/euphemia.ttf"
        size 22
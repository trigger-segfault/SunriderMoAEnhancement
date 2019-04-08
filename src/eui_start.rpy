init python:
    # Keep track of the old callback so it can still be called
    eui_original_label_callback = config.label_callback

    def eui_label_callback(label, abnormal):
        # Make sure to call the original label callback too
        if eui_original_label_callback != None:
            eui_original_label_callback(label, abnormal)

        if label == 'start':
            # Hackish way to guarantee the gameprefs screen is on the right tab
            eui.option_show = 3
        if label == 'start' or label == 'after_load':
            # Make sure Enhancement mod settings are setup for the game
            if not hasattr(store,'emod'):
                emod = EnhancementMod()
            #renpy.show_screen('quick_menu')
            
    config.label_callback = eui_label_callback
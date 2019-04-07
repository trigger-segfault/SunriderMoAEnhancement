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
            emod = EnhancementMod()
            #renpy.show_screen('quick_menu')
            
    config.label_callback = eui_label_callback

# Make sure this label exists so that it is called, it can easily be overwritten
#init -2:
#    label before_main_menu:
        #if not hasattr(store,'BM'):
        #    $BM = Battle()
#        return

#label before_main_menu:
    #if not hasattr(store,'BM'):
    #    $BM = Battle()
#    return
#label eui_before_main_menu: #this is run even if the player quits back to main menu and is required to properly set up the BM
#    if not hasattr(store,'BM'):
#        $store.BM = Battle()
#    if not hasattr(store,'eui'):
#        $store.eui = EnhancementModUI()
#    return
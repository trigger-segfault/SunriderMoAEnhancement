init +2:
    ##############################################################################
    # Main Menu
    #
    # Screen that's used to display the main menu, when Ren'Py first starts
    # http://www.renpy.org/doc/html/screen_special.html#main-menu

    screen main_menu:

        if not renpy.showing("bg cera") is True:
            $ renpy.scene()
            # Fade in so that we don't see this for a split second before the splash screen
            $ renpy.show("bg cera", [tr_fadein(1.0)])

        add "UI/black.jpg"

        if not hasattr(store,'BM'):
            $store.BM = Battle()
            $store.MasterBM = store.BM
            $store.BM.phase = 'Player'
        if not hasattr(store,'emod'):
            $store.emod = EnhancementMod()

        imagemap:
            ground "Menu/menu_default.jpg"
            idle "Menu/menu_default.jpg"
            #insensitive "Menu/menu_inactive.jpg"
            insensitive "UI/eui_menu_inactive_bar.jpg"
            hover "Menu/menu_hover.jpg"

            hotspot (160, 405, 133+ 9+3, 50) action Show('campaigns', transition=dissolve)
            hotspot ( 80, 472, 208+14+3, 50) action FileLoad("1", page="auto", confirm=False)
            hotspot (171, 537, 118+13+3, 50) action ShowMenu('load')
            hotspot ( 92, 598, 200+10+3, 50) action ShowMenu('preferences')
            hotspot (138, 666, 151+13+3, 50) action ShowMenu('gallery_back')
            hotspot (186, 730, 108+ 8+3, 50) action Quit()

        text '[config.version]' xpos 0.01 ypos 0.98 size 12

        if CENSOR == False:

            text ' RESTORATION PATCH DETECTED' xpos 0.01 ypos 0.958 size 15

        if CENSOR == True:

            text ' VANILLA EDITION' xpos 0.01 ypos 0.958 size 15

    screen campaigns:
    
        imagemap:
            ground "Menu/mainmenu_campaign.png"
            idle "Menu/mainmenu_campaign.png"
            insensitive "Menu/mainmenu_campaign.png"
            hover "Menu/mainmenu_campaign_hover.png"
            alpha False
            
            hotspot (300, 385, 230, 40) action Start()
            hotspot (300, 425, 350, 40) action Show("yesno_prompt", None,"Welcome to the Mask of Arcadius campaign. It is highly suggested that you complete the First Arrival campaign before playing Mask of Arcadius.\nDo you want to continue?", (Hide("yesno_prompt"),Show("history")), Hide("yesno_prompt"))
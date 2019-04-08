init +2:
    ##############################################################################
    # Quick Menu
    #
    # A screen that's included by the default say screen, and adds quick access to
    # several useful functions.
    screen quick_menu():

        # Add an in-game quick menu.
        hbox:
            style_group "quick"

            xalign 1.0
            yalign 1.0

            textbutton _("Back") action Rollback()
            if BM.phase == 'Player':
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
            textbutton _("Skip") action Skip()
            textbutton _("F.Skip") action Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Prefs") action ShowMenu('preferences')

    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

    #screen prolog:
    #    
    #    frame:
    #        
    #        background None
    #        xpos 200 xmaximum 1520 yalign 0.5
    #        text what id "what" font "Fonts/ShareTech-Regular.ttf" size 35
        
    screen quick_menu:
        if not hasattr(BM,'supress_menu'):
            $BM.supress_menu = False
        if (BM.phase == 'Player' or BM.phase == 'formation') and (BM.battlemode == False or BM.supress_menu == False):
            key "mouseup_3" action If(True,true=(FileTakeScreenshot(),If(eui.show_sidemenu, true=(Hide("sidebuttons"),SetField(eui, "show_sidemenu", False)), false=(Show("sidebuttons"),SetField(eui, "show_sidemenu", True)))),false=NullAction())
        elif BM.supress_menu and BM.selected is None:
            key "mouseup_3" action SetField(BM,'supress_menu',False)
        
        zorder 350
        imagebutton:
            xpos 1755
            idle "UI/menu.png"
            hover tr_hoverglow("UI/menu.png")
            
            activate_sound "sound/button1.ogg"
            action If((BM.phase == 'Player' or BM.phase == 'formation'),[FileTakeScreenshot(),If(eui.show_sidemenu, true=(Hide("sidebuttons"),SetField(eui, "show_sidemenu", False)), false=(Show("sidebuttons"),SetField(eui, "show_sidemenu", True)))],NullAction())
        
    screen sidebuttons:
        
        zorder 300
        
        if eui.show_sidemenu == True:
            imagebutton:
                idle "UI/menu_qsave.png"
                hover tr_hoverglow("UI/menu_qsave.png")
                
                activate_sound "sound/button1.ogg"
                action (QuickSave(message='                                   Quick save complete.', newest=False),Hide("sidebuttons"),SetField(eui, "show_sidemenu", False))
                at tr_sidemenu(100)
            imagebutton:
                idle "UI/menu_save.png"
                hover tr_hoverglow("UI/menu_save.png")
                
                activate_sound "sound/button1.ogg"
                action Show("save"),FileTakeScreenshot()
                #action If(show_save, true=(Hide("save"),SetVariable("show_save",False)), false=(Show("save"),SetVariable("show_save",True)))
                at tr_sidemenu(150)
            imagebutton:
                idle "UI/menu_load.png"
                hover tr_hoverglow("UI/menu_load.png")
                
                activate_sound "sound/button1.ogg"
                action Show("load")
                #action If(show_load, true=(Hide("load"),SetVariable("show_load",False)), false=(Show("load"),SetVariable("show_load",True)))
                at tr_sidemenu(200)
            imagebutton:
                idle "UI/menu_options.png"
                hover tr_hoverglow("UI/menu_options.png")
                
                activate_sound "sound/button1.ogg"
                action Show("preferences")
                #action If(show_preference, true=(Hide("preferences"),SetVariable("show_preference",False)), false=(Show("preferences"),SetVariable("show_preference",True)))
                at tr_sidemenu(250)
            
            $hideui_action = NullAction() if (BM.battlemode or 'victory2' in renpy.get_showing_tags('screens')) else HideInterface()
            imagebutton:
                idle "UI/menu_hideui.png"
                hover tr_hoverglow("UI/menu_hideui.png")
                
                activate_sound "sound/button1.ogg"
                action hideui_action
                at tr_sidemenu(300)
            
            imagebutton:
                idle "UI/menu_auto.png"
                hover tr_hoverglow("UI/menu_auto.png")
                
                activate_sound "sound/button1.ogg"
                action Preference("auto-forward", "toggle")
                at tr_sidemenu(350)
            
            $screenshot_action = Screenshot() if (BM.battlemode or 'victory2' in renpy.get_showing_tags('screens')) else (HideInterface(),Screenshot())
            imagebutton:
                idle "UI/menu_screenshot.png"
                hover tr_hoverglow("UI/menu_screenshot.png")
                
                activate_sound "sound/button1.ogg"
                action screenshot_action
                at tr_sidemenu(400)
                
            imagebutton:
                idle "UI/menu_quit.png"
                hover tr_hoverglow("UI/menu_quit.png")
                
                activate_sound "sound/button1.ogg"
                action MainMenu(confirm=True)
                at tr_sidemenu(450)
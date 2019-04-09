init +2:
    ##############################################################################
    # Preferences
    #
    # Screen that allows the user to change the preferences.
    # http://www.renpy.org/doc/html/screen_special.html#prefereces

    screen preferences:
        zorder 1200
        modal True
        
        #if not hasattr(store,'BM'):
        #    $store.BM = Battle()
        #    $store.MasterBM = store.BM
        #    $store.BM.phase = 'Player'
            
        #drag:

        #    drag_name "drag_prefs"
        #    drag_handle (0,0,450,44)
        #    xpos 360 ypos 200
        #    drag_offscreen False
        
        fixed at tr_fadein(0):
            xmaximum 1196 ymaximum 630
            xalign 0.5 yalign 0.5

            add "UI/options_base.png"

            imagebutton:
                xpos 565 ypos 50
                idle "UI/options_main.png"
                hover tr_hoverglow("UI/options_main.png")
                selected_idle "UI/options_main_select.png"
                selected_hover tr_hoverglow("UI/options_main_select.png")
                action SetField(eui,"option_show",1)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            imagebutton:
                xpos 754 ypos 50
                idle "UI/options_audio.png"
                hover tr_hoverglow("UI/options_audio.png")
                selected_idle "UI/options_audio_select.png"
                selected_hover tr_hoverglow("UI/options_audio_select.png")
                action SetField(eui,"option_show",2)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            imagebutton:
                xpos 943 ypos 50
                idle "UI/options_gameplay.png"
                hover tr_hoverglow("UI/options_gameplay.png")
                selected_idle "UI/options_gameplay_select.png"
                selected_hover tr_hoverglow("UI/options_gameplay_select.png")
                action SetField(eui,"option_show",3)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"

            imagebutton:
                xpos 1133 ypos 52
                idle "UI/load_cancel.png"
                hover tr_hoverglow("UI/load_cancel.png")            
                action (Hide("preferences"),Hide("gameprefs"))#,Hide("option_main"),Hide("option_audio"),Hide("option_gameplay"),SetVariable("show_preference",False))
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            if eui.option_show == 1:

                add "UI/eui_options_main_text.png"

                imagebutton:
                    xpos 86 ypos 165
                    idle "UI/options_main_fullscreen.png"
                    hover tr_hoverglow("UI/options_main_fullscreen.png")
                    selected_idle "UI/options_main_fullscreen_select.png"
                    selected_hover tr_hoverglow("UI/options_main_fullscreen_select.png")
                    action Preference("display", "fullscreen")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 165
                    idle "UI/options_main_window.png"
                    hover tr_hoverglow("UI/options_main_window.png")
                    selected_idle "UI/options_main_window_select.png"
                    selected_hover tr_hoverglow("UI/options_main_window_select.png")
                    action [ Preference("display", "window"), SelectedIf(not _preferences.fullscreen) ]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 86 ypos 360
                    idle "UI/options_main_skipall.png"
                    hover tr_hoverglow("UI/options_main_skipall.png")
                    selected_idle "UI/options_main_skipall_select.png"
                    selected_hover tr_hoverglow("UI/options_main_skipall_select.png")
                    action Preference("skip", "all")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 360
                    idle "UI/options_main_skipseen.png"
                    hover tr_hoverglow("UI/options_main_skipseen.png")
                    selected_idle "UI/options_main_skipseen_select.png"
                    selected_hover tr_hoverglow("UI/options_main_skipseen_select.png")
                    action Preference("skip", "seen")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 86 ypos 428
                    idle "UI/options_main_keepskipping.png"
                    hover tr_hoverglow("UI/options_main_keepskipping.png")
                    selected_idle "UI/options_main_keepskipping_select.png"
                    selected_hover tr_hoverglow("UI/options_main_keepskipping_select.png")
                    action Preference("after choices", "skip")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 428
                    idle "UI/options_main_stop.png"
                    hover tr_hoverglow("UI/options_main_stop.png")
                    selected_idle "UI/options_main_stop_select.png"
                    selected_hover tr_hoverglow("UI/options_main_stop_select.png")
                    action Preference("after choices", "stop")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                #imagebutton:
                #    xpos 590 ypos 460
                #    idle "UI/usa_base.jpg"
                #    hover "UI/usa_hover.jpg"
                #    selected_idle "UI/usa_select.jpg"
                #    selected_hover "UI/usa_select_hover.jpg"
                #    action Language(None)
                #    hover_sound "sound/hover1.ogg"
                #    activate_sound "sound/button1.ogg"

                #imagebutton:
                #    xpos 720 ypos 460
                #    idle "UI/japan_base.jpg"
                #    hover "UI/japan_hover.jpg"
                #    selected_idle "UI/japan_select.jpg"
                #    selected_hover "UI/japan_select_hover.jpg"
                #    action Language("japanese")
                #    hover_sound "sound/hover1.ogg"
                #    activate_sound "sound/button1.ogg"

                bar:
                    xpos 600
                    ypos 165
                    xmaximum 300
                    value Preference("text speed")
                bar:
                    xpos 600
                    ypos 350
                    xmaximum 300
                    value Preference("auto-forward time")

            if eui.option_show == 2:

                if eui_battle_voice_option == True:
                    add "UI/eui_options_audio_text.png"
                else:
                    add "UI/eui_options_audio_text_no_battle_voice.png"

                bar:
                    xpos 60
                    ypos 160
                    xmaximum 300
                    value Preference("music volume")
                bar:
                    xpos 60
                    ypos 250
                    xmaximum 300
                    value Preference("sound volume")
                bar:
                    xpos 60
                    ypos 340
                    xmaximum 300
                    value Preference("voice volume")

                imagebutton:
                    xpos 450 ypos 250
                    idle "UI/options_audio_test.png"
                    hover tr_hoverglow("UI/options_audio_test.png")
                    selected_idle "UI/options_audio_test_select.png"
                    selected_hover tr_hoverglow("UI/options_audio_test_select.png")
                    action Play("sound", "sound/explosion1.ogg", selected=True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 450 ypos 340
                    idle "UI/options_audio_test.png"
                    hover tr_hoverglow("UI/options_audio_test.png")
                    selected_idle "UI/options_audio_test_select.png"
                    selected_hover tr_hoverglow("UI/options_audio_test_select.png")
                    action Play("voice", "sound/Voice/asa_Sel_07.ogg", selected=True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                #english battle voices
                if eui_battle_voice_option == True:
                    imagebutton:
                        xpos 690 ypos 175
                        idle "UI/options_audio_libdayvoice.png"
                        hover tr_hoverglow("UI/options_audio_libdayvoice.png")
                        selected_idle "UI/options_audio_libdayvoice_selected.png"
                        selected_hover tr_hoverglow("UI/options_audio_libdayvoice_selected.png")
                        if eui_battle_voice_object == None:
                            action SetVariable(eui_battle_voice_field,False)
                        else:
                            action SetField(eval(eui_battle_voice_object),eui_battle_voice_field,False)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"

                    imagebutton:
                        xpos 690 ypos 225
                        idle "UI/options_audio_moavoice.png"
                        hover tr_hoverglow("UI/options_audio_moavoice.png")
                        selected_idle "UI/options_audio_moavoice_selected.png"
                        selected_hover tr_hoverglow("UI/options_audio_moavoice_selected.png")
                        if eui_battle_voice_object == None:
                            action SetVariable(eui_battle_voice_field,True)
                        else:
                            action SetField(eval(eui_battle_voice_object),eui_battle_voice_field,True)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"

                #dialogue voicing
                #imagebutton:
                #    xpos 690 ypos 340
                #    idle "UI/checkbox.png"
                #    hover tr_hoverglow("UI/checkbox.png")
                #    selected_idle "UI/checkbox_select.png"
                #    selected_hover tr_hoverglow("UI/checkbox_select.png")
                #    action ToggleField(config, 'auto_voice',true_value='sound/Voice/{id}.ogg', false_value=False)
                #    hover_sound "sound/hover1.ogg"
                #    activate_sound "sound/button1.ogg"

            if eui.option_show == 3:

                add "UI/eui_options_gameplay_text.png"

                default tt = Tooltip("")

                imagebutton:
                    xpos 90 ypos 170
                    idle "UI/options_gameplay_waifu.png"
                    hover tr_hoverglow("UI/options_gameplay_waifu.png")
                    selected_idle "UI/options_gameplay_waifu_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_waifu_select.png")
                    hovered tt.Action("Reduces the difficulty to near nill\nfor a stress free experience."),SetField(eui,"tty",170)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 0)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 220
                    idle "UI/options_gameplay_casual.png"
                    hover tr_hoverglow("UI/options_gameplay_casual.png")
                    selected_idle "UI/options_gameplay_casual_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_casual_select.png")
                    hovered tt.Action("Easy for newcomers and people not\ninterested in strategy."),SetField(eui,"tty",220)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 1)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 270
                    idle "UI/options_gameplay_ensign.png"
                    hover tr_hoverglow("UI/options_gameplay_ensign.png")
                    selected_idle "UI/options_gameplay_ensign_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_ensign_select.png")
                    hovered tt.Action("Average difficulty for people who want\na reasonable challenge."),SetField(eui,"tty",270)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 2)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 320
                    idle "UI/options_gameplay_captain.png"
                    hover tr_hoverglow("UI/options_gameplay_captain.png")
                    selected_idle "UI/options_gameplay_captain_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_captain_select.png")
                    action SetVariable("Difficulty", 3)
                    hovered tt.Action("Challenging but fair. Your mistakes\nwill be punished without mercy."),SetField(eui,"tty",320)
                    unhovered SetField(eui,"tty",-5000)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 370
                    idle "UI/options_gameplay_admiral.png"
                    hover tr_hoverglow("UI/options_gameplay_admiral.png")
                    selected_idle "UI/options_gameplay_admiral_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_admiral_select.png")
                    hovered tt.Action("For people who are good at this game."),SetField(eui,"tty",370)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 4)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 420
                    idle "UI/options_gameplay_spacewhale.png"
                    hover tr_hoverglow("UI/options_gameplay_spacewhale.png")
                    selected_idle "UI/options_gameplay_spacewhale_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_spacewhale_select.png")
                    hovered tt.Action("Why would you do this to yourself..."),SetField(eui,"tty",420)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 5)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 600 ypos 168
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM,"show_tooltips",true_value=True, false_value=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 600 ypos 274
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM,"edgescroll",true_value=(100,800), false_value=(0,0))
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                #text "{k=0.5}SHOW BATTLE LOG{/k}":
                #    xpos 590 ypos 340
                #    font "Fonts/mplus-2p-regular.ttf"
                #    size 20
                #    color "#F7F7F7"


                imagebutton:
                    xpos 600 ypos 380
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM,"show_battle_log",true_value=True, false_value=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                frame:

                    xpos 360
                    ypos eui.tty
                    background "#000000"

                    text tt.value:
                        font "Fonts/ShareTech-Regular.ttf"
                        size 20
                        color "#F7F7F7"

    screen gameprefs:
        zorder 2000
        modal True

        # Nice little method to set eui.option_show = 3 only ONCE per screen show
        default eui_gameprefs_init = False
        if eui_gameprefs_init == False:
            $ eui.option_show = 3
        $ eui_gameprefs_init = True

        #if not hasattr(store,'BM'):
        #    $store.BM = Battle()
        #    $store.MasterBM = store.BM
        #    $store.BM.phase = 'Player'
            
        #drag:

        #    drag_name "drag_prefs"
        #    drag_handle (0,0,450,44)
        #    xpos 360 ypos 200
        #    drag_offscreen False
        
        fixed at tr_fadein(0):
            xmaximum 1196 ymaximum 630
            xalign 0.5 yalign 0.5

            add "UI/options_base.png"

            imagebutton:
                xpos 565 ypos 50
                idle "UI/options_main.png"
                hover tr_hoverglow("UI/options_main.png")
                selected_idle "UI/options_main_select.png"
                selected_hover tr_hoverglow("UI/options_main_select.png")
                action SetField(eui,"option_show",1)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            imagebutton:
                xpos 754 ypos 50
                idle "UI/options_audio.png"
                hover tr_hoverglow("UI/options_audio.png")
                selected_idle "UI/options_audio_select.png"
                selected_hover tr_hoverglow("UI/options_audio_select.png")
                action SetField(eui,"option_show",2)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            imagebutton:
                xpos 943 ypos 50
                idle "UI/options_gameplay.png"
                hover tr_hoverglow("UI/options_gameplay.png")
                selected_idle "UI/options_gameplay_select.png"
                selected_hover tr_hoverglow("UI/options_gameplay_select.png")
                action SetField(eui,"option_show",3)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"

            imagebutton:
                xpos 1133 ypos 52
                idle "UI/load_cancel.png"
                hover tr_hoverglow("UI/load_cancel.png")            
                action (Hide("preferences"),Hide("gameprefs"))#,Hide("option_main"),Hide("option_audio"),Hide("option_gameplay"),SetVariable("show_preference",False))
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            if eui.option_show == 1:

                add "UI/eui_options_main_text.png"

                imagebutton:
                    xpos 86 ypos 165
                    idle "UI/options_main_fullscreen.png"
                    hover tr_hoverglow("UI/options_main_fullscreen.png")
                    selected_idle "UI/options_main_fullscreen_select.png"
                    selected_hover tr_hoverglow("UI/options_main_fullscreen_select.png")
                    action Preference("display", "fullscreen")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 165
                    idle "UI/options_main_window.png"
                    hover tr_hoverglow("UI/options_main_window.png")
                    selected_idle "UI/options_main_window_select.png"
                    selected_hover tr_hoverglow("UI/options_main_window_select.png")
                    action [ Preference("display", "window"), SelectedIf(not _preferences.fullscreen) ]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 86 ypos 360
                    idle "UI/options_main_skipall.png"
                    hover tr_hoverglow("UI/options_main_skipall.png")
                    selected_idle "UI/options_main_skipall_select.png"
                    selected_hover tr_hoverglow("UI/options_main_skipall_select.png")
                    action Preference("skip", "all")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 360
                    idle "UI/options_main_skipseen.png"
                    hover tr_hoverglow("UI/options_main_skipseen.png")
                    selected_idle "UI/options_main_skipseen_select.png"
                    selected_hover tr_hoverglow("UI/options_main_skipseen_select.png")
                    action Preference("skip", "seen")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 86 ypos 428
                    idle "UI/options_main_keepskipping.png"
                    hover tr_hoverglow("UI/options_main_keepskipping.png")
                    selected_idle "UI/options_main_keepskipping_select.png"
                    selected_hover tr_hoverglow("UI/options_main_keepskipping_select.png")
                    action Preference("after choices", "skip")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 428
                    idle "UI/options_main_stop.png"
                    hover tr_hoverglow("UI/options_main_stop.png")
                    selected_idle "UI/options_main_stop_select.png"
                    selected_hover tr_hoverglow("UI/options_main_stop_select.png")
                    action Preference("after choices", "stop")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                #imagebutton:
                #    xpos 590 ypos 460
                #    idle "UI/usa_base.jpg"
                #    hover "UI/usa_hover.jpg"
                #    selected_idle "UI/usa_select.jpg"
                #    selected_hover "UI/usa_select_hover.jpg"
                #    action Language(None)
                #    hover_sound "sound/hover1.ogg"
                #    activate_sound "sound/button1.ogg"

                #imagebutton:
                #    xpos 720 ypos 460
                #    idle "UI/japan_base.jpg"
                #    hover "UI/japan_hover.jpg"
                #    selected_idle "UI/japan_select.jpg"
                #    selected_hover "UI/japan_select_hover.jpg"
                #    action Language("japanese")
                #    hover_sound "sound/hover1.ogg"
                #    activate_sound "sound/button1.ogg"

                bar:
                    xpos 600
                    ypos 165
                    xmaximum 300
                    value Preference("text speed")
                bar:
                    xpos 600
                    ypos 350
                    xmaximum 300
                    value Preference("auto-forward time")

            if eui.option_show == 2:

                if eui_battle_voice_option == True:
                    add "UI/eui_options_audio_text.png"
                else:
                    add "UI/eui_options_audio_text_no_battle_voice.png"

                bar:
                    xpos 60
                    ypos 160
                    xmaximum 300
                    value Preference("music volume")
                bar:
                    xpos 60
                    ypos 250
                    xmaximum 300
                    value Preference("sound volume")
                bar:
                    xpos 60
                    ypos 340
                    xmaximum 300
                    value Preference("voice volume")

                imagebutton:
                    xpos 450 ypos 250
                    idle "UI/options_audio_test.png"
                    hover tr_hoverglow("UI/options_audio_test.png")
                    selected_idle "UI/options_audio_test_select.png"
                    selected_hover tr_hoverglow("UI/options_audio_test_select.png")
                    action Play("sound", "sound/explosion1.ogg", selected=True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 450 ypos 340
                    idle "UI/options_audio_test.png"
                    hover tr_hoverglow("UI/options_audio_test.png")
                    selected_idle "UI/options_audio_test_select.png"
                    selected_hover tr_hoverglow("UI/options_audio_test_select.png")
                    action Play("voice", "sound/Voice/asa_Sel_07.ogg", selected=True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                #english battle voices
                if eui_battle_voice_option == True:
                    imagebutton:
                        xpos 690 ypos 175
                        idle "UI/options_audio_libdayvoice.png"
                        hover tr_hoverglow("UI/options_audio_libdayvoice.png")
                        selected_idle "UI/options_audio_libdayvoice_selected.png"
                        selected_hover tr_hoverglow("UI/options_audio_libdayvoice_selected.png")
                        if eui_battle_voice_object == None:
                            action SetVariable(eui_battle_voice_field,False)
                        else:
                            action SetField(eval(eui_battle_voice_object),eui_battle_voice_field,False)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"

                    imagebutton:
                        xpos 690 ypos 225
                        idle "UI/options_audio_moavoice.png"
                        hover tr_hoverglow("UI/options_audio_moavoice.png")
                        selected_idle "UI/options_audio_moavoice_selected.png"
                        selected_hover tr_hoverglow("UI/options_audio_moavoice_selected.png")
                        if eui_battle_voice_object == None:
                            action SetVariable(eui_battle_voice_field,True)
                        else:
                            action SetField(eval(eui_battle_voice_object),eui_battle_voice_field,True)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"

                #dialogue voicing
                #imagebutton:
                #    xpos 690 ypos 340
                #    idle "UI/checkbox.png"
                #    hover tr_hoverglow("UI/checkbox.png")
                #    selected_idle "UI/checkbox_select.png"
                #    selected_hover tr_hoverglow("UI/checkbox_select.png")
                #    action ToggleField(config, 'auto_voice',true_value='sound/Voice/{id}.ogg', false_value=False)
                #    hover_sound "sound/hover1.ogg"
                #    activate_sound "sound/button1.ogg"

            if eui.option_show == 3:

                add "UI/eui_options_gameplay_text.png"

                default tt = Tooltip("")

                imagebutton:
                    xpos 90 ypos 170
                    idle "UI/options_gameplay_waifu.png"
                    hover tr_hoverglow("UI/options_gameplay_waifu.png")
                    selected_idle "UI/options_gameplay_waifu_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_waifu_select.png")
                    hovered tt.Action("Reduces the difficulty to near nill\nfor a stress free experience."),SetField(eui,"tty",170)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 0)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 220
                    idle "UI/options_gameplay_casual.png"
                    hover tr_hoverglow("UI/options_gameplay_casual.png")
                    selected_idle "UI/options_gameplay_casual_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_casual_select.png")
                    hovered tt.Action("Easy for newcomers and people not\ninterested in strategy."),SetField(eui,"tty",220)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 1)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 270
                    idle "UI/options_gameplay_ensign.png"
                    hover tr_hoverglow("UI/options_gameplay_ensign.png")
                    selected_idle "UI/options_gameplay_ensign_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_ensign_select.png")
                    hovered tt.Action("Average difficulty for people who want\na reasonable challenge."),SetField(eui,"tty",270)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 2)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 320
                    idle "UI/options_gameplay_captain.png"
                    hover tr_hoverglow("UI/options_gameplay_captain.png")
                    selected_idle "UI/options_gameplay_captain_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_captain_select.png")
                    action SetVariable("Difficulty", 3)
                    hovered tt.Action("Challenging but fair. Your mistakes\nwill be punished without mercy."),SetField(eui,"tty",320)
                    unhovered SetField(eui,"tty",-5000)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 370
                    idle "UI/options_gameplay_admiral.png"
                    hover tr_hoverglow("UI/options_gameplay_admiral.png")
                    selected_idle "UI/options_gameplay_admiral_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_admiral_select.png")
                    hovered tt.Action("For people who are good at this game."),SetField(eui,"tty",370)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 4)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 420
                    idle "UI/options_gameplay_spacewhale.png"
                    hover tr_hoverglow("UI/options_gameplay_spacewhale.png")
                    selected_idle "UI/options_gameplay_spacewhale_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_spacewhale_select.png")
                    hovered tt.Action("Why would you do this to yourself..."),SetField(eui,"tty",420)
                    unhovered SetField(eui,"tty",-5000)
                    action SetVariable("Difficulty", 5)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 600 ypos 168
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM,"show_tooltips",true_value=True, false_value=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 600 ypos 274
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM,"edgescroll",true_value=(100,800), false_value=(0,0))
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                #text "{k=0.5}SHOW BATTLE LOG{/k}":
                #    xpos 590 ypos 340
                #    font "Fonts/mplus-2p-regular.ttf"
                #    size 20
                #    color "#F7F7F7"


                imagebutton:
                    xpos 600 ypos 380
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM,"show_battle_log",true_value=True, false_value=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                frame:

                    xpos 360
                    ypos eui.tty
                    background "#000000"

                    text tt.value:
                        font "Fonts/ShareTech-Regular.ttf"
                        size 20
                        color "#F7F7F7"

    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0
init +2:
    ##############################################################################
    # History
    #
    # A screen that displays choices to make before beginning Mask of Arcadius
    # route.
    screen history:
        #TODO: Hotkey (or button) to randomize choices, I hate filling these out every single time
        zorder 500
        
        #if not renpy.showing("bg cera") is True:
        #    $ renpy.scene()
        #    # Fade in so that we don't see this for a split second before the splash screen
        #    $ renpy.show("bg cera")#, [tr_fadein_2(1.0)])

        add "Space/cera.jpg" at tr_fadein_2(0.2)
        
        add "UI/input_back.png" at tr_fadein_2(1):
            xpos 375 ypos 107
            
        default htt = Tooltip("")
        
        imagebutton at tr_fadein_2(1):
            xpos 1300 ypos 125
            idle "UI/back.png"
            hover tr_hoverglow("UI/back.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/button1.ogg"
            #action Show("main_menu"),Hide("history")
            action Hide("history")
        
        # No Import Feature for First Arrival pre MoA.
        #imagebutton at tr_fadein(1):
        #    xpos 1110 ypos 125
        #    idle "UI/import.png"
        #    hover tr_hoverglow("UI/import.png")
        #    hover_sound "sound/hover1.ogg"
        #    activate_sound "sound/button1.ogg"
        #    action SetVariable("customstat",False),Start()

        frame at tr_fadein_2(1):
            area (425, 207, 2000, 740)
            background None
            #viewport:# id "eui_history_box":
            #    draggable False
            #    mousewheel True
            #    child_size (1800,25+(eui.optpoint*41))
            frame at tr_fadein_2(1):
                background None

                for item in eui.setoptions:
                    if item[0] == 1: # Is an option title
                        if eui.his_eval(item[3]):
                            imagebutton at tr_fadein_2(0.2):
                                xpos eui.optionsxpos[eui.setoptions.index(item)] ypos eui.optionsypos[eui.setoptions.index(item)]
                                idle "UI/input_plotback.png"
                                hover "UI/input_plotback.png"
                                action NullAction()
                                
                                hovered htt.Action(item[2]), SetField(eui,"httx",eui.optionsxpos[eui.setoptions.index(item)]), SetField(eui,"htty",eui.optionsypos[eui.setoptions.index(item)])
                                
                                unhovered SetField(eui,"htty",-5000)
                                # Why was this here? This isn't really supposed to be a button
                                #activate_sound "sound/button1.ogg"

                            text item[1]:
                                xpos 10+25 ypos eui.optionsypos[eui.setoptions.index(item)]+10
                                font "Fonts/ShareTech-Regular.ttf"
                                size 20
                                color "#F7F7F7"

                    if item[0] == 2: # Is a pick able option
                        if eui.his_eval(item[3]):
                            imagebutton:
                                xpos eui.optionsxpos[eui.setoptions.index(item)] ypos eui.optionsypos[eui.setoptions.index(item)]
                                idle "UI/input_decision.png"
                                hover "UI/input_decision.png"
                                selected_idle "UI/input_decision_select.png"
                                selected_hover "UI/input_decision_select.png"
                                
                                hovered htt.Action(item[2]), SetField(eui,"httx",eui.optionsxpos[eui.setoptions.index(item)]), SetField(eui,"htty",eui.optionsypos[eui.setoptions.index(item)])
                                
                                unhovered SetField(eui,"htty",-5000)
                                action SetField(eui,item[4][0],item[4][1])
                                activate_sound "sound/button1.ogg" 

                            text item[1]:
                                xpos eui.optionsxpos[eui.setoptions.index(item)]+25 ypos eui.optionsypos[eui.setoptions.index(item)]+10
                                font "Fonts/ShareTech-Regular.ttf"
                                size 20
                                color "#000000"
                            
                            if htt.value != "":
                                frame: # Frame matches required size, MAGIC!
                                    xpos eui.httx+200 ypos eui.htty+20
                                    background "#000000"
                                    text htt.value:
                                        font "Fonts/ShareTech-Regular.ttf"
                                        size 20
                                        color "#F7F7F7"
                                    
                    #vbar value YScrollValue("eui_history_box") xpos 1070

        # Fix confirm button fading in too fast if already visible when showing this screen
        fixed at  tr_fadein_2(1):
            if eui.show_confirm():
                imagebutton at tr_fadein_2(0.2):
                    xpos 805 ypos 125
                    idle "UI/confirm.png"
                    hover tr_hoverglow("UI/confirm.png")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/ButtonClick.ogg"
                    action Hide("history"),Start("eui_skiptomaskofarcadius")
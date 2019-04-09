init +2:
    ##############################################################################
    # Say
    #
    # Screen that's used to display adv-mode dialogue.
    # http://www.renpy.org/doc/html/screen_special.html#say

    # init python:
        # store.say_text_size = 50

    screen say(who, what, side_image=None, two_window=False):

        default side_image = None
        default two_window = False
        zorder 100

        add "UI/messagebox.png":
            yanchor 1.0 ypos 1.0

        # Decide if we want to use the one-window or two-window varaint.
        if not two_window:

            window:
                id "window"
                
                has frame:
                    background None
                    ysize 380
                    ypos -220

                    if who:
                        
                        if who != " ":
                            add "UI/nametag.png" xpos -155 ypos -90

                            text who:
                                id "who"
                                size 70
                                xpos -50
                                ypos -146
                                font "Fonts/ShareTech-Regular.ttf"
                                outlines [ (3, "#0a0a0a", 0, 0) ] 

                    if len(what) > 300:
                        $say_text_size = 45
                    else:
                        $say_text_size = 50
                        
                    #if dlc == False:
                    
                    text what:
                        id "what"
                        size say_text_size
                        xpos 0
                        ypos -60
                        xmaximum 1640
                        font "Fonts/ShareTech-Regular.ttf"
                        outlines [(4, "#000000", 2, 2),(1, "#272727", 0, 0) ] 
                    
                    #if dlc == True:
                    
                    #    text what:
                    #        id "what"
                    #        size say_text_size
                    #        xpos 0
                    #        ypos -60
                    #        xmaximum 1640
                    #        font "Fonts/ShareTech-Regular.ttf"
                    #        outlines [(2, "#000000", 2, 2),(1, "#272727", 0, 0) ] 

        # Use the quick menu.
        #use quick_menu

    ##############################################################################
    # Choice
    #
    # Screen that's used to display in-game menus.
    # http://www.renpy.org/doc/html/screen_special.html#choice

    screen choice(items):

        #modal True
        #zorder 100
        #$pointBase = 0.35
        #if len(menu_choices) >= 4: # shift all up by .15, to keep it evenish
        #    $pointBase = 0.2
        #if len(menu_choices) >= 6:
        #    $pointBase = 0.05
        #for item in menu_choices:
        #    imagebutton at tr_decision(0.2*menu_choices.index(item)):
        #        xanchor 0.5
        #        ypos pointBase+(0.15*menu_choices.index(item))# (+0.15 ypos per item)
        #        idle "UI/choice_base.png"
        #        hover tr_hoverglow("UI/choice_base.png")
        #        
        #        activate_sound "sound/button1.ogg"
        #        action (Hide("decision"),Jump(item[1]))
        #        
        #    text item[0] at tr_decision(0.2*menu_choices.index(item)):
        #        text_align 0.5 xanchor 0.5 ypos pointBase+0.04 +(0.15*menu_choices.index(item))
        #        size 40
        #        outlines [ (4, "#282828", 0, 0) ]  

        modal True
        zorder 100
        $pointBase = 0.35
        if len(items) >= 4: # shift all up by .15, to keep it evenish
            $pointBase = 0.2
        if len(items) >= 6:
            $pointBase = 0.05
        for item in items:
            if item[1]:
                imagebutton at tr_decision(0.2*items.index(item)):
                    xanchor 0.5
                    ypos pointBase+(0.15*items.index(item))# (+0.15 ypos per item)
                    idle "UI/choice_base.png"
                    hover tr_hoverglow("UI/choice_base.png")
                    
                    activate_sound "sound/button1.ogg"
                    action item[1]
            else:
                imagebutton at tr_decision(0.2*items.index(item)):
                    xanchor 0.5
                    ypos pointBase+(0.15*items.index(item))# (+0.15 ypos per item)
                    idle "UI/choice_base.png"
                    hover tr_hoverglow("UI/choice_base.png")
                    
                    activate_sound "sound/button1.ogg"
                
            text item[0] at tr_decision(0.2*items.index(item)):
                text_align 0.5 xanchor 0.5 ypos pointBase+0.04 +(0.15*items.index(item))
                font "Fonts/ShareTech-Regular.ttf"
                #TODO: WE NEED WRAPPING!
                if len(item[0]) >= 200:
                    size 25
                    outlines [ (2, "#282828", 0, 0) ]
                elif len(item[0]) >= 100:
                    size 32
                    outlines [ (3, "#282828", 0, 0) ]
                else:
                    size 40
                    outlines [ (4, "#282828", 0, 0) ]  
        #use quick_menu

    ##############################################################################
    # Input
    #
    # Screen that's used to display renpy.input()
    # http://www.renpy.org/doc/html/screen_special.html#input

    screen input(prompt):

        window style "input_window":
            has vbox

            text prompt style "input_prompt"
            input id "input" style "input_text"

        #use quick_menu

    ##############################################################################
    # Nvl
    #
    # Screen used for nvl-mode dialogue and menus.
    # http://www.renpy.org/doc/html/screen_special.html#nvl

    screen nvl(dialogue, items=None):

        window:
            style "nvl_window"

            has vbox:
                style "nvl_vbox"

            # Display dialogue.
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id

                    has hbox:
                        spacing 10

                    if who is not None:
                        text who id who_id

                    text what id what_id

            # Display a menu, if given.
            if items:

                vbox:
                    id "menu"

                    for caption, action, chosen in items:

                        if action:

                            button:
                                style "nvl_menu_choice_button"
                                action action

                                text caption style "nvl_menu_choice"

                        else:

                            text caption style "nvl_dialogue"

        add SideImage() xalign 0.0 yalign 1.0

        #use quick_menu

    ##############################################################################
    # Yes/No Prompt
    #
    # Screen that asks the user a yes or no question.
    # http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

    screen yesno_prompt(message, yes_action, no_action):

        zorder 10000
        modal True
        fixed at tr_fadein(0):
            add "UI/yesno_base.png"
                        
            imagebutton:
                xpos 0.4 ypos 0.58 xanchor 0.5 yanchor 0.5
                idle "UI/yesno_yes.png"
                hover tr_hoverglow("UI/yesno_yes.png")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                action yes_action
                
            imagebutton:
                xpos 0.6 ypos 0.58 xanchor 0.5 yanchor 0.5
                idle "UI/yesno_no.png"
                hover tr_hoverglow("UI/yesno_no.png")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                action no_action

            frame:
                background None
                text message font "Fonts/SourceCodePro-Regular.ttf" size 20 color "#F7F7F7"
                xalign 0.5
                yalign 0.45
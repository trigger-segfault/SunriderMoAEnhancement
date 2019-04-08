init +2:
    ##############################################################################
    # Save, Load
    #
    # Screens that allow the user to save and load the game.
    # http://www.renpy.org/doc/html/screen_special.html#save
    # http://www.renpy.org/doc/html/screen_special.html#load

    # Since saving and loading are so similar, we combine them into
    # a single screen, file_picker. We then use the file_picker screen
    # from simple load and save screens.
    screen save():

        zorder 1200
        modal True
        
        drag:

            drag_name "drag_save"
            drag_handle (0,0,450,44)
            xpos 360 ypos 200
            drag_offscreen False

            fixed at tr_fadein(0):
                xmaximum 1196 ymaximum 630

                add "UI/save_base.png"

                imagebutton:
                    xpos 565 ypos 50
                    idle "UI/load_default.png"
                    hover tr_hoverglow("UI/load_default.png")          
                    selected_idle "UI/eui_load_default_select.png"
                    selected_hover tr_hoverglow("UI/eui_load_default_select.png")     
                    action [FilePage(persistent.eui_file_page), SelectedIf(eui.is_file_page())]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None
                    
                imagebutton:
                    xpos 754 ypos 50
                    idle "UI/load_auto.png"
                    hover tr_hoverglow("UI/load_auto.png")           
                    selected_idle "UI/eui_load_auto_select.png"
                    selected_hover tr_hoverglow("UI/eui_load_auto_select.png")   
                    action [FilePage("auto"), SelectedIf(eui.file_page_name() == "auto")]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None
                    
                imagebutton:
                    xpos 943 ypos 50
                    idle "UI/load_quick.png"
                    hover tr_hoverglow("UI/load_quick.png")            
                    selected_idle "UI/eui_load_quick_select.png"
                    selected_hover tr_hoverglow("UI/eui_load_quick_select.png")  
                    action [FilePage("quick"), SelectedIf(eui.file_page_name() == "quick")]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None

                imagebutton:
                    xpos 1133 ypos 50
                    idle "UI/load_cancel.png"
                    hover tr_hoverglow("UI/load_cancel.png")                
                    action (Hide("save"))#,SetVariable("show_load",False))
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None

                if eui.is_file_page():
                    imagebutton:
                        xpos 1118 ypos 98
                        if FilePageName() != "1":
                            idle "UI/eui_pageup.png"
                            hover tr_hoverglow("UI/eui_pageup.png")  
                            hover_sound "sound/hover1.ogg"
                            activate_sound "sound/button1.ogg" 
                            action (FilePagePrevious(), SetField(persistent, 'eui_file_page', eui.file_page_number() - 1), renpy.save_persistent())
                        else:
                            idle "UI/eui_pageup_limit.png"
                            hover tr_hoverglow("UI/eui_pageup_limit.png")        
                        focus_mask None

                    imagebutton:
                        xpos 1118 ypos 401
                        idle "UI/eui_pagedown.png"
                        hover tr_hoverglow("UI/eui_pagedown.png")            
                        action (FilePageNext(), SetField(persistent, 'eui_file_page', eui.file_page_number() + 1), renpy.save_persistent())
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                        focus_mask None

                style "file_picker_frame"

                $ columns = 4
                $ rows = 3#50
                hbox:
                    area (26, 92, 1148, 517)
                    viewport:
                        #draggable True
                        #mousewheel True
                        #scrollbars "vertical"
                        child_size (1100,517)
                        #child_size (1100,5000)
                                    
                        grid columns rows:
                            transpose False
                            xfill True
                            style_group "file_picker"
                            xpos 40
                            ypos 190

                            for i in eui.file_range():
                                
                                frame:
                                    xmaximum 265
                                    ymaximum 165
                                    background None
                                
                                    add FileScreenshot(eui.file_slot(i), page=eui.file_page(i)) size(266,150) ypos 1 xpos -7
                                    add "UI/eui_load_nameplate.png"
                                    button:
                                        background None
                                        focus_mask None
                                        
                                        #has vbox

                                        if FilePageName() == 'None':
                                            $ description = ""
                                        else:
                                            $ description = "% 2s. %s\n%s" % (
                                                FileSlotName(eui.file_name_slot(i), eui.EUI_FILE_COUNT),
                                                FileTime(eui.file_slot(i), page=eui.file_page(i), empty=_("Empty Slot.")),
                                                FileSaveName(eui.file_slot(i), page=eui.file_page(i)))
                                        
                                        #add FileScreenshot(eui.file_slot(i), page=eui.file_page(i)) size(227,127) ypos -15
                                        text description ysize 10 color "F7F7F7" font "Fonts/SourceCodePro-Regular.ttf" size 13
                                        #text description ysize 10 color "000000" font "Fonts/SourceCodePro-Regular.ttf" size 13


                                    imagebutton:
                                        idle "UI/saveload_slot_base.png"
                                        hover "UI/saveload_slot_hover.png"
                                        hover_sound "sound/hover1.ogg"
                                        activate_sound "sound/button1.ogg"
                                        focus_mask None
                                        action FileAction(eui.file_slot(i), page=eui.file_page(i))
                                
                                    imagebutton:
                                        idle "UI/savedelete_base.png"
                                        hover "UI/savedelete_hover.png"
                                        insensitive "UI/savedelete_inactive.png"
                                        activate_sound "sound/cancel.ogg"
                                        xpos 184
                                        action FileDelete(eui.file_slot(i), page=eui.file_page(i))      
    screen load:

        zorder 1200
        modal True
        
        drag:
            
            drag_name "drag_load"
            drag_raise True
            drag_handle (0,0,450,44)
            xpos 360 ypos 200
            drag_offscreen False
            
            fixed at tr_fadein(0):
                xmaximum 1196 ymaximum 630

                add "UI/load_base.png"

                imagebutton:
                    xpos 565 ypos 50
                    idle "UI/load_default.png"
                    hover tr_hoverglow("UI/load_default.png")          
                    selected_idle "UI/eui_load_default_select.png"
                    selected_hover tr_hoverglow("UI/eui_load_default_select.png")     
                    action [FilePage(persistent.eui_file_page), SelectedIf(eui.is_file_page())]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None
                    
                imagebutton:
                    xpos 754 ypos 50
                    idle "UI/load_auto.png"
                    hover tr_hoverglow("UI/load_auto.png")           
                    selected_idle "UI/eui_load_auto_select.png"
                    selected_hover tr_hoverglow("UI/eui_load_auto_select.png")   
                    action [FilePage("auto"), SelectedIf(eui.file_page_name() == "auto")]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None
                    
                imagebutton:
                    xpos 943 ypos 50
                    idle "UI/load_quick.png"
                    hover tr_hoverglow("UI/load_quick.png")            
                    selected_idle "UI/eui_load_quick_select.png"
                    selected_hover tr_hoverglow("UI/eui_load_quick_select.png")  
                    action [FilePage("quick"), SelectedIf(eui.file_page_name() == "quick")]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None

                imagebutton:
                    xpos 1133 ypos 50
                    idle "UI/load_cancel.png"
                    hover tr_hoverglow("UI/load_cancel.png")                
                    action (Hide("load"))#,SetVariable("show_load",False))
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    focus_mask None

                if eui.is_file_page():
                    imagebutton:
                        xpos 1118 ypos 98
                        if FilePageName() != "1":
                            idle "UI/eui_pageup.png"
                            hover tr_hoverglow("UI/eui_pageup.png")  
                            hover_sound "sound/hover1.ogg"
                            activate_sound "sound/button1.ogg" 
                            action (FilePagePrevious(), SetField(persistent, 'eui_file_page', eui.file_page_number() - 1), renpy.save_persistent())
                        else:
                            idle "UI/eui_pageup_limit.png"
                            hover tr_hoverglow("UI/eui_pageup_limit.png")        
                        focus_mask None

                    imagebutton:
                        xpos 1118 ypos 401
                        idle "UI/eui_pagedown.png"
                        hover tr_hoverglow("UI/eui_pagedown.png")            
                        action (FilePageNext(), SetField(persistent, 'eui_file_page', eui.file_page_number() + 1), renpy.save_persistent())
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                        focus_mask None

                style "file_picker_frame"

                $ columns = 4
                $ rows = 3#50
                hbox:
                    area (26, 92, 1148, 517)
                    viewport:
                        #draggable True
                        #mousewheel True
                        #scrollbars "vertical"
                        child_size (1100,517)
                        #child_size (1100,5000)
                                    
                        grid columns rows:
                            transpose False
                            xfill True
                            style_group "file_picker"
                            xpos 40
                            ypos 190

                            for i in eui.file_range():
                                
                                frame:
                                    xmaximum 265
                                    ymaximum 165
                                    background None
                                
                                    add FileScreenshot(eui.file_slot(i), page=eui.file_page(i)) size(266,150) ypos 1 xpos -7
                                    add "UI/eui_load_nameplate.png"

                                    button:
                                        background None
                                        focus_mask None
                                        
                                        #has vbox

                                        if FilePageName() == 'None':
                                            $ description = ""
                                        else:
                                            $ description = "% 2s. %s\n%s" % (
                                                FileSlotName(eui.file_name_slot(i), eui.EUI_FILE_COUNT),
                                                FileTime(eui.file_slot(i), page=eui.file_page(i), empty=_("Empty Slot.")),
                                                FileSaveName(eui.file_slot(i), page=eui.file_page(i)))
                                        
                                        #add FileScreenshot(eui.file_slot(i), page=eui.file_page(i)) size(227,127) ypos -15
                                        text description ysize 10 color "F7F7F7" font "Fonts/SourceCodePro-Regular.ttf" size 13
                                        #text description ysize 10 color "000000" font "Fonts/SourceCodePro-Regular.ttf" size 13


                                    imagebutton:
                                        idle "UI/saveload_slot_base.png"
                                        hover "UI/saveload_slot_hover.png"
                                        hover_sound "sound/hover1.ogg"
                                        activate_sound "sound/button1.ogg"
                                        focus_mask None
                                        action FileAction(eui.file_slot(i), page=eui.file_page(i))
                                
                                    imagebutton:
                                        idle "UI/savedelete_base.png"
                                        hover "UI/savedelete_hover.png"
                                        insensitive "UI/savedelete_inactive.png"
                                        activate_sound "sound/cancel.ogg"
                                        xpos 184
                                        action FileDelete(eui.file_slot(i), page=eui.file_page(i))

    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text
init +2:
    screen gallery_back:
        
        zorder 1200
        modal True

        add "UI/bonus_back.png":
            xalign 0.5 yalign 0.5
        #imagebutton:
        #    xpos 1542 ypos 50
        #    idle "UI/load_cancel.png"
        #    hover tr_hoverglow("UI/load_cancel.png")                
        #    action (Hide("gallery_back"),Hide("page"))#,SetVariable("show_load",False))
        #    hover_sound "sound/hover1.ogg"
        #    activate_sound "sound/button1.ogg"
        #    focus_mask None
        vbox:
            spacing 10
            xpos 1260 ypos 185
            #xpos 1260 ypos 250
            xsize 470
            ysize 863
            #ysize 740
            
            
            if renpy.seen_label("aftercredits7") == True:
                        
                imagebutton:
                    if eui.show_bonus != 1:
                        idle "UI/bonus_charactercg_base.png"
                        hover "UI/bonus_charactercg_hover.png"
                    else:
                        idle "UI/bonus_charactercg_selected.png"
                        hover "UI/bonus_charactercg_selected_hover.png"
                    action If(eui.show_bonus == 1, true=(Hide("gallery_charactercg")), false=(Show("gallery_charactercg"))),ToggleField(eui,"show_bonus",true_value=1,false_value=0)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"

                imagebutton:
                    if eui.show_bonus != 2:
                        idle "UI/bonus_mechacg_base.png"
                        hover "UI/bonus_mechacg_hover.png"
                    else:
                        idle "UI/bonus_mechacg_selected.png"
                        hover "UI/bonus_mechacg_selected_hover.png"
                    action If(eui.show_bonus == 2, true=(Hide("gallery_mechacg")), false=(Show("gallery_mechacg"))),ToggleField(eui,"show_bonus",true_value=2,false_value=0)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"

                imagebutton:
                    if eui.show_bonus != 3:
                        idle "UI/bonus_backgrounds_base.png"
                        hover "UI/bonus_backgrounds_hover.png"
                    else:
                        idle "UI/bonus_backgrounds_selected.png"
                        hover "UI/bonus_backgrounds_selected_hover.png"
                    action If(eui.show_bonus == 3, true=(Hide("gallery_backgrounds")), false=(Show("gallery_backgrounds"))),ToggleField(eui,"show_bonus",true_value=3,false_value=0)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"

                imagebutton:
                    if eui.show_bonus != 4:
                        idle "UI/bonus_music_base.png"
                        hover "UI/bonus_music_hover.png"
                    else:
                        idle "UI/bonus_music_selected.png"
                        hover "UI/bonus_music_selected_hover.png"
                    action If(eui.show_bonus == 4, true=(Hide("gallery_music")), false=(Show("gallery_music"))),ToggleField(eui,"show_bonus",true_value=4,false_value=0)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                        
                        
            if renpy.seen_label("aftercredits7") == False:
                
                add "UI/bonus_charactercg_locked.png"
                add "UI/bonus_mechacg_locked.png"
                add "UI/bonus_backgrounds_locked.png"
                add "UI/bonus_music_locked.png"

            

            imagebutton:
                if eui.show_bonus != 5:
                    idle "UI/eui_bonus_deleted_scenes_base.png"
                    hover "UI/eui_bonus_deleted_scenes_hover.png"
                else:
                    idle "UI/eui_bonus_deleted_scenes_selected.png"
                    hover "UI/eui_bonus_deleted_scenes_selected_hover.png"
                action If(eui.show_bonus == 5, true=(Hide("gallery_deleted_scenes")), false=(Show("gallery_deleted_scenes"))),ToggleField(eui,"show_bonus",true_value=5,false_value=0)
                hover_sound "Sound/hover1.ogg"
                activate_sound "Sound/button1.ogg"

            imagebutton:
                if eui.show_bonus != 6:
                    idle "UI/eui_bonus_mod_scenes_base.png"
                    hover "UI/eui_bonus_mod_scenes_hover.png"
                else:
                    idle "UI/eui_bonus_mod_scenes_selected.png"
                    hover "UI/eui_bonus_mod_scenes_selected_hover.png"
                action If(eui.show_bonus == 6, true=(Hide("gallery_mod_scenes")), false=(Show("gallery_mod_scenes"))),ToggleField(eui,"show_bonus",true_value=6,false_value=0)
                hover_sound "Sound/hover1.ogg"
                activate_sound "Sound/button1.ogg"
                    
            imagebutton:
                idle "UI/bonus_back_base.png"
                hover "UI/bonus_back_hover.png"
            
                action Hide("gallery_back"),Hide("page"),SetField(eui,"show_bonus",0)
                hover_sound "Sound/hover1.ogg"
                activate_sound "Sound/button1.ogg"

            #if eui.show_chivos == False:
                
            #    imagebutton:
            #        idle "UI/bonus_achievements_base.png"
            #        hover "UI/bonus_achievements_hover.png"
            #        action If(eui.show_chivos, true=(Hide("gallery_achievements")), false=(Show("gallery_achievements"))),ToggleVariable("eui.show_chivos",true_value=True, false_value=False),SetVariable("eui.show_charactercg",False),SetVariable("eui.show_mechacg",False),SetVariable("eui.show_music",False),SetVariable("eui.show_backgrounds",False)
            #        hover_sound "Sound/hover1.ogg"
            #        activate_sound "Sound/button1.ogg"
                    
            #if eui.show_chivos == True:
                
            #    imagebutton:
            #        idle "UI/bonus_achievements_selected.png"
            #        hover "UI/bonus_achievements_selected_hover.png"
            #        action If(eui.show_chivos, true=(Hide("gallery_achievements")), false=(Show("gallery_achievements"))),ToggleVariable("eui.show_chivos",true_value=True, false_value=False)
            #        hover_sound "Sound/hover1.ogg"
            #        activate_sound "Sound/button1.ogg"

            #imagebutton:
            #    idle "UI/eui_bonus_addon_scenes_base.png"
            #    hover "UI/bonus_back_hover.png"
            
            #    action Hide("gallery_back"),Hide("gallery_achievements"),Hide("page"),SetVariable("eui.show_charactercg",False),SetVariable("eui.show_chivos",False),SetVariable("eui.show_mechacg",False),SetVariable("eui.show_backgrounds",False),SetVariable("eui.show_music",False)
            #    hover_sound "Sound/hover1.ogg"
            #    activate_sound "Sound/button1.ogg"

            #imagebutton:
            #    idle "UI/bonus_back_base.png"
            #    hover "UI/bonus_back_hover.png"
            #
            #    action Hide("gallery_back"),Hide("gallery_achievements"),Hide("page"),SetVariable("eui.show_charactercg",False),SetVariable("eui.show_chivos",False),SetVariable("eui.show_mechacg",False),SetVariable("eui.show_backgrounds",False),SetVariable("eui.show_music",False)
            #    hover_sound "Sound/hover1.ogg"
            #    activate_sound "Sound/button1.ogg"

    screen gallery_music:
        
        tag page
        
        zorder 1300
        
        frame:
            area (245,265,980,700)
            background None
            
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                child_size (920,1015)
                
                grid 3 6:
                    
                    xfill True
                    yfill True

                    for i in range(0,3*6):
                        text ""
                    
                grid 3 6:
                    
                    xfill True
                    yfill True

                    for i in range(0,3*6):
                        text ""
                            

    screen gallery_charactercg:
        
        tag page
        
        zorder 1300
        
        frame:
            area (245,265,980,700)
            background None
            
            if CENSOR == True:
            
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    child_size (920,2369)
                        
                    grid 3 14:
                        
                        xfill True
                        yfill True

                        # Call make_button to show a particular button.

                        for i in range(0,3*14):
                            text ""

            if CENSOR == False:
                
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    child_size (920,2538)
                                
                    grid 3 15:
                        
                        xfill True
                        yfill True

                        for i in range(0,3*15):
                            text ""
                        


    screen gallery_mechacg:
        
        tag page
        
        zorder 1300
        
        frame:
            area (245,265,980,700)
            background None
            
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                child_size (920,2370)
        
                grid 3 14:

                    xfill True
                    yfill True

                    for i in range(0,3*14):
                        text ""


    screen gallery_backgrounds:
        
        tag page
        
        zorder 1300
        
        frame:
            area (245,265,980,700)
            background None
            
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                child_size (920,2370)
        
                grid 3 14:

                    xfill True
                    yfill True

                    for i in range(0,3*14):
                        text ""


    screen gallery_deleted_scenes:
        
        tag page
        
        zorder 1300
        
        frame:
            area (245,265,980,700)
            background None
            
            $ eui_scene_rows = int((len(scenes) + 2) / 3)

            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                child_size (920,eui_scene_rows*169+1)
            
                grid 3 max(eui_scene_rows,1):
                    
                    xfill True
                    yfill True
                
                    if hasattr(store,"BM"):
                        $BM.phase = 'Player' # This is done to make sure that we can open the menu while in a bonus
                    
                    for i in range(1, len(scenes) + 1):
                        $ is_label = renpy.has_label(scenes[i - 1].jumpLoc)
                        $ eui_scene = scenes[i-1]

                        frame:
                            style "default"

                            #imagebutton:
                            #    idle "UI/bonus_song_base.png"
                            #    hover "UI/bonus_song_hover.png"
                            #    insensitive "CG/thumbs/locked.jpg"
                            #    selected_idle "UI/bonus_song_baseplay.png"
                            #    selected_hover "UI/bonus_song_hoverplay.png"
                            #    action mr.Play("Music/Anguish.ogg")
                            #    hover_sound "Sound/hover1.ogg"
                            #    activate_sound "Sound/button1.ogg"

                            imagebutton:
                                idle (scenes[i - 1].image)
                                hover tr_hoverglow(scenes[i - 1].image)
                                at zoom_button(scenes[i - 1].zoom)
                                #at zoom (scenes[i - 1].zoom)
                                action If(is_label, true = [Hide('gallery_back'),SetField(eui,"show_bonus",0),Start(scenes[i - 1].jumpLoc)], false = [Hide('gallery_back'),SetField(eui,"show_bonus",0),ShowMenu(scenes[i - 1].jumpLoc)])
                                hover_sound "Sound/hover1.ogg"
                                activate_sound "Sound/button1.ogg"

                            text scenes[i - 1].text ysize 10 color "#F7F7F7" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100

                        $ del is_label
                        $ del eui_scene
                    for i in range(len(scenes),max(eui_scene_rows,1)*3):
                        text ""
            $ del eui_scene_rows      

    screen gallery_mod_scenes:
        
        tag page
        
        zorder 1300
        
        frame:
            area (245,265,980,700)
            background None
            
            $ eui_addon_rows = int((len(addon_scenes) + 2) / 3)

            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                child_size (920,eui_addon_rows*169+1)
            
                grid 3 max(eui_addon_rows,1):
                    
                    xfill True
                    yfill True
                
                    if hasattr(store,"BM"):
                        $BM.phase = 'Player' # This is done to make sure that we can open the menu while in a bonus
                    
                    for i in range(1, len(addon_scenes) + 1):
                        $ is_label = renpy.has_label(addon_scenes[i - 1].jumpLoc)
                        $ eui_addon = addon_scenes[i-1]

                        frame:
                            style "default"

                            #imagebutton:
                            #    idle "UI/bonus_song_base.png"
                            #    hover "UI/bonus_song_hover.png"
                            #    insensitive "CG/thumbs/locked.jpg"
                            #    selected_idle "UI/bonus_song_baseplay.png"
                            #    selected_hover "UI/bonus_song_hoverplay.png"
                            #    action mr.Play("Music/Anguish.ogg")
                            #    hover_sound "Sound/hover1.ogg"
                            #    activate_sound "Sound/button1.ogg"

                            imagebutton:
                                idle (addon_scenes[i - 1].image)
                                hover tr_hoverglow(addon_scenes[i - 1].image)
                                at zoom_button(addon_scenes[i - 1].zoom)
                                action If(is_label, true = [Hide('gallery_back'),SetField(eui,"show_bonus",0),Start(addon_scenes[i - 1].jumpLoc)], false = [Hide('gallery_back'),SetField(eui,"show_bonus",0),ShowMenu(addon_scenes[i - 1].jumpLoc)])
                                hover_sound "Sound/hover1.ogg"
                                activate_sound "Sound/button1.ogg"

                            text addon_scenes[i - 1].text ysize 10 color "#F7F7F7" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100

                        $ del is_label
                        $ del eui_addon
                    for i in range(len(addon_scenes),max(eui_addon_rows,1)*3):
                        text ""
            $ del eui_addon_rows                   
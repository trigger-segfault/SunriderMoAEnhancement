init +1:
    screen load:

        modal True
        zorder 200

        key "mousedown_3" action Hide('load', transition=dissolve)
        key 'mousedown_4' action NullAction() #should fix a bug where you can rollback in battle when the menu is open.

        #if not hasattr(store,'BM'):
        #    $ BM = Battle()
        #    $ MasterBM = BM
        if (BM.phase == 'PACT' or BM.phase == 'Pirate'):
            text 'WARNING! \n You can not load during the enemy \n turn.':
                xalign 0.5
                yalign 0.5
                size 35
                color 'fff'
                outlines [(2,'f00',0,0)]

            timer 2 action Hide('load')
        else:

            imagemap:
                ground "Menu/load_base.png"
                hover "Menu/load_hover.png"

                hotspot (752, 215, 137, 28) action FilePage(1)
                hotspot (913, 215, 137, 28) action FilePage("auto")
                hotspot (1075, 215, 137, 28) action FilePage("quick")
                hotspot (1221, 250, 30, 146) action FilePagePrevious()
                hotspot (1221, 724, 30, 146) action FilePageNext()
                hotspot (948, 926, 107, 23) action Hide('load', transition=dissolve)
                hotspot (726, 59, 137, 44) action [ Hide('load'), Show('save', transition=dissolve) ]
                hotspot (1002, 59, 137, 44) action [ Hide('load'), Show('preferences', transition=dissolve) ]
                hotspot (1140, 59, 137, 44) action MainMenu()

                style "file_picker_frame"

                $ columns = 1
                $ rows = 8

                # Display a grid of file slots.
                grid columns rows:
                    transpose True
                    xfill True
                    style_group "file_picker"
                    xpos 753
                    ypos 251

                    # Display eight file slots, numbered 1 - 8.
                    for i in range(1, columns * rows + 1):

                        # Each file slot is an hbox containing two buttons.
                        hbox:

                            button:

                                xminimum 424
                                yminimum 77
                                action FileAction(i)

                                has hbox

                                # Add the screenshot.
                                add FileScreenshot(i) size(config.thumbnail_width,config.thumbnail_height)

                                # Format the description, and add it as text.
                                $ description = "% 2s. %s\n%s" % (
                                    FileSlotName(i, columns * rows),
                                    FileTime(i, empty=_("Empty Slot.")),
                                    FileSaveName(i))

                                text description

                                key "save_delete" action FileDelete(i)

                            button:

                                yminimum 77
                                action FileDelete(i)
                                text "X" # Or this could be an image or something.

    screen save:

        modal True
        zorder 200

        key "mousedown_3" action Hide('save', transition=dissolve)
        key 'mousedown_4' action NullAction() #should fix a bug where you can rollback in battle when the menu is open.

        #if not hasattr(store,"BM"):
        #    $ BM = Battle()
            #No need to update the MasterBM if there is no battle manager to begin with.  Besides, the MasterBM and the BM might not be the same
        if (BM.phase == 'PACT' or BM.phase == 'Pirate'):
            text 'WARNING! \n You can not save during the enemy \n turn.':
                xalign 0.5
                yalign 0.5
                size 35
                color 'fff'
                outlines [(2,'f00',0,0)]

            timer 2 action Hide('save')

        else:

            imagemap:
                ground "Menu/save_base.png"
                hover "Menu/save_hover.png"

                hotspot (752, 215, 137, 28) action FilePage(1)
                hotspot (913, 215, 137, 28) action FilePage("auto")
                hotspot (1075, 215, 137, 28) action FilePage("quick")
                hotspot (1221, 250, 30, 146) action FilePagePrevious()
                hotspot (1221, 724, 30, 146) action FilePageNext()
                hotspot (948, 926, 107, 23) action Hide('save', transition=dissolve)
                hotspot (864, 59, 137, 44) action [ Hide('save'), Show('load', transition=dissolve) ]
                hotspot (1002, 59, 137, 44) action [ Hide('save'), Show('preferences', transition=dissolve) ]
                hotspot (1140, 59, 137, 44) action MainMenu()

                style "file_picker_frame"

                $ columns = 1
                $ rows = 8

                # Display a grid of file slots.
                grid columns rows:
                    transpose True
                    xfill True
                    style_group "file_picker"
                    xpos 753
                    ypos 251

                    # Display eight file slots, numbered 1 - 8.
                    for i in range(1, columns * rows + 1):

                        # Each file slot is an hbox containing two buttons.
                        hbox:

                            button:

                                xminimum 424
                                yminimum 77
                                action FileAction(i)

                                has hbox

                                # Add the screenshot.
                                add FileScreenshot(i) size(config.thumbnail_width,config.thumbnail_height)

                                # Format the description, and add it as text.
                                $ description = "% 2s. %s\n%s" % (
                                    FileSlotName(i, columns * rows),
                                    FileTime(i, empty=_("Empty Slot.")),
                                    FileSaveName(i))

                                text description

                                key "save_delete" action FileDelete(i)

                            button:

                                yminimum 77
                                action FileDelete(i)
                                text "X" # Or this could be an image or something.
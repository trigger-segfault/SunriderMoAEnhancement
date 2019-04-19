init +2:
    # screen galaxymap_buttons: ###################################GALAXY MAP BUTTONS

    #     modal True

    #     for planet in planets:
    #         if planet.shouldShowOnMap():
    #             imagebutton:
    #                 action Jump(planet.jumpLocation)
    #                 idle "Map/map_icon_base.png"
    #                 hover "Map/map_icon_hover.png"
    #                 xpos planet.xPos ypos planet.yPos
    #             text planet.name xpos planet.xPos + 55 ypos planet.yPos size 15

    #     imagebutton:
    #         xpos 1600 ypos 950
    #         action Jump("galaxymapend")
    #         idle "Map/back_button_base.png"
    #         hover "Map/back_button_hover.png"

    screen galaxymap_buttons: ###################################GALAXY MAP BUTTONS
    # Now, picked planets are set to GM_selected so they can be traced by screen code
    # Planets have .missions attribute that can be used to set missions to appear.
    # A default setting will let planets gen their own mission select options

        modal True
        #tag galaxy_map

        key "mousedown_4" action NullAction()

        Planet("CERA", "warpto_OccupiedCera", 1297, 480, "warpto_occupiedcera")
        Planet("TYDARIA", "warpto_Tydaria", 1390, 540, "warpto_tydaria")
        Planet("ASTRAL EXPANSE", "warpto_astralexpanse", 1250, 540, "warpto_astralexpanse")
        Planet("PACT Outpost", "warpto_pactstation", 1420, 480, "warpto_pactstation1")
        Planet("VERSTA", "warpto_versta", 1490, 725, "warpto_versta")
        Planet("NOMODORN", "warpto_nomodorn", 1630, 590, "warpto_nomodorn")
        Planet("RYUVIA PRIME", "warpto_ryuvia", 1410, 740, "warpto_ryuvia")
        Planet("FAR PORT", "warpto_farport", 1260, 776, "warpto_farport")
        Planet("ONGESS", "warpto_ongess", 1345, 655, "warpto_ongess")

        for planet in planets:
            if planet.shouldShowOnMap():

                $ idle_image = "Map/map_icon_base.png"
                $ hover_image = "Map/map_icon_hover.png"
                $ planet_active = False

#region PLANET_ACTIVE CONDITIONS
                if planet.jumpLocation == "warpto_Tydaria":
                    if MetAsaga == False:
                        $ planet_active = True

                    if mission_pirateattack == True:
                        $ planet_active = True

                    if warpto_versta == True:
                        $ planet_active = False
                        
                    if tydaria_morepirates == True:
                        $ planet_active = True

                    if tydaria_escort == True:
                        $ planet_active = True

                elif planet.jumpLocation == "warpto_astralexpanse":
                    if mission_pirateattack == True:
                        if mission3_complete == False and mission4_complete == False:
                            $ planet_active = True

                elif planet.jumpLocation == "warpto_pactstation":
                    if mission_pirateattack == True:
                        if mission3_complete == False and mission4_complete == False:
                            $ planet_active = True

                elif planet.jumpLocation == "warpto_versta":
                    if amissionforalliance == True:
                        $ planet_active = True
                        
                    elif versta_ambush == True:
                        $ planet_active = True

                elif planet.jumpLocation == "warpto_nomodorn":
                    if missionforryuvia == True:
                        $ planet_active = True

                elif planet.jumpLocation == "warpto_farport":
                    if farport_losttech == True:
                        $ planet_active = True

                elif planet.jumpLocation == "warpto_ongess":
                    if greytour == True:
                        $ planet_active = True
#endregion

                if planet_active:
                    $ idle_image = "Map/map_icon_base_highlight.png"
                    $ hover_image = "Map/map_icon_hover_highlight.png"
                
                imagebutton:
                    action Jump(planet.jumpLocation)
                    idle idle_image
                    hover hover_image
                    xpos planet.xPos ypos planet.yPos
                text planet.name xpos planet.xPos + 55 ypos planet.yPos size 15

        imagebutton:
            xpos 1600 ypos 950
            action Jump("galaxymapend")
            idle "Map/back_button_base.png"
            hover "Map/back_button_hover.png"
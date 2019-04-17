init +2:
    # Draw Movement energy below targetting
    # Liberation Day Targetting window
    # Remove zoom scaling on numerous text elements like in Liberation Day
    screen battle_screen:
        font "Fonts/ShareTech-Regular.ttf"
        size 30
        tag tactical
        modal False
        zorder -5
        key "mousedown_4" action ZoomAction(["zoom", "in"])    #scroll in and out
        key "mousedown_5" action ZoomAction(["zoom", "out"])
        key "K_PAGEUP" action Return(["zoom", "in"])
        key "K_PAGEDOWN" action Return(["zoom", "out"])
        if 'mouseup_2' not in config.keymap['hide_windows']:
            key "mousedown_2" action Return(["next ship"])
        if 'mouseup_3' not in config.keymap['game_menu']:
            key "mousedown_3" action Return(["deselect"])
        key "]" action Return(["next ship"])
        if BM.phase == "battle":
            key "[" action Return(["previous ship"])

        ##messing with the player for fun and profit
        if BM.battlemode:
            timer 900 repeat False action Show('game_over_gimmick')

        add MouseTracker() #relates drags and clicks to the viewport and the BM

        if config.developer: #a release version should have set this to False
            key "Q" action Jump(['quit'])  ##DEBUG FAST QUIT##
            key "A" action Return(['anime'])
            if BM.phase != 'formation':
                key "P" action Return(['I WIN'])

        $childx = round(3840*zoomlevel) #this makes it so you can't scroll past the edge of the battlefield when zoomed out
        $childy = round(3006*zoomlevel+300) #extra 300 is so that the status window doesn't occlude ships in the far right bottom corner

        add BM.battle_bg xalign 0.5 yalign 0.5 #zoom 0.5 ##background for the battlefield##

        viewport id "grid":
            xmaximum 1920
            ymaximum 1080
            xadjustment BM.xadj
            yadjustment BM.yadj
            child_size (childx,childy)
            draggable False #BM.draggable
            mousewheel False
            edgescroll BM.edgescroll #(0,0) #(70,400*zoomlevel)

                    ##CREATE HEX GRID##

    ##laggy as fuck!!
            if BM.show_grid:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        $xposition = dispx(a, b, zoomlevel)
                        $yposition = dispy(a, b, zoomlevel)
                        $xsize = int((HEXW + 4) * zoomlevel)
                        $ysize = int((HEXH + 4) * zoomlevel)
                        add "Battle UI/hex.png":
                            xpos xposition
                            ypos yposition
                            size (xsize,ysize)
                            alpha 0.4
            else:
    ##much faster!
                $xsize = int((HEXW+5.5) * zoomlevel * 18)
                $ysize = int((HEXD+4) * zoomlevel * 16)
                add IC.hexgrid:
                    alpha 0.4
                    # zoom zoomlevel * 0.685
                    size (xsize,ysize)
                    xpos int(HEXW * zoomlevel)
                    ypos int((HEXD-2) * zoomlevel)

            if not BM.hovered == None: #when you hover over a ship
                if BM.hovered.shield_generation > 0:
                    for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.shield_range:
                                $ ship = BM.hovered
                                $ effective_shielding = ship.shield_generation + ship.modifiers['shield_generation'][0]
                                if effective_shielding > 0:
                                    $xposition = dispx(a,b,zoomlevel)
                                    $yposition = dispy(a,b,zoomlevel)
                                    $xsize = int((HEXW + 4) * zoomlevel)
                                    $ysize = int((HEXH + 4) * zoomlevel)
                                    add IC.blue_hex:
                                        xpos xposition
                                        ypos yposition
                                        size (xsize,ysize)
                                        alpha 0.7
                if BM.hovered.flak > 0:
                    for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.flak_range:
                                $ ship = BM.hovered
                                $effective_flak = ship.flak + ship.modifiers['flak'][0]
                                if effective_flak > 0:
                                    $xposition = dispx(a,b,zoomlevel)
                                    $yposition = dispy(a,b,zoomlevel)
                                    $xsize = int((HEXW + 4) * zoomlevel)
                                    $ysize = int((HEXH + 4) * zoomlevel)
                                    add IC.red_hex:
                                        xpos xposition
                                        ypos yposition
                                        size (xsize,ysize)
                                        alpha 0.9

            if not BM.weaponhover == None: #when you hover over a weapon button
                if BM.weaponhover.wtype == 'Missile' or BM.weaponhover.wtype == 'Rocket' or BM.weaponhover.name == 'Flak Off':
                    for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                                for ship in enemy_ships:
                                    if get_distance(ship.location,(a,b)) <= ship.flak_range:
                                        $effective_flak = ship.flak + ship.modifiers['flak'][0]
                                        if effective_flak > 0:
                                            $xposition = dispx(a,b,zoomlevel)
                                            $yposition = dispy(a,b,zoomlevel)
                                            $xsize = int((HEXW + 4) * zoomlevel)
                                            $ysize = int((HEXH + 4) * zoomlevel)
                                            add IC.red_hex:
                                                xpos xposition
                                                ypos yposition
                                                size (xsize,ysize)
                                                alpha 0.9
                if BM.weaponhover.wtype == 'Laser' or BM.weaponhover.wtype == 'Pulse' or BM.weaponhover.name == 'Shield Down' or BM.weaponhover.name == 'Shield Jam':
                    for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                                for ship in enemy_ships:
                                    if get_distance(ship.location,(a,b)) <= ship.shield_range:
                                        $effective_shielding = ship.shield_generation + ship.modifiers['shield_generation'][0]
                                        if effective_shielding > 0:
                                            $xposition = dispx(a,b,zoomlevel)
                                            $yposition = dispy(a,b,zoomlevel)
                                            $xsize = int((HEXW + 4) * zoomlevel)
                                            $ysize = int((HEXH + 4) * zoomlevel)
                                            add IC.blue_hex:
                                                xpos xposition
                                                ypos yposition
                                                size (xsize,ysize)
                                                alpha 0.7

                    ## DISPLAY COVER ##
            for cover in BM.covers:
                $xposition = dispx(cover.location[0],cover.location[1],zoomlevel, 0.5)
                $yposition = dispy(cover.location[0],cover.location[1],zoomlevel, 0.5)
                $xsize = int(210 * zoomlevel)
                $ysize = int(120 * zoomlevel)
                add cover.label:
                    xanchor 0.5
                    yanchor 0.5
                    xpos xposition
                    ypos yposition
                    size (xsize,ysize)
                    at Transform(cover.label,rotate = cover.angle)



                    ## DISPLAY SHIP AVATARS ##

            for ship in BM.ships: #cycle through every ship in the battle
                    ##first we show the circle base below every unit
                if ship.location != None:
                    $ x,y = ship.location
                    if x > 0 and y > 0:
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJY) + int(zoomlevel * MOVY)
                        $xsize = int(210 * zoomlevel)
                        $ysize = int(120 * zoomlevel)
                        if ship.faction == 'Player':
                            add IC.player_base:
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)
                        if ship.faction == 'PACT':
                            add IC.pact_base:
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)
                        if ship.faction == 'Pirate':
                            add IC.pirate_base:
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)

                        $cell_width = 1920 / ((GRID_SIZE[0]+2)/2)
                        $cell_height = 1503 / ((GRID_SIZE[1]+2)/2)
                        #$cell_offset = cell_width / 2

                        #calculate the position of the ships on the field
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel, 0.25 * ADJY) + int(zoomlevel * MOVY)

                        if ship.getting_buff:  #used if you buff someone
                            add 'Battle UI/buff_back.png':
                                xpos int(xposition-(cell_width/2)*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at buffup(yposition)

                        if ship.getting_curse:  #used if you curse someone
                            add 'Battle UI/curse_back.png':
                                xpos int(xposition-(cell_width/2)*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at cursedown(yposition-(190)*zoomlevel)

                        #default values.
                        $mode = '' #default
                        $lbl = ship.lbl
                        $hvr = hoverglow(ship.lbl)

                        ##depending on the circumstance of the particular ship in the loop the avatar should appear normally, should blink(target) or should appear dark(offline).

                        if ship.faction == 'Player':
                            #by default player ships can be selected, which the above values are already set to.

                            if BM.targetingmode:
                                #you cannot target yourself with an active weapon
                                $ mode = 'offline'

                                if BM.active_weapon != None:
                                    if BM.active_weapon.wtype == 'Support':
                                        #except when the active weapon is a support skill. in that case, player ships become targets
                                        $ mode = 'target'

                                if ship.cth <=0:
                                    #if the target cannot be affected it should be made obvious.
                                    $ mode = 'offline'

                        else: #ship is an enemy faction
                            #by default enemy ships can be selected (to view stat details), which the above values are already set to.

                            if BM.targetingmode and BM.active_weapon != None:
                                #with an active weapon selected enemies become targets
                                $ mode = 'target'

                                if BM.active_weapon.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(BM.selected,ship) != 1):
                                    #except when the active weapon is melee and this enemy is neither a ryder nor next to the attacking ship
                                    $ mode = 'offline'

                                if BM.active_weapon.wtype == 'Support':
                                    $ mode = 'offline'

                        if BM.active_weapon != None:
                            if BM.active_weapon.name == 'Gravity Gun':
                                #the gravity gun is a bit unique
                                if ship.stype != 'Ryder':
                                    $ mode = 'offline'
                                else:
                                    $ mode = 'target'

                        if mode == 'target':
                            $ lbl = hoverglow(ship.lbl)
                        elif mode == 'offline':
                            $ lbl = im.MatrixColor(ship.lbl,im.matrix.brightness(-0.3))

                        if BM.hovered != None:
                            if BM.hovered == ship:
                                if mode != 'offline':
                                    $ lbl = hoverglow(ship.lbl)

                        add lbl:
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            zoom (zoomlevel/2.5)

                        if ship.getting_buff:
                            add 'Battle UI/buff_front.png':
                                xpos int(xposition-96*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at buffup(int(yposition+50*zoomlevel))

                        if ship.getting_curse:
                            add 'Battle UI/curse_front.png':
                                xpos int(xposition-96*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at cursedown(yposition-(190-50)*zoomlevel)

                        ##add the HP bar and the EN bar
                        if ship.faction == 'Player':
                            $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.08 * ADJX) + int(zoomlevel * MOVX)
                            $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.66 * ADJY) + int(zoomlevel * MOVY)
                            $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                            add IC.hp_bar:
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                crop (0,0,hp_size,79)

                            $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.08 * ADJX) + int(zoomlevel * MOVX)
                            $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.72 * ADJY) + int(zoomlevel * MOVY)
                            $energy_size = int(405*(float(ship.en)/ship.max_en))
                            add IC.energy_bar:
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                crop (0,0,energy_size,79)

                            text str(ship.hp):
                                xanchor 0.5
                                yanchor 0.5
                                xpos int(xposition+80*zoomlevel)
                                ypos int(yposition+27*zoomlevel)
                                size int(16) #*zoomlevel)
                                font "Font/sui generis rg.ttf"
                                outlines [(2,'000',0,0)]

                        else:    #enemies
                            $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.09 * ADJX) + int(zoomlevel * MOVX)
                            $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.70 * ADJY) + int(zoomlevel * MOVY)
                            $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                            add IC.hp_bar:
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                crop (0,0,hp_size,90)

                            text str(ship.hp):
                                xanchor 0.5
                                yanchor 0.5
                                xpos int(xposition+80*zoomlevel)
                                ypos int(yposition+27*zoomlevel)
                                size int(16) #*zoomlevel)
                                font "Font/sui generis rg.ttf"
                                outlines [(2,'000',0,0)]

    ##show flak icon and intercept text
            if BM.missile_moving:
                for ship in BM.ships:
                    if ship.flaksim != None and ship.flak > 0:
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        $ wait = ship.flaksim[0]
                        $ intercept_count = ship.flaksim[1]
                        if intercept_count:
                            $ BM.battle_log_insert(['attack', 'missile'], "{0} intercepted {1} missiles! Effectiveness: {2}%".format(ship.name, intercept_count, int(ship.flak_effectiveness)))

                        add 'Battle UI/warning icon.png':
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            zoom (zoomlevel/2.5)
                            alpha 0.8
                            at delayed_image(wait,'Battle UI/warning icon.png')

                        $ textcolor = 'f00'
                        if ship.faction == 'Player':
                            $ textcolor = '0f0'

                        text '{} intercepted! \neffectiveness: {}%'.format( intercept_count , int(ship.flak_effectiveness) ):
                            xanchor 0.5
                            yanchor 0.5
    #                        xmaximum 200
                            xpos xposition
                            ypos yposition
                            size 28
                            color textcolor
                            outlines [(2,'000',0,0)]
                            at delay_float_text(yposition,wait)


    ##show missiles on the map that are currently flying in space##

            if BM.missile_moving:
                for missile in BM.missiles:
                    if missile.parent.location != None and missile.target.location != None: #failsafes
                        $xposition = dispx(missile.parent.location[0], missile.parent.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(missile.parent.location[0], missile.parent.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        $next_xposition = dispx(missile.target.location[0],missile.target.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                        $next_yposition = dispy(missile.target.location[0],missile.target.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)

                        $ travel_time = get_ship_distance(missile.parent,missile.target)*MISSILE_SPEED*1.5
                        add missile.lbl:
                            at move_ship(xposition,yposition,next_xposition,next_yposition,travel_time)
                            xanchor 0.5
                            yanchor 0.5
                            zoom (zoomlevel/4.0)

        #                text str(missile.shot_count):
        #                    at move_ship(xposition,yposition,next_xposition,next_yposition,0.1)
        #                    xanchor 0.5
        #                    yanchor 0.5
        #                    size (20/zoomlevel)
        #                    outlines [(1,'000',0,0)]


                    ##DISPLAY MOVEMENT OPTIONS##
            if BM.selectedmode and BM.selected != None:
                if BM.selected.faction == 'Player' and not BM.targetingmode and not BM.phase == 'formation':
                    for tile in BM.selected.movement_tiles:
                        $ lbl = IC.move_tile
                        $ tile_location = (tile[3],tile[4])

                        if get_counter_attack(tile_location) and BM.selected.modifiers['stealth'][0] == 0:
                            $ lbl = im.MatrixColor(lbl,im.matrix.tint(1.0, 0.5, 0.5))

                        if tile_location == BM.mouse_location:
                            $ lbl = hoverglow(lbl)
                        add lbl:
                            zoom (0.2 * zoomlevel)
                            alpha 0.5
                            xanchor 0.5
                            yanchor 0.5
                            xpos tile[0]
                            ypos tile[1]

                        text (str(BM.selected.move_cost*tile[2]) + ' EN'):
                            xpos tile[0]
                            ypos tile[1]
                            xanchor 0.5
                            yanchor 0.5
                            size (20) # * zoomlevel)
                            outlines [(2,'000',0,0)]


    ##targeting window##

            ##if targeting mode is active show a targeting window over all enemy_ships that gives you chance to hit and other data
            if BM.weaponhover != None or BM.targetingmode and BM.selected != None:
                $ selected = BM.selected  #the screen sometimes loses track of BM.selected and crashes so a local is required

                # draw missile path
                if BM.hovered != None and BM.active_weapon != None and (BM.active_weapon.wtype == 'Missile' or BM.active_weapon.wtype == 'Rocket'):
                    $ loc1 = selected.location
                    $ loc2 = BM.hovered.location
                    $ tiles = interpolate_hex(loc1, loc2)
                    $ effective_flak = 0
                    $ total_effective_flak = 0
                    for i, tile in enumerate(tiles):
                        $xposition = dispx(tile[0],tile[1],zoomlevel)
                        $yposition = dispy(tile[0],tile[1],zoomlevel)
                        $xsize = int((HEXW + 4) * zoomlevel)
                        $ysize = int((HEXH + 4) * zoomlevel)

                        add "Battle UI/missile hex.png":
                            xpos xposition
                            ypos yposition
                            size (xsize,ysize)
                            alpha 0.4

                        for ship in BM.ships:
                            if ship.location is not None and not ship.flak_used:
                                if ship.faction != 'Player':
                                    if get_distance(tile,ship.location) <= ship.flak_range:
                                        if BM.active_weapon.wtype == 'Rocket':
                                            #this looks double but missile_eccm is from a ship through upgrades whereas weaponhover.eccm is from the rocket itself. (default 10)
                                            $ effective_flak = (ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm - BM.active_weapon.eccm)
                                        else:
                                            $effective_flak = (ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm)
                                        if effective_flak > 100:
                                            $ effective_flak = 100
                                        elif effective_flak < 0:
                                            $ effective_flak = 0

                                        $ total_effective_flak = total_effective_flak + (1 - total_effective_flak/100.0) * effective_flak
                                        $ ship.flak_used = True

                        if total_effective_flak > 100:
                            $total_effective_flak = 100

                        if i+1 == len(tiles):
                            if total_effective_flak > 0:
                                # FIXME I canna get tile[0] and tile[1] to work properly
                                add 'Battle UI/icon_intercept.png':
                                    zoom (2 * zoomlevel)
                                    #alpha 0.7
                                    xpos xposition
                                    ypos yposition
                                    xoffset xsize/3
                                    yoffset ysize/2
                                    xanchor 0.5
                                    yanchor 0.5
                                text ('{0:.2g}'.format(total_effective_flak) + "%"):
                                    xpos xposition
                                    ypos yposition
                                    xoffset xsize/3
                                    yoffset ysize/2
                                    xanchor 0.5
                                    yanchor 0.5
                                    size (30 * zoomlevel)
                                    color 'bbb'
                                    outlines [(2,'000',0,0)]

                    for ship in BM.ships:
                        $ ship.flak_used = False
                    $ effective_flak = 0
                    $ total_effective_flak = 0

                for ship in BM.ships:
                    if ship.location != None:

                        $skip = False
                        if BM.weaponhover == None:
                            $BM.weaponhover = BM.active_weapon
                        if BM.weaponhover.wtype == 'Support' and (ship.faction != 'Player' or BM.weaponhover.self_buff == True):
                            $skip = True
                        elif BM.weaponhover.wtype != 'Support' and ship.faction == 'Player' and BM.weaponhover.wtype != 'Special':
                            # wtype:'Special' is a support type that's neither a curse nor a buff but can be used on enemies and player units both
                            $skip = True
                        elif BM.weaponhover.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(ship,selected) > 1):
                            $skip = True

                        #the gravity gun is a little... special
                        if BM.weaponhover.name == 'Gravity Gun' and ship.stype != 'Ryder':
                            $skip = True

                        # if not skip:
                        #     #targeting window
                        #     $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        #     $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        #     add "Battle mods/eui/UI/targeting_window_libday.png":
                        #         xpos xposition
                        #         ypos yposition
                        #         xanchor 0.234
                        #         yanchor 0.347
                        #         zoom 0.9
                                
                        #     #chance to hit text
                        #     $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        #     $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        #     text (str(ship.cth) + '%'):
                        #         xpos xposition -15
                        #         ypos yposition -25
                        #         xanchor -1.5
                        #         yanchor -0.5
                        #         size (20) # * zoomlevel)
                        #         min_width 50
                        #         text_align 1.0
                        #         color '000'
                                
                        #     #effective flak text
                        #     $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        #     $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        #     if selected == None:  #workarounds
                        #         $ effective_flak = 0
                        #     else:
                        #         if BM.weaponhover.wtype == 'Rocket':
                        #             #this looks double but missile_eccm is from a ship through upgrades whereas weaponhover.eccm is rom the rocket itself. (default 10)
                        #             $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm - BM.weaponhover.eccm
                        #         else:
                        #             $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm

                        #     if effective_flak < 0:
                        #         $ effective_flak = 0
                        #     elif effective_flak > 100:
                        #         $ effective_flak = 100

                        #     text str(effective_flak):
                        #         xpos xposition -20
                        #         ypos yposition -25
                        #         xanchor 0.0
                        #         yanchor -1.9
                        #         size (17) # * zoomlevel)
                        #         min_width 50
                        #         text_align 1.0
                        #         color 'fff'
                                
                        #     #shield strength
                        #     $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        #     $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        #     text str(ship.shields):
                        #         xpos xposition -20
                        #         ypos yposition -25
                        #         xanchor -0.85
                        #         yanchor -1.9
                        #         size (17) # * zoomlevel)
                        #         min_width 50
                        #         text_align 1.0
                        #         color 'fff'
                            
                        #     #armor strength
                        #     $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        #     $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        #     ##when you hover over a weapon that does kinetic or assault type damage it shows you armor is double as effective
                        #     if BM.weaponhover == None:
                        #         $weapon = BM.active_weapon
                        #     else:
                        #         $weapon = BM.weaponhover
                        #     if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                        #         text (str(ship.armor) + 'x2'):
                        #             xpos xposition -20
                        #             ypos yposition -28
                        #             xanchor -1.75
                        #             yanchor -2.1
                        #             size (15) # * zoomlevel)
                        #             min_width 50
                        #             text_align 1.0
                        #             color 'fff'
                        #             outlines [(1,'000',0,0)]
                        #     else:
                        #         text str(ship.armor):
                        #             xpos xposition -22
                        #             ypos yposition -25
                        #             xanchor -1.6
                        #             yanchor -1.9
                        #             size (17) # * zoomlevel)
                        #             min_width 50
                        #             text_align 1.0
                        #             color 'fff'

                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.75 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.15 * ADJY) + int(zoomlevel * MOVY)
                        add IC.targeting_window:
                            xpos xposition
                            ypos yposition
                            xanchor 0.5
                            yanchor 0.5
                            zoom (zoomlevel/1.3)
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,.92 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,.20 * ADJY) + int(zoomlevel * MOVY)
                        text (str(ship.cth) + '%'):
                            xpos xposition
                            ypos yposition
                            xanchor 0.5
                            yanchor 0.5
                            size (20) # * zoomlevel)
                            color '000'
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.75 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.40 * ADJY) + int(zoomlevel * MOVY)
                        if selected == None:  #workarounds
                            $ effective_flak = 0
                        else:
                            if BM.weaponhover.wtype == 'Rocket':
                                #this looks double but missile_eccm is from a ship through upgrades whereas weaponhover.eccm is rom the rocket itself. (default 10)
                                $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm - BM.weaponhover.eccm
                            else:
                                $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm

                        if effective_flak < 0:
                            $ effective_flak = 0
                        elif effective_flak > 100:
                            $ effective_flak = 100

                        text str(effective_flak):
                            xpos xposition
                            ypos yposition
                            xanchor 1.0
                            yanchor 0.5
                            size (17) # * zoomlevel)
                            color 'fff'
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,.92 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,.40 * ADJY) + int(zoomlevel * MOVY)
                        text str(ship.shields):
                            xpos xposition
                            ypos yposition
                            xanchor 1.0
                            yanchor 0.5
                            size (17) # * zoomlevel)
                            color 'fff'
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,1.0 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.4 * ADJY) + int(zoomlevel * MOVY)
                        ##when you hover over a weapon that does kinetic or assault type damage it shows you armor is double as effective
                        if BM.weaponhover == None:
                            $weapon = BM.active_weapon
                        else:
                            $weapon = BM.weaponhover
                        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                            text (str(ship.armor) + 'x2'):
                                xpos xposition
                                ypos yposition
                                xanchor 0.0
                                yanchor 0.5
                                size (15) # * zoomlevel)
                                color 'fff'
                        else:
                            text str(ship.armor):
                                xpos xposition
                                ypos yposition
                                xanchor 0.0
                                yanchor 0.5
                                size (17) # * zoomlevel)
                                color 'fff'


            #firing the vanguard cannon  [[doesn't seem to be used any more]]
            if BM.vanguard:
                $xposition = dispx(sunrider.locatio[0],sunrider.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(sunrider.locatio[0],sunrider.location[1],zoomlevel) + int(zoomlevel * MOVY)
                add 'Battle UI/vanguard beam wave.png':
                    xanchor 0.0
                    yanchor 0.27
                    xpos int(xposition+100/zoomlevel)
                    ypos yposition
                    size (int(1344/zoomlevel),int(120/zoomlevel))
                    at vanguard_cannon
                    alpha 1.0

            #selecting target for vanguard cannon
            if BM.vanguardtarget:   #creates buttons over enemy ships
                $ loc1 = sunrider.location
                $ loc2 = BM.mouse_location
                if get_distance(loc1, loc2) <= BM.vanguard_range:
                    $tiles = interpolate_hex(loc1, loc2)
                    for i in tiles:
                        $xposition = dispx(i[0],i[1],zoomlevel)
                        $yposition = dispy(i[0],i[1],zoomlevel)
                        $xsize = int((HEXW + 4) * zoomlevel)
                        $ysize = int((HEXH + 4) * zoomlevel)
                        add "Battle UI/vanguard hex.png":
                            xpos xposition
                            ypos yposition
                            size (xsize,ysize)
                            alpha 0.7

            if BM.enemy_vanguard_path is not None:
                for hex in BM.enemy_vanguard_path:
                    $xposition = dispx(hex[0],hex[1],zoomlevel)
                    $yposition = dispy(hex[0],hex[1],zoomlevel)
                    $xsize = int((HEXW + 4) * zoomlevel)
                    $ysize = int((HEXH + 4) * zoomlevel)
                    add "Battle UI/vanguard hex.png":
                        xpos xposition
                        ypos yposition
                        size (xsize,ysize)
                        alpha 0.7

            #the Sunrider warps from one cell to another
            if BM.warping:
                for location in store.flash_locations:
                    $xposition = dispx(location[0],location[1],zoomlevel) + int(zoomlevel * MOVX)
                    $yposition = dispy(location[0],location[1],zoomlevel,-0.5 * ADJY) + int(zoomlevel * MOVY)
                    add 'Battle UI/label_warpflash.png':
    #                    anchor 0.5  #I get a float object not iterable crash. very annoying
                        xpos xposition
                        ypos yposition
                        at warpout
                        zoom 0.25 * zoomlevel

                ##MOVE SHIP FROM GRID TO GRID##
            if BM.moving and BM.selected != None:
                if BM.selected.current_location != None and BM.selected.next_location != None:
                    $xposition = dispx(BM.selected.current_location[0],BM.selected.current_location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(BM.selected.current_location[0],BM.selected.current_location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                    $next_xposition = dispx(BM.selected.next_location[0],BM.selected.next_location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $next_yposition = dispy(BM.selected.next_location[0],BM.selected.next_location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)

                    $travel_time = BM.selected.travel_time

                    add BM.selected.lbl:
                        at move_ship(xposition,yposition,next_xposition,next_yposition,travel_time)
                        xanchor 0.5
                        yanchor 0.5
                        zoom (zoomlevel/2.5)

            if BM.debugoverlay:  #may use this later for AI debug things too
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        $xposition = dispx(a,b,zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(a,b,zoomlevel,0.5 * ADJY) + int(zoomlevel * MOVY)

                        text '{}/{}'.format(a,b):
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition


    ##not part of the viewport##
        if BM.phase != 'formation':
            vbox:
                xalign 1.0
                vbox:
                    xalign 1.0

                    if store.Difficulty < 3 or config.developer:
                        textbutton "restart turn" xalign 1.0 action Jump('restartturn')
                    if BM.mission == 'skirmish' or config.developer:
                        textbutton "Player AI" xalign 1.0 action Return(['toggle player ai'])

                if config.developer:
                    vbox:
                        xalign 1.0
                        textbutton "Debug Cheats" xalign 1.0 action Return(['cheat'])
                        textbutton "Fast Quit" xalign 1.0 action Jump('quit')

                        if BM.debugoverlay:
                            textbutton "coord overlay" xalign 1.0 action SetField(BM,'debugoverlay',False)
                        else:
                            textbutton "coord overlay" xalign 1.0 action SetField(BM,'debugoverlay',True)
                        if BM.show_grid:
                            textbutton "new grid" xalign 1.0 action SetField(BM,'show_grid',False)
                        else:
                            textbutton "old grid" xalign 1.0 action SetField(BM,'show_grid',True)
                        textbutton "debug log" xalign 1.0 action Show('debug_window')
                        textbutton "debug pships" xalign 1.0 action Show('debug_pships')
                        textbutton "debug eships" xalign 1.0 action Show('debug_eships')

        if BM.just_moved:
            textbutton 'cancel movement':
                ypos 70
                text_size 50
                text_color 'fff'
                action Return(['cancel movement'])

        if not BM.showing_orders and not BM.order_used and not BM.missile_moving and not BM.moving and BM.phase == "Player" and sunrider.location != None:
            imagebutton:
                xpos 0
                ypos 0
                idle 'Battle UI/commandbar.png'
                hover hoverglow('Battle UI/commandbar.png')
                action [SetField(BM,'showing_orders',True),Show('orders')]
            text '{!s}'.format(BM.cmd):
                xanchor 1.0
                xpos 165
                ypos 10
                size 30
                color 'fff'
                outlines [(1,'000',0,0)]

        if BM.phase == 'Player':
            $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(0.6, 1.0, 0.5))
            for ship in player_ships:
                if ship.en >= ship.max_en:
                    $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(1.0, 0.6, 0.5))

            imagebutton:
                xpos 90
                yalign 1.0
                idle endturnbutton_idle
                hover hoverglow(endturnbutton_idle)
                action Return(['endturn'])

        ## skirmish buttons start, return, remove, e.music, p.music
        if BM.phase == 'formation':
            imagebutton:
                xpos 170
                yalign 1.0
                idle 'Skirmish/start.png'
                hover hoverglow('Skirmish/start.png')
                action [ If( BM.selected==None , Return(['start']) ) ]

            if BM.mission == 'skirmish':
                imagebutton:
                    xpos 88
                    ypos 690
                    idle 'Skirmish/return.png'
                    hover hoverglow('Skirmish/return.png')
                    action Return(['quit'])

                $ idl = 'Skirmish/remove.png'
                if BM.remove_mode:
                    $ idl = hoverglow(im.MatrixColor('Skirmish/remove.png',im.matrix.tint(1.0, 1.0, 0)))

                imagebutton:
                    xpos 208
                    ypos 759
                    idle idl
                    hover hoverglow('Skirmish/remove.png')
                    action Return(['remove'])

                imagebutton:
                    xpos 328
                    ypos 828
                    idle 'Skirmish/enemymusic.png'
                    hover hoverglow('Skirmish/enemymusic.png')
                    action Show('enemy_music')

                imagebutton:
                    xpos 448
                    ypos 897
                    idle 'Skirmish/playermusic.png'
                    hover hoverglow('Skirmish/playermusic.png')
                    action Show('player_music')

                imagebutton:
                    xpos 414
                    ypos 1022
                    xanchor 0.5
                    yanchor 0.5
                    idle 'Menu/res_button.png'
                    hover hoverglow('Menu/res_button.png')
                    action Jump('RnD_skirmish')
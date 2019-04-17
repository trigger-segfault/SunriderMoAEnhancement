label replay_legionwarpin:
    scene cg_legionwarpin_background with dissolve
    $ renpy.predict("CG/legionwarpin_full.jpg")
    $ renpy.predict("CG/legionwarpin_legion_warp.png")

    #play music "Music/Posthumus_Regium.ogg"

    play sound1 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate2 warp:
        xpos 1940 ypos 200
        ease 0.05 xpos 300 ypos 200
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash:
        xpos 300 ypos 200
    show cg_legionwarpin_missilefrigate2 out
    pause 0.15
    play sound2 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate1 warp:
        xpos 1940 ypos 800
        ease 0.05 xpos 700 ypos 900
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash:
        xpos 700 ypos 900
    show cg_legionwarpin_missilefrigate1 out behind cg_legionwarpin_missilefrigate_warpflash
    pause 0.15
    play sound3 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate3 warp behind cg_legionwarpin_missilefrigate2:
        xpos 1950 ypos 100
        ease 0.05 xpos 975 ypos 100
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash behind cg_legionwarpin_missilefrigate2:
        xpos 975 ypos 100
    show cg_legionwarpin_missilefrigate3 out behind cg_legionwarpin_missilefrigate2
    pause 0.2
    play sound4 "Sound/large_warpout.ogg"
    show cg_legionwarpin_legion warp behind cg_legionwarpin_missilefrigate1:
        xpos 3000 ypos 600
        ease 0.2 xpos 970 ypos 600
    pause 0.2
    scene cg_legionwarpin_legion_full:
        xpos 0.505 ypos 0.56
        pause 1.0
        ease 0.5 zoom 0.4
        ease 0.5 zoom 0.42
    with flash
    pause 4.0
    #$ renpy.pause(4)

    $ renpy.end_replay()

label replay_legion_cerafire:

    scene legion_cerafire1 with dissolve
    play sound "Sound/legion_maincannon.ogg"
    scene legion_cerafire2 with dissolvelong
    pause 1.0
    scene legion_cerafire3 with dissolvemedium
    #$ renpy.pause(1)
    pause 1.0
    scene legion_cerafire4 with dissolve
    show legion_cerafire5 with horizontalwipereversefast
    hide legion_cerafire5 with horizontalwipereversefast
    play sound1 "Sound/explosion1.wav"
    play sound1 "Sound/explosion5.ogg"
    scene legion_cerafire6:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 4
    with dissolve
    scene legion_cerafire7:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 15
    with dissolve

    pause 2.0

    $ renpy.end_replay()

label replay_sunrider_intro:

    play music "Music/Coming_Soon_Part2.ogg" noloop fadeout 0.5
    scene bg space_red
    show sunrider_warpout 1:
        xpos 0.5 ypos 0.5
    show parallax_ship1 behind sunrider_warpout
    show parallax_ship2 behind sunrider_warpout
    show parallax_ship3 behind sunrider_warpout
    with dissolve
    pause 2.0

    show sunrider_warpout_engine:
        xpos 0.5 ypos 0.48
        alpha 0
        linear 5.0 alpha 1
    show ava uniform alt neutral mad:
        xpos 0.2 xzoom -1
    with dissolve

    $ eui.start_afm()

    $ ava("Warp out in 3...!",afm=True)
    #$ renpy.pause(1.0)
    pause 1.0
    $ ava("2...",afm=True)

    hide ava with dissolve
    show captain order 1:
        xpos 0.4
    with dissolve
    $ kay("... ... ...",afm=True)

    #$ renpy.pause(1.0)
    pause 1.0

    show captain order 2 with dissolve
    $ kay("WARP!!!",afm=True)

    $ eui.stop_afm()

    hide captain with dissolve

    pause 1.5
    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_flash:
        xpos 0.5 ypos 0.5
        alpha 1.0
        linear 0.5 alpha 0
    hide sunrider_warpout_engine with dissolvequick
    show sunrider_warpout 3:
        ease 0.3 xpos -1.0 ypos 2.0
    pause 0.5

    window hide
    play sound1 "Music/Posthumus_Regium_Finale.ogg" fadeout 0.5 fadein 0.5 noloop
    scene bg black2 with dissolvelong
    pause 0.1
    show mainlogo:
        subpixel True
        xpos 0.5 ypos 0.5 zoom 1.0
        ease 7.0 zoom 1.1
    with dissolvelong
    $ renpy.pause(9.0)
    hide mainlogo with dissolvelong

    #pause 1.0

    # Stop the replay from changing the currently playing menu music
    stop music fadeout 1.0

    $ renpy.end_replay()

label replay_graveyardescape:

    scene cg_graveyardescape1
    show cg_graveyardescape4
    with dissolve

    #chi "The core's going critical! It's going to-"
    pause 1.0

    play sound1 "sound/explosion5.ogg"
    scene cg_graveyardescape2
    show cg_graveyardescape5
    with dissolve

    #ava "Holy sweet---"
    #kay "Spool up warp drive! WARP! WARP! Get us out of here!!"

    pause 1.0

    play sound2 "sound/large_warpout.ogg"
    show cg_graveyardescape6:
        alpha 0
        ease 0.2 alpha 1
        ease 0.2 alpha 0
    hide cg_graveyardescape5
    show cg_graveyardescape7:
        xpos 0.5 ypos 0.5
        ease 0.6 xpos -1.0 ypos 2.0 zoom 10.0

    pause 2.0

    play sound3 "sound/explosion4.ogg"
    scene cg_graveyardescape3 with dissolve
    scene white with dissolvelong

    pause 2.0

    $ renpy.end_replay()

label replay_weddingcrash:
    scene cg_weddinghall_ceilingspace
    show cg_weddinghall_ceiling
    with dissolve

    show cg_weddinghall_sunrider warp behind cg_weddinghall_ceiling:
        zoom 0.7 xanchor 0.5 xpos 0.5 ypos 0.5
        ease 0.1 zoom 1.0 ypos -0.2

    pause 0.5

    play sound "sound/large_warpout.ogg"

    show cg_weddinghall_sunrider behind cg_weddinghall_ceiling
    show white:
        alpha 0
        ease 0.2 alpha 0.8
        ease 0.2 alpha 0

    pause 3.0

    $ renpy.end_replay()

label replay_emeraldfleet_warpin:

    scene cg_emeraldfleet_warpinback with dissolve
    show cg_emeraldfleet_warpin1:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.5

    play sound1 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin2 behind cg_emeraldfleet_warpin1:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.25

    play sound2 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin3 behind cg_emeraldfleet_warpin2:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.1

    play sound3 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin4 behind cg_emeraldfleet_warpin3:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.1

    play sound4 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin5 behind cg_emeraldfleet_warpin4:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 0.1

    play sound5 "sound/large_warpout.ogg"
    show cg_emeraldfleet_warpin6 behind cg_emeraldfleet_warpin5:
        zoom 0.1
        ease 0.5 zoom 1.0

    pause 3.0

    $ renpy.end_replay()

label replay_porkfleet:
    scene porkfleet_back with dissolve

    show portfleet_1a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound "sound/large_warpout.ogg"
    show portfleet_1b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_1c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_2a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound1 "sound/large_warpout.ogg"
    show portfleet_2b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_2c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_3a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound2 "sound/large_warpout.ogg"
    show portfleet_3b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_3c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_4a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound3 "sound/large_warpout.ogg"
    show portfleet_4b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_4c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_5a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound4 "sound/large_warpout.ogg"
    show portfleet_5b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_5c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_6a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound5 "sound/large_warpout.ogg"
    show portfleet_6b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_6c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_7a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound6 "sound/large_warpout.ogg"
    show portfleet_7b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_7c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_8a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound7 "sound/large_warpout.ogg"
    show portfleet_8b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_8c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_9a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound8 "sound/large_warpout.ogg"
    show portfleet_9b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_9c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.

    show portfleet_10a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound1 "sound/large_warpout.ogg"
    show portfleet_10b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_10c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_11a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound2 "sound/large_warpout.ogg"
    show portfleet_11b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_11c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 3.0
    
    $ renpy.end_replay()

label replay_ongress_assaultin:

    scene cg_ongess_carrier_back with dissolve

    play sound "sound/large_warpout.ogg"

    show cg_ongess_carrier_carrier1:
        xpos 1.0 ypos -0.3
        ease 0.5 xpos 0.0 ypos 0.0
    show white:
        alpha 0
        pause 0.2
        ease 0.2 alpha 0.8
        ease 0.2 alpha 0.0

    pause 2.5
    # fon "An assault carrier... Swift as a battle cruiser, and supported by a squadron of ryders like a carrier..."
    # fon "Capable of both lightning strikes and long range operations. Quite impressive, considering it was made by a single Neutral Rim world."
    # fon "Now, imagine not a single prototype vessel, but an entire fleet of advanced warships built with the resources of all the worlds of the People's Alliance!"

    play sound "sound/large_warpout.ogg"
    show cg_ongess_carrier_carrier2 behind cg_ongess_carrier_carrier1:
        xpos 1.0 ypos -0.3
        ease 0.2 xpos 0.0 ypos 0.0
    pause 0.4

    play sound1 "sound/large_warpout.ogg"
    show cg_ongess_carrier_carrier3 behind cg_ongess_carrier_carrier2:
        xpos 1.0 ypos -0.3
        ease 0.3 xpos 0.0 ypos 0.0

    pause 0.5

    play sound2 "sound/mechfligh.ogg"

    show cg_ongess_carrier_ryder1:
        xpos 1.0 ypos -0.3
        ease 0.5 xpos 0.0 ypos 0.0

    pause 0.4

    show cg_ongess_carrier_ryder2:
        xpos 1.0 ypos -0.3
        ease 0.5 xpos 0.0 ypos 0.0

    pause 0.4

    show cg_ongess_carrier_ryder3:
        xpos 1.0 ypos -0.3
        ease 0.5 xpos 0.0 ypos 0.0

    pause 0.4

    show cg_ongess_carrier_ryder4:
        xpos 1.0 ypos -0.3
        ease 0.5 xpos 0.0 ypos 0.0

    pause 3.0

    $ renpy.end_replay()

label replay_nightmares:

    scene cg_nightmares_back with dissolve
    show cg_nightmares_3:
        ypos 1.0
        ease 5.0 ypos 0.0

    pause 2.0

    show cg_nightmares_2:
        ypos 1.0
        pause 0.5
        ease 5.0 ypos 0.0

    pause 1.5

    show cg_nightmares_1:
        ypos 1.0
        pause 1.0
        ease 5.0 ypos 0.0

    pause 7.5

    $ renpy.end_replay()

label replay_sunrider_warpout:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    $ del Random

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    # Choose a random warp-in background from ones we have seen
    python:
        random_seen_backgrounds = []
        random_available_backgrounds = ["tydaria_orbit","asteroid back1","versta_approach","map_nomodorn","ongess_approach"]
        for background in random_available_backgrounds:
            if renpy.seen_image(background):
                random_seen_backgrounds.append(background)

        # Supply at least one default background if none are present
        if len(random_seen_backgrounds) == 0:
            random_seen_backgrounds.append("tydaria_orbit")

        Random = renpy.random.randint(0,len(random_seen_backgrounds) - 1)
        Random = random_seen_backgrounds[Random]

        del random_seen_backgrounds
        del random_available_backgrounds

    if Random == "tydaria_orbit":
        scene tydaria_orbit:
            ypos 0
            ease 1.5 ypos -120
        with dissolve
    if Random == "asteroid back1":
        scene asteroid back1:
            yanchor 0 ypos 0
            ease 1.5 ypos -200
        with dissolve
    if Random == "versta_approach":
        scene versta_approach:
            ypos 0
            ease 1.5 ypos -120
        with dissolve
    if Random == "map_nomodorn":
        scene map_nomodorn:
            ypos 0
            ease 1.5 ypos -120
        with dissolve
    if Random == "ongess_approach":
        scene ongess_approach:
            ypos -400
            ease 1.5 ypos -600
        with dissolve
    $ del Random

    pause 1.0

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard

    pause 3.0
    
    $ renpy.end_replay()

label replay_sunrider_vanguard:

    play music "Music/March_of_Immortals.ogg"

    call atkanim_sunrider_vanguard from _call_replay_atkanim_sunrider_vanguard

    # Stop the replay from changing the currently playing menu music
    stop music fadeout 1.0
    
    $ renpy.end_replay()

label replay_op:
    
    scene black
    $ renpy.movie_cutscene("cg/OP.avi",stop_music=True)
    
    $ renpy.end_replay()
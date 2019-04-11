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

    $ renpy.pause(3.0)
    
    $renpy.end_replay()

label replay_op:
    
    scene black
    $ renpy.movie_cutscene("cg/OP.avi",stop_music=True)
    
    $renpy.end_replay()
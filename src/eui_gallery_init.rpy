# CENSOR Data inits at 10
init 11:
    # NSFW thumbs that *probably* shouldn't be in a GitHub repo
    if CENSOR == False:
        image eui_thumb_cg_avascene = im.Scale("Censored/avasexcg.jpg", 288, 160, ypos=1)

        image eui_thumb_cg_avacg2 = im.Scale("Censored/avasexcg2.jpg", 288, 160, ypos=1)

    image eui_thumb_cg_asagashower1 = im.Scale("CG/asagashower1.jpg", 288, 160, ypos=1)

    image eui_cg_legionfall_legion:
        "CG/legionfall_legion.png"
        #subpixel True
        xpos 0.01 ypos -0.1

init 11 python:

    #########CHARACTER CGS

    eui.chcg.add("Episode2_CG2", ["cg_epi2_cg2","cg_epi2_cg3"])
    eui.chcg.add("avateatime", ["cg_avateatime"])
    eui.chcg.add("shoujo captain", ["cg_shojocaptain"])
    eui.chcg.add("ryuvianbridge", ["cg_ryuvianbridge","cg_ryuvianbridge_red","cg_ryuvianbridge_empty"])
    eui.chcg.add("weddingcrash", ["cg_weddingcrash1","cg_weddingcrash2"])
    eui.chcg.add(["eui_thumb_cg_asagashower1"], ["cg_asagashower1","cg_asagashower2"], border=True) # No, it appears even when the censor is disabled, no censor. *shrug*
    eui.chcg.add("chigarateatimesad", ["cg_chigarateatime_sad","cg_chigarateatime_embarassed","cg_chigarateatime_happy"])
    eui.chcg.add("sola_beach", ["sola_beach","sola_beach_sad","sola_beach_surprise"])
    eui.chcg.add("chigarabeach", ["chigara_beach1","chigara_beach2","chigara_beach3"])
    eui.chcg.add("chigarahug", ["cg_chigarahug1","cg_chigarahug2"])
    eui.chcg.add("ava_classroom", ["cg_avaclassroom"])
    eui.chcg.add("marayapprove", ["cg_marayapprove"])
    eui.chcg.add("maraygoodbye", ["cg_maraygoodbye"])
    if CENSOR == False:
        eui.chcg.add(["eui_thumb_cg_avascene"], ["cg_avascene"], censor=True, border=True)
        eui.chcg.add(["eui_thumb_cg_avacg2"], ["cg_avacg2"], censor=True, border=True)
    eui.chcg.add("shieldschigarahug", ["cg_shieldschigarahug"])
    eui.chcg.add("avaleverpull", ["cg_avaleverpull1","cg_avaleverpull2"])
    eui.chcg.add("asagaawaken", [
        ["cg_blackjack_awaken1","cg_asaga_awaken 1"],
        ["cg_blackjack_awaken1","cg_asaga_awaken 2"],
        ["cg_blackjack_awaken2","cg_asaga_awaken 3"]
    ])


    #########MECHA CGS

    ###INTRODUCTION
    eui.mccg.add("sunrider_drydock", ["cg sunrider_drydock"], transforms=tr_pan_right(10.0)) # 133
    eui.mccg.add("drydock_destroyed", ["cg drydockdestroyed 0","cg drydockdestroyed 1","cg drydockdestroyed 2","cg drydockdestroyed 3","cg drydockdestroyed 4"], transforms=tr_center) # 534
    eui.mccg.add_replay("legionwarpin", "replay_legionwarpin", parent="cg_legionwarpin_legion_full") # 742
    eui.mccg.add("legion_cera_fleetfire", ["legion_cera_fleetfire1",["legion_cera_fleetfire1","legion_cera_fleetfire2"]]) # 770
    eui.mccg.add("cerafleet", ["cerafleet1","cerafleet2"]) # 776
    eui.mccg.add_replay("legion_cerafire", "replay_legion_cerafire", parent="legion_cerafire7") # 822
    eui.mccg.add_replay("sunrider_intro", "replay_sunrider_intro", parent="chap1_start") # 918

    ###FIRST MISSION PIRATES
    eui.mccg.add("havoc_tydaria_miss1", ["havoc_tydaria_miss1"]) # 1359

    ###RECRUIT IKARI
    eui.mccg.add("phoenixwarpout",[["space back7","phoenixwarpout"],["space back7","phoenixwarpout laser"]]) # 3798
    eui.mccg.add("epi2_cg", [["cg_epi2_cgback","cg_epi2_phoenix"],"cg_epi2_cgset2","cg_epi2_cgset",["cg_epi2_cgset","cg_epi2_explode1"],["cg_epi2_cgset","cg_epi2_explode2"],["cg_epi2_cgset","cg_epi2_explode3"]]) # 5095

    ###RECRUIT CLAUD
    # CG 3 "cg_mochi 3" isn't shown
    eui.mccg.add("mochi", ["cg_mochi 1","cg_mochi 2",EuiCG("cg_mochi 3", parent="cg_mochi 4"),"cg_mochi 4","cg_mochi 5"]) # 6973

    ###RECRUIT SOLA
    eui.mccg.add("graveyard", ["cg_graveyard"], transforms=tr_pan_graveyard(14.0)) # 7648
    eui.mccg.add("deflectbullet", ["cg_deflectbullet1","cg_deflectbullet3","cg_deflectbullet4","cg_deflectbullet5"]) # 8026
    eui.mccg.add_replay("graveyard_escape", "replay_graveyardescape", parent="cg_graveyardescape3") # 8135

    ###ASAGA KIDNAP
    eui.mccg.add_replay("porkfleet_assembled", "replay_porkfleet", parent="portfleet_11c") # 8614
    eui.mccg.add("asagakidnap_legion", ["cg_asagakidnap_legion",["cg_asagakidnap_legion","cg_asagakidnap_legion_text"]]) # 8740
    eui.mccg.add("sunrider_afterkidnap", ["cg_sunrider_afterkidnap",["cg_sunrider_afterkidnap","cg_sunrider_afterkidnap_text"]]) # 8827
    eui.mccg.add_replay("weddingcrash", "replay_weddingcrash", parent="cg_weddinghall_sunrider") # 9963
    eui.mccg.add("legionsurprise", [["cg_legionsurprise1","cg_legionsurprise_sunrider"],["cg_legionsurprise2","cg_legionsurprise_sunrider"],"cg_legionsurprise3"]) # 10499

    ###FARPORT
    eui.mccg.add("farport_charge", ["cg_farport_charge1"], transforms=tr_pan_right(10.0)) # 12359
    eui.mccg.add("pactfleetfarport", ["cg_farport_charge2"], transforms=tr_pan_right(10.0)) # 12380
    eui.mccg.add("legion_farport_fire", ["cg_legion_farport_fire1","cg_legion_farport_fire2","cg_legion_farport_fire3"]) # 12548
    eui.mccg.add("alliancefleet_farport", ["cg_alliancefleet_farport1","cg_alliancefleet_farport2","cg_alliancefleet_farport3","cg_alliancefleet_farport4","cg_alliancefleet_farport5","cg_alliancefleet_farport6","cg_alliancefleet_farport7"]) # 12563
    eui.mccg.add("porkdeath", ["cg_porkdeath1","cg_porkdeath2","cg_porkdeath3"]) # 12604
    eui.mccg.add("blackjack_farport", ["cg_blackjack_farport3","cg_blackjack_farport4","cg_blackjack_farport5","cg_blackjack_farport6"]) # 12622
    eui.mccg.add_replay("emeraldfleet_warpin", "replay_emeraldfleet_warpin", parent="cg_emeraldfleet_warpin6") # 12766
    eui.mccg.add("phoenixpaladin", ["cg_phoenixpaladin"]) # 12717

    ###ONGRESS
    eui.mccg.add_replay("ongress_assaultin", "replay_ongress_assaultin", parent="cg_ongess_carrier_ryder4") # 18249
    eui.mccg.add("bomberline", ["cg_bomberline"]) # 18349
    eui.mccg.add("ongess_port", ["cg_ongessport1","cg_ongessport2"]) # 18404

    ###HELION
    eui.mccg.add("paradoxcore", ["cg_paradoxcore"]) # 20012
    #eui.mccg.add("legionfleetagain", ["cg_legionfleetagain","cg_legionapproachfire"]) # 20399
    # Combine "legionfleetagain" and "alliancefleet_legion" into a single set beacuse they look so similar
    eui.mccg.add("legionfleetagain", ["cg_legionfleetagain","cg_legionapproachfire","cg_alliancefleet_legionfire1","cg_alliancefleet_legionfire2","cg_alliancefleet_legionfire3"]) # 20399, 21364
    eui.mccg.add("helion_alliancefleet", ["cg_helionalliancefleet"], transforms=tr_pan_right(10.0)) # 21053
    eui.mccg.add("legion_approach", ["cg_legionapproach1","cg_legionapproach2"], transforms=tr_pan_right(4.0)) # 21288
    #eui.mccg.add("alliancefleet_legion", ["cg_alliancefleet_legionfire1","cg_alliancefleet_legionfire2","cg_alliancefleet_legionfire3"]) # 21364
    eui.mccg.add("alliancefleet_helion", ["cg_alliancefleet_helion1","cg_alliancefleet_helion2","cg_alliancefleet_helion3","cg_alliancefleet_helion4"]) # 21375

    ###FINAL STAND
    eui.mccg.add("sunriderdamage", ["cg_sunriderdamage1","cg_sunriderdamage2","cg_sunriderdamage3","cg_sunriderdamage4","cg_sunriderdamage5"]) # 21582
    eui.mccg.add("finalstand", ["cg_finalstand1","cg_finalstand2","cg_finalstand3","cg_finalstand4"]) # 21647
    eui.mccg.add("legionfall", [EuiCG(["cg_legionfallback","eui_cg_legionfall_legion"], parent="cg_legionfallback"),"legionfall_end"]) # 21698

    ##NIGHTMARES
    eui.mccg.add("nightmareenter", ["cg_nightmare_enter","cg_nightmare_explode","cg_nightmaredefeated"]) # 21826
    eui.mccg.add_replay("nightmares","replay_nightmares", parent="cg_nightmares_1") # 21869

    ###MISC
    eui.mccg.add_replay("sunrider_warpout", "replay_sunrider_warpout", parent="sunrider_warpout_standard out")
    eui.mccg.add_replay("sunrider_vanguard", "replay_sunrider_vanguard", parent="atkanim_sunrider_vanguard")
    eui.mccg.add_replay("OP", "replay_op")

    ############BACKGROUNDS

    eui.bg.add("hangar", ["bg hangar"])
    eui.bg.add("bridge", ["bg bridge","bg bridgered"])
    # Unused: Always unlocked
    eui.bg.add("bridgenest", ["bg bridgenest"], parent="bridge")
    eui.bg.add("engineering", ["bg engineering"])
    eui.bg.add("messhall", ["bg messhall"])
    eui.bg.add("captainsloft", ["bg captainsloft"])
    eui.bg.add("captainsoffice", ["bg captainsoffice","bg captainsoffice_nolights","bg captainsoffice2","bg captainsoffice2_dark"])
    eui.bg.add("lab", ["bg lab"])
    eui.bg.add("brig", ["bg brig"])
    eui.bg.add("messhallwindows", ["bg messhallwindows"])
    eui.bg.add("sickbay", ["bg sickbay"])
    eui.bg.add("legionwindows", ["bg legionwindows"])
    eui.bg.add("starpalace", ["bg starpalace"])
    eui.bg.add("beach1", ["bg beach1"])
    eui.bg.add("beach2", ["bg beach2","bg beach2_night"])
    eui.bg.add("cabin", ["bg logcabin","bg cabinday"])
    eui.bg.add("cabindeck", ["bg cabindeck"])
    eui.bg.add("cabinoutside", ["bg cabinoutside"])
    eui.bg.add("ongess1", ["bg ongess1"])
    eui.bg.add("ongess2", ["bg ongess2"])
    eui.bg.add("holdingcell", ["bg holdingcell"])
    eui.bg.add("ongess3", ["bg ongess3"])
    eui.bg.add("classroom", ["bg classroom","bg classroomnight"])
    eui.bg.add("city", ["bg city"])
    eui.bg.add("apartmentfront", ["bg apartmentfront"])
    #TODO: Decide if we show this as a background or not at all
    eui.bg.add("sky", ["cg_sky"])
    eui.bg.add("corebridge", ["bg corebridge"])
    eui.bg.add("balcony", ["bg balcony"])
    if CENSOR == False:
        eui.bg.add("avaroom", ["bg avaroom"], censor=True) # Only appears with Denpasoft patch
    eui.bg.add("engineroom", ["bg engineroom"])

    # Other
    #eui.bg.add("asagacorner", ["asagacorner"])
    #Probably won't include deleted scene images

    #########MUSIC

    eui.tracks.add("A Dark Dream", "A_Dark_Dream")
    eui.tracks.add("Arcadia", "Arcadia")
    eui.tracks.add("As I Figure", "As_I_Figure")
    eui.tracks.add("Battle Against Time", "Battle_Against_Time")
    eui.tracks.add("Boukyou", "boukyou")
    eui.tracks.add("Colors of an Orchestra", "Colors_Of_An_Orchestra")
    eui.tracks.add("Coming Soon (End)", "Coming_Soon_End")
    eui.tracks.add("Coming Soon (Part 1)", "Coming_Soon_Part1")
    eui.tracks.add("Coming Soon (Part 2)", "Coming_Soon_Part2")
    # Unused: unlock associated track
    eui.tracks.add("Daydream (Alternate)", "Daydream_Alternate", parent="Daydream_Reprise")
    eui.tracks.add("Daydream (Reprise)", "Daydream_Reprise")
    eui.tracks.add("Daydream (Tides)", "DayDream_Cut") # Not the correct filename casing, but what is used in-game
    eui.tracks.add("Driving the Top Down", "Driving_the_Top_Down")
    eui.tracks.add("Dusty Universe", "Dusty_Universe")
    eui.tracks.add("El Prendimiento", "el_prendimiento")
    # Unused: unlock associated track
    eui.tracks.add("Firn", "Firn", parent="Firn_ED")
    eui.tracks.add("Firn (Credits)", "Firn_ED")
    eui.tracks.add("Grasping Some Beauty", "Grasping_Some_Beauty")
    eui.tracks.add("Harunokagayaki", "harunokagayaki")
    eui.tracks.add("Hinokageri", "hinokageri")
    eui.tracks.add("Hinokageri (Orchestra)", "hinokageri_orchestra")
    eui.tracks.add("Honor", "Honor")
    # Unused: Beat the game to unlock
    eui.tracks.add("Inhale (Unused)", "Inhale", conditions="renpy.seen_label('aftercredits7')")
    eui.tracks.add("Intruders", "Intruders")
    eui.tracks.add("Invasion of Chaos", "Invasion of Chaos")
    eui.tracks.add("La Busqueda De Ianna", "La_Busqueda_de_Lanna")
    eui.tracks.add("Lighting Soul", "Lighting_Soul")
    eui.tracks.add("Limitless", "Limitless")
    eui.tracks.add("Love", "Love")
    eui.tracks.add("Love Theme", "Love_Theme")
    eui.tracks.add("March of Immortals", "March_of_Immortals")
    eui.tracks.add("March to Glory", "March_to_Glory")
    eui.tracks.add("Mission Briefing", "Mission_Briefing")
    eui.tracks.add("Monkeys Spinning Monkeys", "Monkeys_Spinning_Monkeys")
    eui.tracks.add("Moonlit Night", "Moonlit_Night")
    eui.tracks.add("New Dawn", "New_Dawn")
    eui.tracks.add("One Day in August", "One_Day_In_August")
    eui.tracks.add("Overpower", "Overpowered")
    eui.tracks.add("Poltergeist Attack", "Poltergeist_Attack")
    eui.tracks.add("Posthumus Regnum", "Posthumus_Regium")
    eui.tracks.add("Posthumus Regnum Finale", "Posthumus_Regium_Finale")
    eui.tracks.add("Powerful", "Powerful")
    eui.tracks.add("Prayers", "Prayers")
    eui.tracks.add("Proditionis", "Proditionis")
    eui.tracks.add("Riding With the Wind", "Riding_With_the_Wind")
    eui.tracks.add("Run Amok", "Run Amok")
    eui.tracks.add("Samfree", "SAMFREE")
    eui.tracks.add("Sora no Senritsu", "Sora_no_Senritsu")
    # Unused: Beat the game to unlock
    eui.tracks.add("Space Ace (Unused)", "Space_Ace", conditions="renpy.seen_label('aftercredits7')")
    eui.tracks.add("Star of Bethlehem", "Star_of_Bethlehem")
    eui.tracks.add("Sui Generis", "Sui_Generis")
    eui.tracks.add("The Tumbrel", "The Tumbrel")
    eui.tracks.add("The Beginning of the Adventure", "The_Beginning_Of_The_Adventure")
    eui.tracks.add("The Bladed Druid", "The_Bladed_Druid")
    eui.tracks.add("The Departure", "The_Departure")
    eui.tracks.add("The Flight of the Crow", "The_Flight_of_the_Crow")
    eui.tracks.add("The Meteor", "The_Meteor")
    eui.tracks.add("The Rest of the Ents", "The_Rest_of_the_Ents")
    eui.tracks.add("The Third Fall", "TheThirdFall")
    eui.tracks.add("Tides", "Tides")
    eui.tracks.add("Titan", "Titan")
    eui.tracks.add("Tokyo Lights", "Tokyo_Lights")
    eui.tracks.add("Valve", "Valve")
    eui.tracks.add("Wedding March", "wedding_march")
    eui.tracks.add("World Builder", "WorldBuilder")
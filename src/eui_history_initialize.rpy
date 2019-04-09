label eui_skiptomaskofarcadius:
    scene black
    with dissolve
    
    call initialize from _call_initialize_2_eui

    call firstvariables from _call_firstvariables_2_eui

    python:
        BM.money = 19000
        BM.cmd = 4000
        BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp'] ## Adds in SRW, since the plot event to add it is skipped. Tested it in the current steam ver with and without, should work.
        gal_event = 'jumptogalaxy'
        alliancecruiser1 = None
        alliancecruiser2 = None

        warpto_tydaria = True
        warpto_occupiedcera = True
        warpto_astralexpanse = True
        warpto_pactstation1 = True
        warpto_versta = True
        warpto_nomodorn = True
        warpto_ryuvia = True
        warpto_farport = True
        warpto_ongess = False

        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault(),SunriderPulse()]
        sunrider = create_ship(Sunrider(),(1,1),sunrider_weapons)

        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
        blackjack = create_ship(BlackJack(),(1,2),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
        liberty = create_ship(Liberty(),(5,7),liberty_weapons)

        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(9,5),phoenix_weapons)

        bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
        bianca = create_ship(Bianca(),(14,7),bianca_weapons)

        seraphim_weapons = [SeraphimKinetic(),Awaken()]
        seraphim = create_ship(Seraphim(),(6,8),seraphim_weapons)

        paladin_weapons = [PaladinMissile(),PaladinAssault(),PaladinKinetic()]
        paladin = create_ship(Paladin(),(9,8),paladin_weapons)

        sunrider.repair_drones = 0

        cal_location = "captainsloft"
        cal_event = "ftltransponder"
        res_location = "lab"
        res_event = "allocatefunds"

        for i in range(12):
            setattr(store, 'mission{}_complete'.format(i + 1), True)

    call eui_beginstat from _call_eui_beginstat

    #if store.Difficulty == 3:
    $ show_message('Please select your difficulty.',0.5,0.8,2)
    show screen gameprefs

    window hide

    stop music fadeout 1.5

    show eyecatch_top with eyecatch_wipe
    show eyecatch_bottom with eyecatch_wiperev
    show eyecatch_logo with dissolve
    $ renpy.pause (2.0)

    # This action before the jump is the same as passing True as a parameter
    # to beachepisode, but we can't do that with jump so we do it here.
    $ BM.lowest_difficulty = store.Difficulty
    jump beachepisode

label eui_beginstat:
    if eui.his_ceraflag == True:
        $ captain_prince += 1
    if eui.his_ceraflag == False:
        $ captain_moralist += 1

    if eui.his_professionalreunion == True:
        $ affection_ava -= 1
    if eui.his_professionalreunion == False:
        $ affection_ava += 2
        
    if eui.his_loosenrule == True:
        $ supportedasagacards = True
        $ affection_asaga += 3
        $ captain_moralist += 1
    if eui.his_loosenrule == False:
        $ supportedasagacards = False
        $ affection_ava += 2
        $ captain_prince += 1
        
    if eui.his_pactspire == True:
        $ captain_prince += 3
        $ affection_ava += 1
        
    if eui.his_capturetraffickers == True:
        $ captain_moralist += 3
        $ affection_chigara += 1
        $ affection_asaga += 3
    if eui.his_capturetraffickers == False:
        $ captain_moralist += 3
        $ affection_ava += 1
        $ affection_asaga += 4
        
    if eui.his_diplomatssaved == True:
        $ Saveddiplomats = True
        $ captain_moralist += 13
        $ affection_asaga += 2
    if eui.his_diplomatssaved == False:
        $ Saveddiplomats = False
        $ captain_prince += 13
        $ affection_icari += 4
        $ affection_asaga -= 2
        $ affection_ava += 1

    if eui.his_mochirescue == True:
        $ protectmochi = True
        $ captain_moralist += 2
    if eui.his_mochirescue == False:
        $ protectmochi = False
        $ captain_prince += 2

    if eui.his_claudesupport == True:
        $ affection_claude += 2

    if eui.his_chigaraforgive == True:
        $ affection_chigara += 1

    if eui.his_solacareful == True:
        $ affection_sola += 1
        $ captain_moralist += 1
    if eui.his_solacareful == False:
        $ captain_prince += 1

    if eui.his_noallianceregulations == True:
        $ affection_icari += 2
    if eui.his_noallianceregulations == False:
        $ affection_tera += 2

    if eui.his_cafeteriaasaga == True:
        $ affection_asaga += 1
    if eui.his_cafeteriaasaga == False:
        $ affection_chigara += 1

    if eui.his_notinterestedinfame == True:
        $ captain_moralist += 1
    if eui.his_notinterestedinfame == False:
        $ captain_prince += 1

    if eui.his_beforefarportsuspectalliance == False:
        $ captain_moralist += 1
        $ affection_tera += 3
        
    if eui.his_techdangerous == True:
        $ captain_moralist += 1
    if eui.his_techdangerous == False:
        $ affection_chigara += 1

    return


label eui_beginstat_old:
    if his_ceraflag == True:
        $ captain_prince += 1
    if his_ceraflag == False:
        $ captain_moralist += 1

    if his_professionalreunion == True:
        $ affection_ava -= 1
    if his_professionalreunion == False:
        $ affection_ava += 2
        
    if his_loosenrule == True:
        $ supportedasagacards = True
        $ affection_asaga += 3
        $ captain_moralist += 1
    if his_loosenrule == False:
        $ supportedasagacards = False
        $ affection_ava += 2
        $ captain_prince += 1
        
    if his_pactspire == True:
        $ captain_prince += 3
        $ affection_ava += 1
        
    if his_capturetraffickers == True:
        $ captain_moralist += 3
        $ affection_chigara += 1
        $ affection_asaga += 3
    if his_capturetraffickers == False:
        $ captain_moralist += 3
        $ affection_ava += 1
        $ affection_asaga += 4
        
    if his_diplomatssaved == True:
        $ Saveddiplomats = True
        $ captain_moralist += 13
        $ affection_asaga += 2
    if his_diplomatssaved == False:
        $ Saveddiplomats = False
        $ captain_prince += 13
        $ affection_icari += 4
        $ affection_asaga -= 2
        $ affection_ava += 1

    if his_mochirescue == True:
        $ protectmochi = True
        $ captain_moralist += 2
    if his_mochirescue == False:
        $ protectmochi = False
        $ captain_prince += 2

    if his_claudesupport == True:
        $ affection_claude += 2

    if his_chigaraforgive == True:
        $ affection_chigara += 1

    if his_solacareful == True:
        $ affection_sola += 1
        $ captain_moralist += 1
    if his_solacareful == False:
        $ captain_prince += 1

    if his_noallianceregulations == True:
        $ affection_icari += 2
    if his_noallianceregulations == False:
        $ affection_tera += 2

    if his_cafeteriaasaga == True:
        $ affection_asaga += 1
    if his_cafeteriaasaga == False:
        $ affection_chigara += 1

    if his_notinterestedinfame == True:
        $ captain_moralist += 1
    if his_notinterestedinfame == False:
        $ captain_prince += 1

    if his_beforefarportsuspectalliance == False:
        $ captain_moralist += 1
        $ affection_tera += 3
        
    if his_techdangerous == True:
        $ captain_moralist += 1
    if his_techdangerous == False:
        $ affection_chigara += 1

    return
init +2:
    screen battlewarning:

        modal True

        add "UI/battlestations_bar.png" at tr_fadein(0.5):
            ypos 400 xalign 0.5

        add "UI/battlestations_menuback.png" at tr_fadein(0.5):
            ypos 500 xalign 0.5

        add "UI/battlestations.png" at tr_battlestations

        imagebutton at tr_menubutton(0.55,807):
            ypos 550
            idle "UI/battlestations_quicksave.png"
            hover tr_hoverglow("UI/battlestations_quicksave.png")
            activate_sound "sound/beep1.ogg"
            action QuickSave(message='Quick save complete.', newest=False)
        
        imagebutton at tr_menubutton(0.6,807):
            ypos 620
            idle "UI/battlestations_research.png"
            hover tr_hoverglow("UI/battlestations_research.png")
            activate_sound "sound/beep1.ogg"
            action ShowUpgrades()

        imagebutton at tr_menubutton(0.65,807):
            ypos 690
            idle "UI/battlestations_store.png"
            hover tr_hoverglow("UI/battlestations_store.png")
            activate_sound "sound/beep1.ogg"
            action ShowStore()

        imagebutton at tr_menubutton(0.7,807):
            ypos 760
            idle "UI/battlestations_proceed.png"
            hover tr_hoverglow("UI/battlestations_proceed.png")
            activate_sound "sound/drum.ogg"
            action Return('continue')
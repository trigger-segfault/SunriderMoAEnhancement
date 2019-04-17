init -1:
    transform tr_fadein(ddelay):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1
        on hide:
            pause ddelay
            ease 0.3 alpha 0

    # Fade out faster
    transform tr_fadein_2(ddelay):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1
        on hide:
            #pause ddelay
            ease 0.3 alpha 0

    transform tr_menubutton(ddelay,xxpos):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1  xpos xxpos
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos (xxpos+300)
    
    transform tr_menubutton_onshow(ddelay,xxpos):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1  xpos xxpos
        on hide:
            pause ddelay
    
    transform tr_menubutton_onhide(ddelay,xxpos):
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos (xxpos+300)
            
    transform tr_decision(ddelay):
        alpha 0 xpos 860
        pause ddelay
        ease 0.3 alpha 1  xpos 960
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos 860
            
    transform tr_inactive(img1):
        im.MatrixColor(img1,im.matrix.brightness(-0.4))
            
    transform tr_hoverglow(img1):
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.2))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(.0))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.15))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(0.0))
        pause 0.05
        repeat
        
    transform tr_sidemenu(endpos):
        ypos -80 xpos 1645
        ease 0.3 ypos endpos
        on hide:
            ease 0.3 ypos -80
            
    transform tr_decision(ddelay):
        alpha 0 xpos 860
        pause ddelay
        ease 0.3 alpha 1  xpos 960
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos 860

    transform tr_pan_right(duration):
        xalign 0.0
        linear duration xalign 1.0
    transform tr_pan_left(duration):
        xalign 1.0
        linear duration xalign 0.0
    transform tr_pan_down(duration):
        yalign 0.0
        linear duration yalign 1.0
    transform tr_pan_up(duration):
        yalign 1.0
        linear duration yalign 0.0
    transform tr_center:
        xalign 0.5 yalign 0.5
    transform tr_pan_graveyard(duration):
        xalign 0.0 yalign 0.0
        linear duration xalign 1.0 yalign 1.0
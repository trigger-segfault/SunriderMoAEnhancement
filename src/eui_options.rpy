init +1 python:
    #style.window.background = Solid((0, 0, 128, 128))
    #style.window.xpadding = 10
    #style.window.ypadding = 5
    #style.window.xmargin = 10
    #style.window.ymargin = 5
    #style.window.xfill = True
    #style.window.yfill = False
    #style.window.xminimum = 0 # Includes margins and padding.
    #style.window.yminimum = 150 # Includes margins and padding.
    #style.window.clear()

    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = "UI/messagebox.png"

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 140
    style.window.right_margin = 140
    style.window.top_margin = 0
    style.window.bottom_margin = 0

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 6
    style.window.right_padding = 6
    style.window.top_padding = 6
    style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yanchor = 0.0
    style.window.yminimum = 500

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.diamond(
        ## Theme: Diamond
        ## Color scheme: Colorblind

        ## The color of an idle widget face.
        widget = "#898989",

        ## The color of a focused widget face.
        widget_hover = "#464646",

        ## The color of the text in a widget.
        widget_text = "#CCCCCC",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#F2F2F2",

        ## The color of a disabled widget face.
        disabled = "#898989",

        ## The color of disabled widget text.
        disabled_text = "#666666",

        ## The color of informational labels.
        label = "#c2c2c2",

        ## The color of a frame containing widgets.
        frame = "#252525",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#393939",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#393939",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )
        
    #style.default.font = "Fonts/ShareTech-Regular.ttf"

    ## The default size of text.

    #style.default.size = 30

    style.default.layout = "tex"
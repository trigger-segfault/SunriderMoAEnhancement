# Why Ren'Py decides to set the autosave slot count at this point, I'll never know
init +1701 python:
    # Why is there no config for this?
    eui.quicksave_slots = 12
    config.autosave_slots = 12

init +1 python:
    # FULL HD
    config.thumbnail_width = 266
    config.thumbnail_height = 150

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

    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    # Don't set because it will mess up a small selection of unmodified UIs.
    style.default.font = "Fonts/ShareTech-Regular.ttf"

    ## The default size of text.

    # Don't set because it will mess up a small selection of unmodified UIs.
    style.default.size = 30

    # Prevent text from performing subtitle wrapping which looks terrible when not centered
    style.default.layout = "tex"

    #########################################
    ## Console styles

    style._console_text.size = 28
    style._console_text.font = "Fonts/ShareTech-Regular.ttf"

    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolvemedium

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    ######################################################################
    # First up, we define a bunch of configuration variables, which the
    # user can change.
    
    # What we do on a quit, by default.
    #config.quit_action = ui.gamemenus("_quit_prompt")
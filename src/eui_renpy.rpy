init -1500 python:
    # Doesn't exist in this version of Ren'Py yet
    class EuiToggleScreen(Action, DictEquality):
        """
        :doc: control_action

        This toggles the visibility of `screen`. If it is not currently
        shown, the screen is shown with the provided arguments. Otherwise,
        the screen is hidden.

        If not None, `transition` is use to show and hide the screen.
        """

        args = None

        def __init__(self, screen, transition=None, *args, **kwargs):
            self.screen = screen
            self.transition = transition
            self.args = args
            self.kwargs = kwargs

        def predict(self):
            renpy.predict_screen(self.screen, *self.args, **self.kwargs)

        def __call__(self):
            if renpy.get_screen(self.screen):
                renpy.hide_screen(self.screen)
            else:
                renpy.show_screen(self.screen, *self.args, **self.kwargs)

            if self.transition is not None:
                renpy.transition(self.transition)

            renpy.restart_interaction()

        def get_selected(self):
            return renpy.get_screen(self.screen) is not None

    # For some reason Ren'Py thinks the ImageButton class doesn't exist
    class EuiImageButton(Button):
        """
        Used to implement the guts of an image button.
        """

        def __init__(self,
                    idle_image,
                    hover_image,
                    insensitive_image = None,
                    activate_image = None,
                    selected_idle_image = None,
                    selected_hover_image = None,
                    selected_insensitive_image = None,
                    selected_activate_image = None,
                    style='image_button',
                    clicked=None,
                    hovered=None,
                    **properties):

            insensitive_image = insensitive_image or idle_image
            activate_image = activate_image or hover_image

            selected_idle_image = selected_idle_image or idle_image
            selected_hover_image = selected_hover_image or hover_image
            selected_insensitive_image = selected_insensitive_image or insensitive_image
            selected_activate_image = selected_activate_image or activate_image

            self.state_children = dict(
                idle_ = renpy.easy.displayable(idle_image),
                hover_ = renpy.easy.displayable(hover_image),
                insensitive_ = renpy.easy.displayable(insensitive_image),
                activate_ = renpy.easy.displayable(activate_image),

                selected_idle_ = renpy.easy.displayable(selected_idle_image),
                selected_hover_ = renpy.easy.displayable(selected_hover_image),
                selected_insensitive_ = renpy.easy.displayable(selected_insensitive_image),
                selected_activate_ = renpy.easy.displayable(selected_activate_image),
                )

            super(EuiImageButton, self).__init__(None,
                                            style=style,
                                            clicked=clicked,
                                            hovered=hovered,
                                            **properties)

        def visit(self):
            return self.state_children.values()

        def get_child(self):
            return self.style.child or self.state_children[self.style.prefix]
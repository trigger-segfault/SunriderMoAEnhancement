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

    class EuiIfReplay(Action, DictEquality):
        def __init__(self,true=None,false=None):
            self.true = true
            self.false = false

        def get_action(self):
            if not renpy.store._in_replay is None:
                return self.true
            else:
                return self.false

        def get_sensitive(self):
            return renpy.ui.is_sensitive(self.get_action())

        def get_selected(self):
            return renpy.ui.is_selected(self.get_action())

        def periodic(self):
            action = self.get_action()
            if isinstance(action, (list, tuple)):
                for i in action:
                    i.periodic()

            elif isinstance(action, Action):
                action.periodic()

        def predict(self):
            action = self.get_action()
            if isinstance(action, (list, tuple)):
                for i in action:
                    i.predict()

            elif isinstance(action, Action):
                action.predict()

        def __call__(self):
            action = self.get_action()
            if isinstance(action, (list, tuple)):
                for i in action:
                    i()

            elif isinstance(action, Action):
                action()

    class EuiEvalIf(Action, DictEquality):

        def __init__(self,expression,true=None,false=None):
            self.expression = expression
            self.true = true
            self.false = false

        def get_action(self):
            if eval(self.expression):
                return self.true
            else:
                return self.false

        def get_sensitive(self):
            return renpy.ui.is_sensitive(self.get_action())

        def get_selected(self):
            return renpy.ui.is_selected(self.get_action())

        def periodic(self):
            action = self.get_action()
            if isinstance(action, (list, tuple)):
                for i in action:
                    i.periodic()

            elif isinstance(action, Action):
                action.periodic()

        def predict(self):
            action = self.get_action()
            if isinstance(action, (list, tuple)):
                for i in action:
                    i.predict()

            elif isinstance(action, Action):
                action.predict()

        def __call__(self):
            action = self.get_action()
            if isinstance(action, (list, tuple)):
                for i in action:
                    i()

            elif isinstance(action, Action):
                action()

    class EuiProportionalScale(im.ImageBase):
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            img = im.image(imgname)
            super(EuiProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
            self.imgname = imgname
            self.image = img
            self.maxwidth = maxwidth
            self.maxheight = maxheight
            self.bilinear = bilinear

        def load(self):
            surf = im.cache.get(self.image)
            width, height = surf.get_size()
            
            ratio = min(self.maxwidth/float(width), self.maxheight/float(height))
            width = int(round(ratio * width))
            height = int(round(ratio * height))
            
            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(surf, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(surf, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv

        def predict_files(self):
            return self.image.predict_files()

    class EuiBonusItemScale(im.ImageBase):
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            img = Image(imgname)
            super(EuiBonusItemScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
            self.imgname = imgname
            self.image = img
            self.maxwidth = maxwidth
            self.maxheight = maxheight
            self.bilinear = bilinear

        def load(self):
            surf = im.cache.get(self.image)
            width, height = surf.get_size()
            
            ratio = self.maxwidth / float(width)
            width = int(round(ratio * width))
            height = int(round(ratio * height))
            
            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(surf, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(surf, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv.subsurface((0, 0, min(rv.get_width(), self.maxwidth), min(rv.get_height(), self.maxheight)))

        def predict_files(self):
            return self.image.predict_files()

    class EuiBonusItemRender(renpy.Displayable):
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            renpy.Displayable.__init__(self, **properties)
            #self.mod = mod
            #self.zoom = mod.zoom
            #self.image = mod#renpy.easy.displayable(mod.image)
            self.image = renpy.displayable(imgname)
            self.maxwidth = maxwidth
            self.maxheight = maxheight
            self.bilinear = bilinear

        def render(self, width, height, st, sa):

            image_render = renpy.render(self.image, width, height, st, sa)
            image_width, image_height = image_render.get_size()

            render = renpy.Render(image_width, image_height)
            render.blit(image_render, (0, 0))

            surf = render.render_to_texture()
            
            ratio = self.maxwidth / float(image_width)
            self.width = int(round(ratio * image_width))
            self.height = int(round(ratio * image_height))

            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(surf, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(surf, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv.subsurface((0, 0, min(rv.get_width(), self.maxwidth), min(rv.get_height(), self.maxheight)))
    # class EuiBonusItemRender(renpy.Displayable):
    #     def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
    #         renpy.Displayable.__init__(self, **properties)
    #         #self.mod = mod
    #         #self.zoom = mod.zoom
    #         #self.image = mod#renpy.easy.displayable(mod.image)
    #         self.image = renpy.displayable(imgname)
    #         self.maxwidth = maxwidth
    #         self.maxheight = maxheight
    #         self.bilinear = bilinear

    #     def render(self, width, height, st, sa):

    #         image_render = renpy.render(self.image, width, height, st, sa)
    #         image_width, image_height = image_render.get_size()

    #         render = renpy.Render(image_width, image_height)
    #         surf.blit(image_render, (0, 0))
            
    #         ratio = self.maxwidth / float(image_width)
    #         self.width = int(round(ratio * image_width))
    #         self.height = int(round(ratio * image_height))

    #         if self.bilinear:
    #             try:
    #                 renpy.display.render.blit_lock.acquire()
    #                 rv = renpy.display.scale.smoothscale(surf, (width, height))
    #             finally:
    #                 renpy.display.render.blit_lock.release()
    #         else:
    #             try:
    #                 renpy.display.render.blit_lock.acquire()
    #                 rv = renpy.display.pgrender.transform_scale(surf, (width, height))
    #             finally:
    #                 renpy.display.render.blit_lock.release()
    #         return rv.subsurface((0, 0, min(rv.get_width(), self.maxwidth), min(rv.get_height(), self.maxheight)))

            # Create the render we will return.
            #render = renpy.Render(width, height)

            # t = Transform(child=self.image,size=(self.width,self.height))

            # child_render = renpy.render(t, width, height, st, sa)

            # # Create the render we will return.
            # render = renpy.Render(self.width, self.height)

            # # Blit (draw) the child's render to our render.
            # render.blit(child_render, (0, 0))

            # # Return the render.
            # return render


            
            # if self.bilinear:
            #     try:
            #         renpy.display.render.blit_lock.acquire()
            #         rv = renpy.display.scale.smoothscale(surf, (width, height))
            #     finally:
            #         renpy.display.render.blit_lock.release()
            # else:
            #     try:
            #         renpy.display.render.blit_lock.acquire()
            #         rv = renpy.display.pgrender.transform_scale(surf, (width, height))
            #     finally:
            #         renpy.display.render.blit_lock.release()
            # return rv.subsurface((0, 0, min(rv.get_width(), self.maxwidth), min(rv.get_height(), self.maxheight)))
            #newwidth, newheight = child_render.get_size()

            
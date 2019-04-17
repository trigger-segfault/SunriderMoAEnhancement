init -1 python:

    class EnhancementModBlankItem(_object):
        def make_button(self):
            return Text("")
        def make_text(self):
            return Text("")

    # Conditions for images really need to better organized.
    # Right now it's not possible to use both the default unlock and extra conditions,
    # you also can't use gallery.allprior which is a pretty handy condition.

    class EuiCG(_object):
        def __init__(self, images, parent=None, transforms=None, conditions=None):
            if isinstance(images, list):
                self.images = images
            elif images is None:
                self.images = []
            else:
                self.images = [ images ]

            if isinstance(conditions, list):
                self.conditions = conditions
            elif conditions is None:
                self.conditions = []
            else:
                self.conditions = [ conditions ]

            self.parent = parent

            if isinstance(transforms, list):
                self.transforms = transforms
            elif transforms is None:
                self.transforms = []
            else:
                self.transforms = [ transforms ]

    class EnhancementModCGItem(_object):
        def __init__(self, prefix, gallery, name, thumb, images, parent=None, conditions=None, transforms=None, censor=False, replay=False, border=False):
            self.gallery = gallery
            self.name = name
            if isinstance(thumb, list):
                # A really stupid way of overriding the default thumb path
                self.thumb = thumb[0]
            else:
                self.thumb = "mods/eui/cg/thumbs/{0}/{1}.jpg".format(prefix,thumb)
            self.border = border
            if isinstance(images, list):
                self.images = images
            else:
                self.images = [ images ]

            # Convert all images to EuiCG
            for i in range(0, len(self.images)):
                image = self.images[i]
                if not isinstance(image, EuiCG):
                    self.images[i] = EuiCG(image)
                elif not image.parent is None:
                    if renpy.has_label(image.parent):
                        image.conditions += [ "renpy.seen_label('{0}')".format(image.parent) ]
                    else:
                        image.conditions += [ "renpy.seen_image('{0}')".format(image.parent) ]

            if isinstance(conditions, list):
                self.conditions = conditions
            elif conditions is None:
                self.conditions = []
            else:
                self.conditions = [ conditions ]

            self.parent = parent
            if not parent is None:
                if renpy.has_label(parent):
                    self.conditions += [ "renpy.seen_label('{0}')".format(parent) ]
                else:
                    self.conditions += [ "renpy.seen_image('{0}')".format(parent) ]

            if isinstance(transforms, list):
                self.transforms = transforms
            elif transforms is None:
                self.transforms = []
            else:
                self.transforms = [ transforms ]
            self.censor = censor
            self.replay = replay

        @property
        def label(self):
            if self.replay == True:
                return self.images[0].images[0]

        def make_button(self):
            if self.border == True:
                borderimg = "mods/eui/cg/thumbs/border.png"
            else:
                borderimg = None
            if self.replay == False:
                return self.gallery.make_button(self.name, self.thumb, locked="cg/thumbs/locked.jpg",hover_border="cg/thumbs/hover.png", idle_border=borderimg, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
            else:
                action = Replay(self.label, locked=False)
                for condition in self.conditions:
                    if not eval(condition):
                        action = None
                        break
                return Button(action=action, child=self.thumb, insensitive_child="CG/thumbs/locked.jpg",hover_foreground="mods/eui/cg/thumbs/replay_hover.png",idle_foreground=borderimg,hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

        def is_unlocked(self):
            for condition in self.conditions:
                if not eval(condition):
                    seen_all = False
                    break
            if self.replay == False:
                # I think this is right, haven't tested it yet
                for imageset in self.images:
                    seen_all = True
                    
                    if len(self.conditions + imageset.conditions) == 0:
                        for image in imageset.images:
                            if not renpy.seen_image(image):
                                seen_all = False
                                break
                    else:
                        for condition in imageset.conditions:
                            if not eval(condition):
                                seen_all = False
                                break
                    if seen_all == True:
                        return True
                return False
            else:
                # We shouldn't be defining conditions here for replays, but, whatever
                for condition in self.images[0].conditions:
                    if not eval(condition):
                        return False
                return True

    # Declare the Enhancement Mod UI variables that are not important to remember
    # Extend _object so we're not placed in the Ren'Py store.
    # Our variables will be remembered for the lifespan of the game window
    class EnhancementModCGGallery(_object):
        def __init__(self, gallery, prefixType):
            self.gallery = gallery
            self.prefix = prefixType
            self.cgs = []

        @property
        def next_name(self):
            return "{0}{1}".format(self.prefix, len(self.cgs) + 1)

        def add(self, thumb, images, parent=None, conditions=None, transforms=None, censor=False, border=False):
            cg = EnhancementModCGItem(self.prefix, self.gallery, self.next_name, thumb, images, parent=parent, conditions=conditions, transforms=transforms, censor=censor, border=border)
            self.cgs.append(cg)
            self.gallery.button(cg.name)
            for condition in cg.conditions:
                self.gallery.condition(condition)
            for image in cg.images:
                if len(cg.conditions + image.conditions) == 0:
                    self.gallery.unlock_image(*image.images)
                else:
                    self.gallery.image(*image.images)
                    for condition in image.conditions:
                        self.gallery.condition(condition)
                if len(cg.transforms + image.transforms) != 0:
                    self.gallery.transform(*(cg.transforms + image.transforms))

        def add_replay(self, thumb, label, parent=None, conditions=None, censor=False, border=False):
            cg = EnhancementModCGItem(self.prefix, self.gallery, self.next_name, thumb, label, parent=parent, conditions=conditions, censor=censor, replay=True, border=border)
            self.cgs.append(cg)

        def find(self, image):
            results = [cg for cg in self.cgs if cg.images[0].image == image]
            if len(results) > 0:
                return results[0]
            return None

        def is_unlocked(self, image):
            return self.find(image).is_unlocked()

        def getlist(self):
            global CENSOR
            cglist = []
            count = 0
            for cg in self.cgs:
                if CENSOR == False or cg.censor == False:
                    cglist.append(cg)
                    count += 1

            while len(cglist) < 3 or len(cglist) % 3 != 0:
                cglist.append(EnhancementModBlankItem())

            return cglist

    class EnhancementModMusicItem(_object):
        def __init__(self, musicroom, title, filename, parent=None, conditions=None):
            self.mr = musicroom
            self.title = title
            # Fix case sensitivity
            self.filename = filename
            self.file_upper = "Music/{0}.ogg".format(filename)
            self.file_lower = "music/{0}.ogg".format(filename)
            if isinstance(conditions, list):
                self.conditions = conditions
            elif conditions is None:
                self.conditions = []
            else:
                self.conditions = [ conditions ]

            # Fix case sensitivity
            if not parent is None:
                self.conditions += [ "eui.tracks.is_unlocked('{0}')".format(parent) ]

        @property
        def file(self):
            if self.mr.is_unlocked(self.file_upper):
                return self.file_upper
            else:
                return self.file_lower

        def make_button(self):
            action = self.mr.Play(self.file)
            for condition in self.conditions:
                if not eval(condition):
                    action = None
                    break
            return renpy.display.behavior.ImageButton(idle_image="UI/bonus_song_base.png",hover_image="UI/bonus_song_hover.png",action=action,insensitive_image="CG/thumbs/locked.jpg",selected_idle_image="UI/bonus_song_baseplay.png",selected_hover_image="UI/bonus_song_hoverplay.png",hover_sound="Sound/hover1.ogg",xpos=13,ypos=2)
        
        def is_unlocked(self):
            if len(self.conditions) == 0:
                return renpy.seen_audio(self.file)
            else:
                for condition in self.conditions:
                    if not eval(condition):
                        return False
                return True

        def make_text(self):
            if not self.is_unlocked():
                return Text("")
            return Text(self.title,ysize=10,color="#000000",font="Fonts/SourceCodePro-Regular.ttf",size=15,xalign=0.5,ypos=100,xpos=160,text_align=0.5,xmaxmimum=276)


    class EnhancementModMusicGallery(_object):
        def __init__(self, musicroom):
            self.mr = musicroom
            self.tracks = []

        def add(self, title, filename, parent=None, conditions=None):
            track = EnhancementModMusicItem(self.mr, title, filename, parent=parent, conditions=conditions)
            self.tracks.append(track)
            always_unlocked = len(track.conditions) != 0
            self.mr.add(track.file,always_unlocked=always_unlocked)

        def find(self, filename):
            results = [track for track in self.tracks if track.filename == filename]
            if len(results) > 0:
                return results[0]
            return None

        def is_unlocked(self, filename):
            return self.find(filename).is_unlocked()

        def getlist(self):
            tracklist = []
            count = 0
            for track in self.tracks:
                tracklist.append(track)
                count += 1

            while len(tracklist) < 3 or len(tracklist) % 3 != 0:
                tracklist.append(EnhancementModBlankItem())

            return tracklist
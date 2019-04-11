init -1 python:

    class EnhancementModBlankItem(_object):
        def make_button(self):
            return Text("")
        def make_text(self):
            return Text("")

        #@property
        #def has_extra(self):
        #    return False
        #def make_extra(self):
        #    return Text("")

    class EnhancementModCGItem(_object):
        def __init__(self, prefix, gallery, name, thumb, images, conditions=[], transforms=[], censor=False, replay=False, border=False):
            self.gallery = gallery
            self.name = name
            if isinstance(thumb, list):
                # A really stupid way of overriding the default thumb path
                self.thumb = thumb[0]
            else:
                self.thumb = "cg/thumbs/eui/{0}/{1}.jpg".format(prefix,thumb)
            self.border = border
            #self.thumb = "cg/thumbs/eui/{0}.jpg".format(thumb)
            if isinstance(images, list):
                self.images = images
            else:
                self.images = [ images ]

            if isinstance(conditions, list):
                self.conditions = conditions
            elif conditions is None:
                self.conditions = []
            else:
                self.conditions = [ conditions ]

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
                return self.images[0]

        def make_button(self):
            if self.border == True:
                borderimg = "cg/thumbs/eui/border.png"
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
                return Button(action=action, child=self.thumb, insensitive_child="CG/thumbs/locked.jpg",hover_foreground="cg/thumbs/eui/replay_hover.png",idle_foreground=borderimg,hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

        def is_unlocked(self):
            if replay == False and len(self.conditions) == 0:
                return renpy.seen_image(self.images[0])
            else:
                for condition in self.conditions:
                    if not eval(condition):
                        return False
                return True

        #@property
        #def has_extra(self):
        #    return thumb
        #def make_extra(self):
        #    return Text("")

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

        def add(self, thumb, images, conditions=[], transforms=[], censor=False, border=False):
            cg = EnhancementModCGItem(self.prefix, self.gallery, self.next_name, thumb, images, conditions=conditions, transforms=transforms, censor=censor, border=border)
            self.cgs.append(cg)
            self.gallery.button(cg.name)
            for image in cg.images:
                if len(cg.conditions) == 0:
                    self.gallery.unlock_image(image)
                else:
                    self.gallery.image(image)
            for condition in cg.conditions:
                self.gallery.condition(condition)
            if len(cg.transforms) != 0:
                self.gallery.transform(cg.transforms)

        def add_replay(self, thumb, label, conditions=[], censor=False, border=False):
            cg = EnhancementModCGItem(self.prefix, self.gallery, self.next_name, thumb, label, conditions=conditions, censor=censor, replay=True, border=border)
            self.cgs.append(cg)


        #def transform(self, *transforms):
        #    self.cgs[len(self.cgs) - 1].transforms = transforms
        #    self.gallery.transform(transforms)

        def find(self, image):
            results = [cg for cg in self.cgs if cg.images[0] == image]
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
        def __init__(self, musicroom, title, filename, conditions=[]):
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
            return EuiImageButton(idle_image="UI/bonus_song_base.png",hover_image="UI/bonus_song_hover.png",action=action,insensitive_image="CG/thumbs/locked.jpg",selected_idle_image="UI/bonus_song_baseplay.png",selected_hover_image="UI/bonus_song_hoverplay.png",hover_sound="Sound/hover1.ogg")
        
        def is_unlocked(self):
            if len(self.conditions) == 0:
                return renpy.seen_audio(self.file)
            else:
                for condition in self.conditions:
                    if not eval(condition):
                        return False
                return True

        def make_text(self):
            if not self.mr.is_unlocked(self.file):
                return Text("")
            return Text(self.title,ysize=10,color="#000000",font="Fonts/SourceCodePro-Regular.ttf",size=15,xalign=0.5,ypos=100,xpos=144,text_align=0.5,xmaxmimum=276)#ypos=100


    class EnhancementModMusicGallery(_object):
        def __init__(self, musicroom):
            self.mr = musicroom
            self.tracks = []

        def add(self, title, filename, conditions=[]):
            track = EnhancementModMusicItem(self.mr, title, filename, conditions=conditions)
            self.tracks.append(track)
            always_unlocked = len(conditions) != 0
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
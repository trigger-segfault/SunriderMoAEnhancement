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
        def __init__(self, prefix, gallery, name, thumb, images, censor=False, video=False, border=False):
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
            self.censor = censor
            self.video = video
            self.transforms = []

        @property
        def label(self):
            if self.video == True:
                return self.images[0]

        def make_button(self):
            if self.border == True:
                borderimg = "eui_thumb_border"#"cg/thumbs/eui/border.png"
            else:
                borderimg = None
            if self.video == False:
                return self.gallery.make_button(self.name, self.thumb, locked="cg/thumbs/locked.jpg",hover_border="cg/thumbs/hover.png", idle_border=borderimg, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
            else:
                return Button(action=Replay(self.label), child=self.thumb, insensitive_child="CG/thumbs/locked.jpg",hover_foreground="cg/thumbs/eui/replay_hover.png",foreground=borderimg,hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

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

        def add(self, thumb, images, censor=False, border=False):
            cg = EnhancementModCGItem(self.prefix, self.gallery, self.next_name, thumb, images, censor=censor, border=border)
            self.cgs.append(cg)
            self.gallery.button(cg.name)
            for image in cg.images:
                self.gallery.unlock_image(image)

        def add_video(self, thumb, label, censor=False, border=False):
            cg = EnhancementModCGItem(self.prefix, self.gallery, self.next_name, thumb, label, censor=censor, video=True, border=border)
            self.cgs.append(cg)


        def transform(self, *transforms):
            self.cgs[len(self.cgs) - 1].transforms = transforms
            self.gallery.transform(transforms)

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
        def __init__(self, musicroom, name, filename):
            self.mr = musicroom
            self.name = name
            # Fix case sensitivity
            self.filename_upper = "Music/{0}.ogg".format(filename)
            self.filename_lower = "music/{0}.ogg".format(filename)

        @property
        def filename(self):
            if self.mr.is_unlocked(self.filename_upper):
                return self.filename_upper
            else:
                return self.filename_lower

        def make_button(self):
            return EuiImageButton(idle_image="UI/bonus_song_base.png",hover_image="UI/bonus_song_hover.png",action=self.mr.Play(self.filename),insensitive_image="CG/thumbs/locked.jpg",selected_idle_image="UI/bonus_song_baseplay.png",selected_hover_image="UI/bonus_song_hoverplay.png",hover_sound="Sound/hover1.ogg")

        def make_text(self):
            if not self.mr.is_unlocked(self.filename):
                return Text("")
            return Text(self.name,ysize=10,color="#000000",font="Fonts/SourceCodePro-Regular.ttf",size=15,xalign=0.5,ypos=100,xpos=144,text_align=0.5,xmaxmimum=276)#ypos=100


    class EnhancementModMusicGallery(_object):
        def __init__(self, musicroom):
            self.mr = musicroom
            self.tracks = []

        def add(self, name, filename, always_unlocked=False):
            track = EnhancementModMusicItem(self.mr, name, filename)
            self.tracks.append(track)
            # Fix case sensitivity
            self.mr.add(track.filename,always_unlocked=always_unlocked)

        def getlist(self):
            tracklist = []
            count = 0
            for track in self.tracks:
                tracklist.append(track)
                count += 1

            while len(tracklist) < 3 or len(tracklist) % 3 != 0:
                tracklist.append(EnhancementModBlankItem())

            return tracklist
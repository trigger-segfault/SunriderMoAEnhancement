init python:
    # Needed for renpy.loadsave function overrides
    from cStringIO import StringIO
    from json import dumps as json_dumps

    # Declare the Enhancement Mod UI variables that are not important to remember
    # Extend _object so we're not placed in the Ren'Py store.
    # Our variables will be remembered for the lifespan of the game window
    class EnhancementModUI(_object):
      
        ### Important Variables

        # The version of this MoA Enhancement UI mod file
        @property
        def version(self):
            return 'v0.0.0.1' # Constant

#region ### Constructor

        # The current version of the MoA Enhancement class that you loaded the save from
        def __init__(self):

            self.show_charactercg = False
            self.show_mechacg = False
            self.show_backgrounds = False
            self.show_music = False
            self.show_chivos = False
            self.show_bonus = 0

            self.quicksave_slots = 12

            self.mr = MusicRoom(channel='music', fadeout=1.0, fadein=0.0, loop=True, single_track=True, shuffle=False, stop_action=None)
            self.gallery = Gallery()
            self.gallery.transition = dissolve
            self.gallery.navigation = True # Enable navbar

            self.chcg = EnhancementModCGGallery(self.gallery, "chcg")
            self.mccg = EnhancementModCGGallery(self.gallery, "mccg")
            self.bg = EnhancementModCGGallery(self.gallery, "bg")
            self.tracks = EnhancementModMusicGallery(self.mr)

            self.show_sidemenu = False
            self.option_show = 1
            self.tty = -5000
            #self.english_battle_voices = True
            self.httx = 0
            self.htty = -5000

            self.his_ceraflag = None
            self.his_professionalreunion = None
            self.his_loosenrule = None
            self.his_pactspire = None
            self.his_capturetraffickers = None
            self.his_diplomatssaved = None
            self.his_mochirescue = None
            self.his_claudesupport = None
            self.his_chigaraforgive = None
            self.his_solacareful = None
            self.his_noallianceregulations = None
            self.his_cafeteriaasaga = None
            self.his_notinterestedinfame = None
            self.his_beforefarportsuspectalliance = None
            self.his_techdangerous = None

            self.Optionsvars = ["his_ceraflag", "his_professionalreunion", "his_loosenrule", "his_pactspire", "his_diplomatssaved", "his_mochirescue", "his_claudesupport", "his_chigaraforgive", "his_solacareful", "his_noallianceregulations", "his_cafeteriaasaga", "his_notinterestedinfame", "his_beforefarportsuspectalliance", "his_techdangerous"]
            
            # Relivent functions in functions.rpy: 
            self.optionsypos = []
            self.optionsxpos = []
            self.Optionsfuncs = [self.validate_spire]
            self.setoptions = [
            [1,"Flag","After the fall of Cera, which flag did you suggest flying?","True"],
            [2,"Cera","You told Ava the Sunrider would always fly Cera's flag.","True",("his_ceraflag",True)],
            [2,"Pirate","You told Ava being a pirate ship wouldn't be bad.","True",("his_ceraflag",False)],
            
            [1,"Reunion with Ava","How did you treat Ava upon reuniting with her\nafter ten years?","True"],
            [2,"Professional","You were professional with Ava.","True",("his_professionalreunion",True)],
            [2,"Friendly","You told Ava that it'll be just like old times.","True",("his_professionalreunion",False)],
            
            [1,"Military discipline","Who did you support after meeting Asaga and Chigara\nat Tydaria?","True"],
            [2,"Relaxed rules","You loosened up the rules for Asaga.","True",("his_loosenrule",True)],
            [2,"Enforced discipline","You supported Ava's enforcement of military discipline.","True",("his_loosenrule",False)],
            
            [1,"First side job","Which first side job did you perform?","True"],
            [2,"PACT Spire","You attacked the PACT communication spire.","True",("his_pactspire",True)],
            [2,"Human traffickers","You stopped the human traffickers.","True",("his_pactspire",False)],
            
            [1,"Fate of the Traffickers","What did you do with the captured human traffickers?","his_pactspire == False"],
            [2,"Taken alive","You captured them and turned them over to the authorities.","his_pactspire == False",("his_capturetraffickers",True)],
            [2,"Killed","You left them to die slowly in space.","his_pactspire == False",("his_capturetraffickers",False)],
            
            [1,"Versta diplomats","What happened to the Alliance diplomats at Versta?","True"],
            [2,"Saved","You saved the diplomats.","True",("his_diplomatssaved",True)],
            [2,"Killed","The Agamemnon was sank and all lives onboard were lost.","True",("his_diplomatssaved",False)],
            
            [1,"Mochi rescue","What did you order during the mission to rescue the Mochi?","True"],
            [2,"Ryders forward","You sent your ryders ahead to rescue the Mochi.","True",("his_mochirescue",True)],
            [2,"Defend the Sunrider","You held your ryders back to protect the Sunrider.","True",("his_mochirescue",False)],
            
            [1,"Medical Malpractice","What did you do after you found out Claude was a fraud?","True"],
            [2,"Let Claude off","You let Claude off the hook.","True",("his_claudesupport",True)],
            [2,"Claude imprisoned","You put her in the brig.","True",("his_claudesupport",False)],
            
            [1,"Chigara's apology","Did you reprimand Chigara for hiding the fact that\nAsaga was the princess of Ryuvia?","True"],
            [2,"Forgave Chigara","You forgave Chigara because she was trying to protect Asaga.","True",("his_chigaraforgive",True)],
            [2,"Reprimanded Chigara","You reprimanded Chigara for endangering the ship.","True",("his_chigaraforgive",False)],
            
            [1,"Talking with Sola","When you spoke with Sola after Asaga was kidnapped, what did you say?","True"],
            [2,"Be careful","You told Sola to watch herself and not do\n anything dangerous.","True",("his_solacareful",True)],
            [2,"Give PACT hell","You told Sola to give PACT hell.","True",("his_solacareful",False)],
            
            [1,"Safety regulations","When Icari and Kryska got into a fight about the Phoenix's breach of safety regulations, who did you back?","True"],
            [2,"Sided with Icari","You sided with Icari and told Kryska that Alliance\nsafety regulations did not apply in the Neutral Rim.","True",("his_noallianceregulations",True)],
            [2,"Sided with Kryska","You sided with Kryska and told Icari to upgrade\nthe Phoenix to the Alliance's safety regulations.","True",("his_noallianceregulations",False)],
            
            [1,"Messhall talk","When Chigara was nervous after meeting Arcadius for the first time, who did you support?","True"],
            [2,"Sided with Asaga","You agreed with Asaga and told Chigara to be more brave.","True",("his_cafeteriaasaga",True)],
            [2,"Sided with Chigara","You sided with Chigara and told Asaga not everyone\nwas as macho as her.","True",("his_cafeteriaasaga",False)],
            
            [1,"Growing fame","When Icari talked about your growing fame, what did you say you wanted?","True"],
            [2,"Not Interested","You said you weren't interested in becoming famous.","True",("his_notinterestedinfame",True)],
            [2,"Rally against PACT","You said you would use your fame to rally\nthe galaxy against PACT.","True",("his_notinterestedinfame",False)],
            
            [1,"The Alliance","Before the Battle of Far Port, what stance did you take with the Alliance?","True"],
            [2,"Distrust","You suspected the Alliance.","True",("his_beforefarportsuspectalliance",True)],
            [2,"Trust","You trusted the Alliance.","True",("his_beforefarportsuspectalliance",False)],
            
            [1,"Paradox Project","When you discussed the Paradox Project with Chigara over tea, what did you say?","True"],
            [2,"Dangerous","You said such technology could be dangerous if misused.","True",("his_techdangerous",True)],
            [2,"Useful","You said such technology could be useful now.","True",("his_techdangerous",False)],
                        ]
            self.optpoint = 0

            self.setoptions_ypos(self.setoptions)

            ## Comment these out if you don't want to overwrite Ren'Py functionality

            # Fixes only panning between locked images instead of unlocked images and vice-versa
            self.gallery.show = self.gallery_show

            # This fixes autosave cycling and cycling for quicksaves
            renpy.loadsave.cycle_saves = self.cycle_saves
            renpy.loadsave.autosave_thread = self.autosave_thread

#endregion

#region ### Gallery Screen Helpers

        # def toggle_afm(self):
        #    _preferences.afm_enable = not _preferences.afm_enable
        #    renpy.restart_interaction()

        def start_afm(self):
           _preferences.afm_enable = True
           renpy.restart_interaction()

        def stop_afm(self):
           _preferences.afm_enable = False
           renpy.restart_interaction()

        def gallery_rows(self, list):
            return max(int((len(list) + 2) / 3), 1)

        # Fix all_images being swapped with unlocked_images, now you can see if some images are locked
        def gallery_show(self, button=0, image=0):
            """
            Starts showing gallery images.

            `button`
                The index of the button to start showing.
            """

            # A list of (button, image) index pairs for all of the images we know
            # about.
            all_images = [ ]

            # A list of (button, image) index pairs for all of the unlocked
            # images.
            unlocked_images = [ ]

            for bi, b in enumerate(self.gallery.button_list):

                all_unlocked = True

                for ii, i in enumerate(b.images):

                    all_images.append((bi, ii))

                    unlocked = i.check_unlock(all_unlocked)

                    if unlocked:
                        unlocked_images.append((bi, ii))
                    else:
                        all_unlocked = False

            self.gallery.slideshow = False

            # Loop, displaying the images.
            while True:

                b = self.gallery.button_list[button]
                i = b.images[image]

                result = i.show((button, image) not in unlocked_images, image, len(b.images))

                # Default action for click.

                if result is True:
                    result = "next"

                if result == 'return':
                    break

                # At this point, result is either 'next', "next_unlocked", "previous", or "previous_unlocked"
                # Go through the common advance code.

                if self.gallery.locked and result.endswith("_unlocked"):
                    images = unlocked_images
                else:
                    images = all_images

                if (button, image) in images:
                    index = images.index((button, image))
                else:
                    index = -1

                if result.startswith('previous'):
                    index -= 1
                else:
                    index += 1

                if index < 0 or index >= len(images):
                    break

                new_button, new_image = images[index]

                if not self.gallery.span_buttons:
                    if new_button != button:
                        break

                button = new_button
                image = new_image

            renpy.transition(self.gallery.transition)

#endregion

#region ### File Screen Helpers

        # Thank you Python, for allowing me to overwrite everyone's hard work so I can fix shit

        # This is designed to fix autosave cycling empty save slots.
        # The original cycle_saves sometimes results in slot gaps between autosaves for no good reason.
        def cycle_saves(self, name, count):
            """
            :doc: loadsave

            Rotates the first `count` saves beginning with `name`.

            For example, if the name is auto- and the count is 10, then
            auto-9 will be renamed to auto-10, auto-8 will be renamed to auto-9,
            and so on until auto-1 is renamed to auto-2.
            """

            # Hack to fix Ren'Py's hardcoded 10-slot cycle
            if count == 10:
                if name == "quick-":
                    count = self.quicksave_slots
                elif name == "auto-":
                    count = config.autosave_slots

            # A simple fix to prevent saves from being pushed when there's no need to push
            for i in range(1, count):
                if not renpy.loadsave.can_load(name + str(i)):
                    count = i
                    break

            for i in range(count - 1, 0, -1):
                renpy.loadsave.rename_save(name + str(i), name + str(i + 1))

        # This is the same as renpy.loadsave.save, except we also cycle saves here
        def save_and_cycle(self, slotname, extra_info='', mutate_flag=False):
            """
            :doc: loadsave
            :args: (filename, extra_info='')

            Saves the game state to a save slot.

            `filename`
                A string giving the name of a save slot. Despite the variable name,
                this corresponds only loosely to filenames.

            `extra_info`
                An additional string that should be saved to the save file. Usually,
                this is the value of :var:`save_name`.

            :func:`renpy.take_screenshot` should be called before this function.
            """

            if mutate_flag:
                renpy.python.mutate_flag = False

            roots = renpy.game.log.freeze(None)

            if renpy.config.save_dump:
                renpy.loadsave.save_dump(roots, renpy.game.log)

            logf = StringIO()
            renpy.loadsave.dump((roots, renpy.game.log), logf)

            if mutate_flag and renpy.python.mutate_flag:
                raise renpy.loadsave.SaveAbort()

            screenshot = renpy.game.interface.get_screenshot()

            json = { "_save_name" : extra_info }

            for i in renpy.config.save_json_callbacks:
                i(json)

            json = json_dumps(json)

            # We'll put the cycle here, that way we don't push the saves 
            # and then end up with a failed save and blank space.
            try:
                dash_index = slotname.index("-")
                cycle_name = slotname[:dash_index+1]
                if cycle_name == "auto-":
                    self.cycle_saves(cycle_name, renpy.config.autosave_slots)
                elif cycle_name == "quick-":
                    self.cycle_saves(cycle_name, self.quicksave_slots)
                else:
                    # Might as well use the hardcoded 10 here because we
                    # have no precedent for setting normal save slot count.
                    self.cycle_saves(cycle_name, 10)
            except:
                pass

            sr = renpy.loadsave.SaveRecord(screenshot, extra_info, json, logf.getvalue())
            renpy.loadsave.location.save(slotname, sr)

            renpy.loadsave.location.scan()
            renpy.loadsave.clear_slot(slotname)

        # Change when cycle_saves is called so that we don't
        # needlessly cycle and end up with empty slots.
        def autosave_thread(self, take_screenshot):

            try:

                try:
                    # Uh uh uh, we're doing this in eui.save_and_cycle
                    #self.cycle_saves("auto-", renpy.config.autosave_slots)

                    if renpy.config.auto_save_extra_info:
                        extra_info = renpy.config.auto_save_extra_info()
                    else:
                        extra_info = ""

                    if take_screenshot:
                        renpy.exports.take_screenshot(background=True)

                    self.save_and_cycle("auto-1", mutate_flag=True, extra_info=extra_info)
                    renpy.loadsave.autosave_counter = 0

                except:
                    pass

            finally:
                renpy.loadsave.autosave_not_running.set()

        # Becuase file pages were normally 8 per page but we use 12 per page,
        # We need to keep the original page number when looking up saves.

        @property
        def MOA_FILE_COUNT(self):
            return 8
        @property
        def EUI_FILE_COUNT(self):
            return 12

        def file_page(self,i):
            if self.is_file_page():
                return (i - 1) / self.MOA_FILE_COUNT + 1
            else:
                return self.file_page_name()
        def file_page_number(self):
            try:
                return int(FilePageName());
            except:
                pass
                #return 1
        def file_page_name(self):
            if FilePageName() == 'None':
                return 1
            else:
                return FilePageName("auto", "quick")
        def file_slot(self,i):
            if self.is_file_page():
                return (i - 1) % self.MOA_FILE_COUNT + 1
            else:
                return i
        def file_name_slot(self,i):
            if self.is_file_page():
                return (i - 1) % self.EUI_FILE_COUNT + 1
            else:
                return i
        def file_range(self):
            try:
                start = (int(FilePageName()) - 1) * self.EUI_FILE_COUNT + 1;
            except:
                start = 1
            return range(start, start + self.EUI_FILE_COUNT)
        def is_file_page(self):
            try:
                int(FilePageName());
                return True
            except:
                return False

#endregion

#region ### History Screen Functions

        # Functions used by the history screen, from Liberation Day

        def validate_spire(self):
            #global his_pactspire, his_capturetraffickers
            Confirm = True
            if self.his_pactspire == False and self.his_capturetraffickers == None:
                Confirm = False
            return Confirm
            
        def show_confirm(self):
            Confirm = True
            if self.Optionsvars != []:
                for item in self.Optionsvars:
                    if self.his_eval(item) == None:
                        Confirm = False
            if self.Optionsfuncs != []:
                for item in self.Optionsfuncs:
                    if item() == False:
                        Confirm = False
            return Confirm

        def options_insert(self,point,insert_list):
            global setoptions
            note = 0 #Failsafe, if no match it goes to the top
            #Find the point in the setoptions list
            for item in self.setoptions:
                if item[1] == point:
                    note = self.setoptions.index(item)
            setoptions_hold = self.setoptions[note:]
            self.setoptions = self.setoptions[:note]
            for piece in insert_list:
                self.setoptions.append(piece)
            for piece in setoptions_hold:
                self.setoptions.append(piece)
            return
            
        def setoptions_ypos(self,list):
            #global optionsypos, optionsxpos, optpoint
            OptDepth = 0
            StoreHoldingNumber = 1
            HoldingNumber = 0
            self.optionsypos = []
            self.optionsxpos = []
            for item in list[:]:
                try:
                    if item[0] == 1:
                        HoldingNumber += 1
                        if HoldingNumber > StoreHoldingNumber:
                            OptDepth += 1
                            StoreHoldingNumber += 1
                        HoldingCount = 0
                        self.optionsypos.append(10+(OptDepth*40))
                        self.optionsxpos.append(10)
                        
                    if item[0] == 2:
                        if HoldingCount == 2:
                            HoldingCount = 0
                            OptDepth += 1
                        self.optionsypos.append(10+(OptDepth*40))
                        if HoldingCount == 0: self.optionsxpos.append(430)
                        if HoldingCount == 1: self.optionsxpos.append(740)
                        HoldingCount += 1 # If there are more than 2 options, start a new line for the next ones, repeat every 2 options
                except:
                    pass
            for item in list:
                if item[0] == 2:
                    self.optpoint += 1
            self.optpoint /= 2
        
        def his_eval(self,item):
            return eval(item.replace('his_', 'eui.his_'))

#endregion

#region ### Quick Menu Screen Helpers

        # Makes sure the quick menu is visible and hidden at the right times
        def manage_quick_menu_visibility(self, label):
            # Make sure the quick menu is active when we start a campaign or addon
            if label == 'initialize':
                renpy.show_screen('quick_menu')

            # Make sure the quick menu is shown after loading a game before Enhanced UI was added
            if label == "after_load":
                # The only time we don't show the quick menu is in the stores, hide it if we're in these screens
                if renpy.get_screen("upgrade") or renpy.get_screen("store_union"):
                    renpy.hide_screen('quick_menu')
                elif not renpy.get_screen("quick_menu"):
                    renpy.show_screen('quick_menu')

            # The only time we don't show the quick menu is in the stores, hide it when we get to this label
            if label == "allocatefunds" or label == "unionstore":
                renpy.hide_screen('quick_menu')

            # This is called when returning from either store, make sure to show the quick menu again
            if label == 'dispatch' and not renpy.get_screen("quick_menu"):
                renpy.show_screen('quick_menu')
#endregion
    
    eui = EnhancementModUI()
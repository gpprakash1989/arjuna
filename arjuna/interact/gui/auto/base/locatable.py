
class Locatable:

    def __init__(self, gui, emd):
        # super().__init__(automator.config) #, obj_name)
        self.__gui = gui
        self.__automator = gui.automator
        self.__lmd = emd
        self.__located = False
        self.__located_by = None 

        # self.__parent = parent

    @property
    def gui(self):
        return self.__gui
        
    @property
    def automator(self):
        return self.__automator

    @property
    def lmd(self):
        return self.__lmd

    @property
    def located(self):
        return self.__located

    @property
    def located_with(self):
        return self.__located_by

    @located_with.setter
    def located_with(self, locator_tuple):
        self.__located = True
        self.__located_by = locator_tuple


'''
From Base Element
    def __init__(self, automator, emd):
        self.__dispatcher_element = None



    # @property
    # def parent_container(self):
    #     if self.__parent is not None:
    #         return self.__parent
    #     else:
    #         return self.__automator

    def _create_element_flat_or_nested(self, locator_meta_data):
        from arjuna.interact.gui.auto.element.guielement import GuiElement
        return GuiElement(self.__automator, locator_meta_data, parent=self) 

    def _create_multielement_flat_or_nested(self, locator_meta_data):
        from arjuna.interact.gui.auto.element.multielement import GuiMultiElement
        return GuiMultiElement(self.__automator, locator_meta_data, parent=self) 

    def create_dispatcher(self):
        self._set_dispatcher(self.dispatcher_creator.create_gui_element_dispatcher(self.__automator.dispatcher, self.setu_id))

'''
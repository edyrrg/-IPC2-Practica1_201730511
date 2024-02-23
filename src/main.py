from controllers.lector_xml_file import lector_xml_file as lector_xml
from gui.gui import GUI


def init():
    lector_ui = lector_xml('./gui/gui_models/ui_menu.xml')
    view = GUI(lector_ui)
    view.init_core_ui()


if __name__ == '__main__':
    init()

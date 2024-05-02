from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Link import GDT_Link


class module_contact(GDO_Module):

    def gdo_init_sidebar(self, page):
        page._bottom_bar.add_field(GDT_Link().href(self.href('form')).text('module_contact'))


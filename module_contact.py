from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.base.Util import module_enabled
from gdo.contact.GDO_ContactMessage import GDO_ContactMessage
from gdo.core.GDT_Bool import GDT_Bool
from gdo.ui.GDT_Link import GDT_Link


class module_contact(GDO_Module):

    def gdo_classes(self):
        return [
            GDO_ContactMessage,
        ]

    def gdo_friendencies(self) -> list:
        return [
            'captcha',
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Bool('contact_captcha').initial('1'),
        ]

    def cfg_captcha(self) -> bool:
        return self.get_config_value('contact_captcha') and module_enabled('captcha')

    async def gdo_init_sidebar(self, page):
        page._bottom_bar.add_field(GDT_Link().href(self.href('form')).text('module_contact'))


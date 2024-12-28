from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.date.GDT_Created import GDT_Created
from gdo.mail.GDT_Email import GDT_Email
from gdo.message.GDT_Message import GDT_Message


class GDO_ContactMessage(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('cm_id'),
            GDT_Email('cm_from').not_null(),
            GDT_Message('cm_message').not_null(),
            GDT_Created('cm_created'),
            GDT_Creator('cm_creator'),
        ]

from gdo.base.Trans import t
from gdo.base.Util import Arrays, dump
from gdo.captcha.GDT_Captcha import GDT_Captcha
from gdo.contact.method.form import form
from gdo.contact.module_contact import module_contact
from gdo.contact.GDO_ContactMessage import GDO_ContactMessage
from gdo.core.Connector import Connector
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.mail.GDT_Email import GDT_Email
from gdo.mail.Mail import Mail
from gdo.message.GDT_Message import GDT_Message
from gdo.user.GDT_ProfileLink import GDT_ProfileLink


class feedback(MethodForm):

    def gdo_connectors(self) -> str:
        return Connector.text_connectors()

    @classmethod
    def gdo_trigger(cls) -> str:
        return "feedback"

    def gdo_create_form(self, form: GDT_Form) -> None:
        email = GDT_Email('email')
        if self._env_user.is_user():
            email.initial(self._env_user.get_setting_val('email'))
        form.add_fields(
            email,
            GDT_RestOfText('message').not_null(),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        method = form().env_copy(self).args_copy(self)
        return method.execute()

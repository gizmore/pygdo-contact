from gdo.base.Trans import t
from gdo.base.Util import Arrays, dump
from gdo.captcha.GDT_Captcha import GDT_Captcha
from gdo.contact.module_contact import module_contact
from gdo.contact.GDO_ContactMessage import GDO_ContactMessage
from gdo.core.GDO_User import GDO_User
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.mail.GDT_Email import GDT_Email
from gdo.mail.Mail import Mail
from gdo.ui.GDT_Message import GDT_Message
from gdo.user.GDT_ProfileLink import GDT_ProfileLink


class form(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        staff = []
        for user in GDO_User.staff():
            staff.append(GDT_ProfileLink().user(user).with_username().with_avatar().render())
        form.text('info_contact_form', [Arrays.human_join(staff)])
        email = GDT_Email('email')
        if self._env_user.is_user():
            email.initial(self._env_user.get_setting_val('email'))
        form.add_field(
            email,
            GDT_Message('message').not_null(),
        )
        if module_contact.instance().cfg_captcha():
            form.add_field(GDT_Captcha())
        super().gdo_create_form(form)

    def form_submitted(self):
        email = self.param_value('email')
        message = self.param_val('message')

        GDO_ContactMessage.blank({
            'cm_from': email,
            'cm_message': message,
        }).insert()

        self.send_mails(email, message)

        return self.msg('msg_contact_sent')

    def send_mails(self, email: str, message: str):
        for user in GDO_User.staff():
            self.send_mail(user, email, message)

    def send_mail(self, user: GDO_User, email: str, message: str):
        mail = Mail.from_bot()
        mail.subject(t('mails_contact'))
        mail.body(t('mailb_contact', [
            user.render_name(),
            email,
            message,
        ]))
        mail.send_to_user(user)

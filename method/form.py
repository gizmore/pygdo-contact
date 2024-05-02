from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm


class form(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.text('info_contact_form')

        super().gdo_create_form(form)

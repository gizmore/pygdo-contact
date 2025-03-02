import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled
from gdo.core.GDO_Session import GDO_Session
from gdotest.TestUtil import web_plug, reinstall_module, web_gizmore, install_module, GDOTestCase, WebPlug


class ContactTest(GDOTestCase):

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        install_module('mail')
        install_module('contact')
        loader.load_modules_db()
        loader.init_modules(True, True)
        Application.init_cli()

    def test_00_install(self):
        reinstall_module('contact')
        self.assertTrue(module_enabled('contact'), 'cannot install contact')

    def test_01_form_rendering(self):
        Application.set_session(GDO_Session.for_user(web_gizmore()))
        out = web_plug('contact.form.html').exec()
        self.assertIn('gizmore', out, 'Staff link not shown on contact form.')

    def test_02_contact(self):
        Application.set_session(GDO_Session.for_user(web_gizmore()))
        out = WebPlug('contact.form.html').user('gizmore').post({'message': "test", 'submit': 1}).exec()
        self.assertIn('gizmore', out, 'Staff link not shown on contact form.')


if __name__ == '__main__':
    unittest.main()

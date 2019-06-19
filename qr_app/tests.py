from django.test import RequestFactory,TestCase
from .models import WeblinkModel, SmsModel, WifiModel, generate
from .views import weblink, sms, wifi, index
# Create your tests here.
# coverage run manage.py test
# coverage report -m

class SimpleTest(TestCase):

    def setUp(self):
         
        self.factory = RequestFactory()
        self._weblink = WeblinkModel()
        self._weblink.create("google.dk")

        self._wifi = WifiModel()
        self._wifi.create("keawifi", "WPA2", "1234")

        self._sms = SmsModel()
        self._sms.create("12124562", "hej kasperlololo")

        

    def test_gen(self):
        self.assertTrue("1234", generate("1234"))

    def test_wifi_model(self):
        self.assertTrue(isinstance(self._wifi, WifiModel))


    def test_sms_model(self):
       self.assertTrue(isinstance(self._weblink, WeblinkModel))



    def test_weblink_model(self):
       self.assertTrue(isinstance(self._weblink, WeblinkModel))
       
    def test_weblink_view(self):
        request = self.factory.get('/weblink')
        response = weblink(request)
        self.assertEqual(response.status_code, 200)

    def test_wifi_view(self):
        request = self.factory.get('/wifi')
        response = wifi(request)
        self.assertEqual(response.status_code, 200)

    def test_sms_view(self):
        request = self.factory.get('/sms')
        response = sms(request)
        self.assertEqual(response.status_code, 200)

    

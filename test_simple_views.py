from django.test import TestCase


class SimpleViewsTests(TestCase):
    def test_hello(self):
        url = "/hello/udi/"
        resp = self.client.get(url)
        self.assertContains(resp, "hello <b>udi</b> Your lucky number is 22!")
        # self.assertEquals(resp.content, "sadsad")

    def test_bad_url(self):
        url = "/kuku/324234/"
        resp = self.client.get(url)

        self.assertEquals(resp.status_code, 404)

    def test_add_json(self):
        x, y = 52, 16
        url = "/add/{}/{}/json/".format(x, y)
        resp = self.client.get(url)
        self.assertJSONEqual(resp.content, {"result": x + y})

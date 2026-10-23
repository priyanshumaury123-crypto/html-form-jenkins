import unittest
from html.parser import HTMLParser


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.inputs = {}
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if tag == "input":
            name = attrs.get("name")
            if name:
                self.inputs[name] = attrs

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("index.html", encoding="utf-8") as file:
            html = file.read()

        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form_exists(self):
        self.assertTrue(self.parser.form_found)

    def test_required_fields_exist(self):
        for field in ["name", "email", "contact"]:
            with self.subTest(field=field):
                self.assertIn(field, self.parser.inputs)
                self.assertIn("required", self.parser.inputs[field])

    def test_submit_button_exists(self):
        self.assertTrue(self.parser.submit_found)


if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest
from main import ServiceFunnel


class TestServiceFunnelScrape(unittest.TestCase):
    def setUp(self):
        self.service_funnel = ServiceFunnel()
        html_string = """
            <article class="article " id="id-39334" data-tags="A,B,C"><h2>S1</h2></article>
            <article class="article " id="id-39335" data-tags="B,C,D,E"><h2>S2</h2></article>
        """
        self.service_funnel.scrape_html(html_string)

    def test_valid_tags_with_snippet(self):
        result = self.service_funnel.handle_request(
            {"selected_tags": [{"name": "A"}, {"name": "B"}, {"name": "C"}]}
        )
        self.assertEqual(result["status"]["code"], 0)
        self.assertEqual(result["status"]["msg"], "Valid tags with snippet")
        self.assertEqual(
            result["selected_tags"],
            [{"name": "A"}, {"name": "B"}, {"name": "C"}],
        )
        self.assertCountEqual(result["next_tags"], [])
        self.assertEqual(
            result["snippet"],
            '<article class="article" data-tags="A,B,C" id="id-39334"><h2>S1</h2></article>',
        )

    def test_valid_tags_without_snippet(self):
        result = self.service_funnel.handle_request(
            {"selected_tags": [{"name": "B"}]}
        )
        self.assertEqual(result["status"]["code"], 1)
        self.assertEqual(result["status"]["msg"], "Valid tags but no snippet")
        self.assertEqual(result["selected_tags"], [{"name": "B"}])
        self.assertCountEqual(
            result["next_tags"],
            [{"name": "A"}, {"name": "C"}, {"name": "D"}, {"name": "E"}],
        )
        self.assertEqual(result["snippet"], None)

    def test_invalid_tags(self):
        result = self.service_funnel.handle_request(
            {"selected_tags": [{"name": "A"}, {"name": "E"}]}
        )
        self.assertEqual(result["status"]["code"], 2)
        self.assertEqual(result["status"]["msg"], "Invalid tags")
        self.assertEqual(
            result["selected_tags"], [{"name": "A"}, {"name": "E"}]
        )
        self.assertCountEqual(result["next_tags"], [])
        self.assertEqual(result["snippet"], None)


if __name__ == "__main__":
    unittest.main()

import argparse
from typing import List, Optional
from bs4 import BeautifulSoup


class ServiceFunnel:
    def __init__(self) -> None:
        self._all_tags = set()
        self._index = dict()
        self._articles = dict()
        self._selected_tags = set()

    def get_article(self, index_id):
        return self._articles.get(index_id, None)

    @staticmethod
    def get_tags(article: BeautifulSoup) -> List[Optional[str]]:
        """
        Get tags from an article.

        Args:
            article (str) : Part of .
        """
        article_tags = (
            article.get("data-tags").split(",") if article.get("data-tags") else []
        )
        article_tags = map(str.strip, article_tags)
        return [_ for _ in article_tags]

    def get_next_tags(self):
        return [{"name": tag} for tag in sorted(self._all_tags - self._selected_tags)]

    def get_selected_tags(self):
        return [{"name": tag} for tag in sorted(self._selected_tags)]

    @staticmethod
    def response_status_msg(status_code: int) -> str:
        """
        Defines response status message based on the number of articles.

        Args:
            status_code (int): Status code based on the number of articles.
        Returns:
            status (int): Response status description message.
        """
        messages = {
            0: "Valid tags with snippet",
            1: "Valid tags but no snippet",
            2: "Invalid tags",
        }

        return messages.get(status_code, "Invalid tags")

    @staticmethod
    def response_status(number_of_articles: int) -> int:
        """
        Defines response status based on the number of articles.

        Status 0 if the user needs to select more tags to see a snippet;
        Status 1 if the tag combination exists and has a snippet;
        Status 2 if invalid combo of tags - user needs to go back by removing one or more tags

        Args:
            number_of_articles (int): Request object as specified in the readme.
        Returns:
            status (int): Response object as specified in the readme.
        """
        if number_of_articles == 0:
            return 2
        elif number_of_articles == 1:
            return 0

        return 1

    def scrape_html(self, html: str) -> None:
        """
        Scrape HTML, extract tags and snippet and store them in an appropriate data structure.

        Args:
            html (str) : Entire HTML content. Not the path to HTML document.
        """
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            article_id = article.get("id")
            article_tags = self.get_tags(article=article)

            # extend index
            self._index.setdefault(article_id, set(article_tags))

            # extend articles
            self._articles.setdefault(article_id, str(article))

            # extend tags
            self._all_tags.update(article_tags)

    def handle_request(self, request: dict) -> dict:
        """
        Find out the correct snippet that maps to a set of input tags.

        Args:
            request (dict): Request object as specified in the readme.
        Returns:
            response (dict): Response object as specified in the readme.
        """
        self._selected_tags = set([_.get("name") for _ in request.get("selected_tags")])

        # count how many articles we've got
        count_of_articles = 0
        index_id = None

        for index_item in self._index:
            if self._selected_tags.issubset(self._index[index_item]):
                index_id = index_item
                count_of_articles += 1

        response_status_code = self.response_status(count_of_articles)
        response_status_msg = self.response_status_msg(response_status_code)

        return {
            "snippet": self.get_article(index_id=index_id)
            if response_status_code == 0
            else None,
            "next_tags": self.get_next_tags() if response_status_code == 1 else [],
            "status": {"msg": response_status_msg, "code": response_status_code},
            "selected_tags": self.get_selected_tags(),
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--html_path",
        help="path leading to the html file",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    with open(args.html_path, "r") as f:
        html_str = f.read()
    service_funnel = ServiceFunnel()
    service_funnel.scrape_html(html_str)

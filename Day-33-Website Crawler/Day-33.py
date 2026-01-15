# Day 33 - Website Crawler
# Focus: Depth-First Search (DFS)
# Language: Python 3


class WebsiteCrawler:
    def __init__(self):
        self.web_graph = {}

    def add_page(self, page):
        if page not in self.web_graph:
            self.web_graph[page] = []

    def add_link(self, from_page, to_page):
        self.add_page(from_page)
        self.add_page(to_page)
        self.web_graph[from_page].append(to_page)

    def crawl(self, start_page):
        visited = set()
        crawl_order = []

        def dfs(page):
            if page in visited:
                return
            visited.add(page)
            crawl_order.append(page)

            for link in self.web_graph.get(page, []):
                dfs(link)

        dfs(start_page)
        return crawl_order


def main():
    crawler = WebsiteCrawler()

    crawler.add_link("home", "about")
    crawler.add_link("home", "products")
    crawler.add_link("products", "product1")
    crawler.add_link("products", "product2")
    crawler.add_link("about", "contact")

    result = crawler.crawl("home")

    print("\nWebsite Crawl Order:")
    for page in result:
        print(page)


if __name__ == "__main__":
    main()

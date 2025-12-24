# Day 11 - Browser History Manager
# Focus: Stack
# Language: Python 3


class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self):
        if not self.back_stack:
            print("No back history.")
            return self.current

        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if not self.forward_stack:
            print("No forward history.")
            return self.current

        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        return self.current

    def show(self):
        print("\nCurrent Page:", self.current)
        print("Back Stack:", self.back_stack)
        print("Forward Stack:", self.forward_stack)


def main():
    browser = BrowserHistory("google.com")

    browser.visit("github.com")
    browser.visit("leetcode.com")
    browser.visit("linkedin.com")

    browser.show()

    print("\nBack:", browser.back())
    print("Back:", browser.back())

    browser.show()

    print("\nForward:", browser.forward())
    browser.show()


if __name__ == "__main__":
    main()

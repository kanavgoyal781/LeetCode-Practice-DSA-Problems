class node:
    def __init__(self, url:str):
        self.prev=None
        self.next=None
        self.url=url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current=node(homepage)

    def visit(self, url: str) -> None:
        self.current.next=node(url)
        self.current.next.prev=self.current
        self.current=self.current.next
        

    def back(self, steps: int) -> str:
        while self.current.prev and steps>0:
            self.current=self.current.prev
            steps=steps-1
        return self.current.url

    def forward(self, steps: int) -> str:
        while self.current.next and steps>0:
            self.current=self.current.next
            steps=steps-1
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
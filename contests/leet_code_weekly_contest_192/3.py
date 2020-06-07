from typing import *
from collections import *

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [homepage]
        self.curr_page = 0

    def visit(self, url: str) -> None:
        if self.curr_page != len(self.history) - 1:
            self.history = self.history[:self.curr_page + 1]

        self.history += url,
        self.curr_page += 1

    def back(self, steps: int) -> str:
        if self.curr_page >= steps:
            self.curr_page -= steps
            return self.history[self.curr_page]
        else:
            self.curr_page = 0
            return self.history[0]

    def forward(self, steps: int) -> str:
        if len(self.history) - (self.curr_page + 1) >= steps:
            self.curr_page += steps
            return self.history[self.curr_page]
        else:
            self.curr_page = len(self.history) - 1
            return self.history[-1]



browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com")
#;       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")
#;     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")
#;      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1)
#;                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1)
#;                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1)
#;                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")
#;     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2)
#;                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2)
#;                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7)
#;                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

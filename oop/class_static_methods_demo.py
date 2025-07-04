class book:
    def __init__(self,title, author, year):
        self.title = title 
        self.author = author
        self.year = year
        
    def __del__(self):
        return f"deleting {self.title}"
    
    def __str__(self):
        return f"{self.title} by {self.author} published in {self.year}"
    
    def __repr__(self):
        return f"book:({self.title}) author:({self.author}) year({self.year})"
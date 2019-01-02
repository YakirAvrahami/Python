class Cookie:
    def __init__ (self,gloten,eggs,sugar,flour):
        self.gloten=gloten
        self.eggs=eggs
        self.sugar=sugar
        self.flour=flour

    def print_cookie (self):
        return "  gloten: "+ str(self.gloten)+"\n  eggs: "+str(self.eggs)+"\n  sugar: "+str(self.sugar)+"\n  flour: "+str(self.flour)

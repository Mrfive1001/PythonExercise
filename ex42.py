class TheThing(object):
    count = 0

    def __init__(self):
        self.number = 0
        self.count += 1
        TheThing.count += 1

    def some_function(self):
        print "I got called."

    def add_me_up(self,more):
        self.number += more
        return self.number

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.count

print TheThing.count

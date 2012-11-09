from collections import defaultdict

def attrdict(*args, **kw):
    return DefDict(attrdict, *args, **kw)


class DefDict(defaultdict):

    def __setattr__(self, name, value):
        self[name] = value
    
    def __getattr__(self, name):
        return self[name]

    def __repr__(self):
        def _dicts(d):
            if getattr(d,"iteritems",None):
                return {k: _dicts(v) for k,v in d.iteritems()}
            else:
                return d
        return str(_dicts(self))


if __name__ == "__main__":

    #normal usage
    cntr = defaultdict(int)
    cntr["book_1"] = 12
    cntr["book_2"] = 111

    print cntr

    d = attrdict()
    d.name = "Brave"
    d.last_name = "Heart"

    print d

    d.friends.best = "Linux"
    print d
    
    if d.enemies.worst:
        print "The enemy is :",d.enemies.worst


    #The problem ?
    print "Problem : ",d



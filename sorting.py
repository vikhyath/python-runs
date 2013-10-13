
import operator

#example to demonstrate itemgetter

dict = {'c': 1, 'b': 4, 'd': -5}
#newdict = sorted(dict.iteritems(), key=operator.itemgetter(1, 0))
newdict = sorted(dict.iteritems(), key=lambda x: (x[1]))
print newdict

values = operator.itemgetter(1)
newdict = sorted(dict.iteritems(), key=values)
print newdict

#sort by value of list
list = [(1,2), (3,5), (9, -10)]
newlist = sorted(list, key=lambda (x,y): (y,x))
print newlist

#sort by key of list
newlist = sorted(list, key=lambda x: x)
print newlist


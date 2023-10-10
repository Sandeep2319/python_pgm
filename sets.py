set1 = {1,2,3,4}
set2 = { (2,3,4,5),frozenset({"sandeep","narvade"}) }


print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.discard(3))
print(set1.update(set2))
print(set1.add(6))
print(set1.remove(6))
print(set1.isdisjoint(set2))
print(set2)

print (set1)
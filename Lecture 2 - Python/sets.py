# Set of names
s = set()

# Adding names to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4) 
s.add(1)  # Duplicate, will be ignored 

s.remove(2)
print(s)    

print(f"The set has {len(s)} elements")
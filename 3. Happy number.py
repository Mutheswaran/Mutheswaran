def happynum(n):
  present=set()
  while n!=1:
        n= sum(int(i)**2 for i in str(n))
        if n in present:
            return False
        present.add(n)
  return True
print(happynum(7))
print(happynum(834))
print(happynum(6))

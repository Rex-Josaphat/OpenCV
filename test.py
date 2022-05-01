a = []
T = int(input())
for i in range(T):
    b = input()
    b = b.split()
    a.append(int(b))

# Test cases
for i in a:
  c = []
  c.append(i[0]**2)
  d = i[0]*i[1]
  c.append((d)**2)

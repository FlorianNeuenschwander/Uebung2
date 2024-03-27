#Übung2


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __abs__(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            return self + other
        
    def __mul__(self, other):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)
    

    def normalize(self):
        len = (self.x**2 + self.y**2 + self.z**2)**0.5
        return(self.x/len,self.y/len,self.z/len)

a = Vector3(3,4,2)
b = Vector3(2,1,0)
c = a * b # Komponentenweise Multiplikation
print(c)
d = a.dot(b) # Skalarprodukt
e = a.cross(b) # Kreuzprodukt



f=a+b
print(f)

g=a-b
print(g)

h=a*b
print(h)

i=a.dot(b)
print(i)

j=a.cross(b)
print(j)

k=a.normalize()
print(k)







class Treenode:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
#Membangun pohon keluarga

#kakek nenek
Kakek = Treenode("Fauzan", "laki-laki")
Nenek = Treenode("Novaria", "Perempuan")

#Anak pertama, kemudian memiliki keturunan
Ayah = Treenode("Andi", "laki-laki")
Ayah.add_child(Treenode("Wahyuni", "Perempuan"))
Ayah.add_child(Treenode("Ari", "Laki-laki"))

#Anak kedua, Kemudian memiliki keturunan
Ibu = Treenode("Amirah", "Perempuan")
Ibu.add_child(Treenode("Faza", "Perempuan"))

Kakek.add_child(Ayah)
Kakek.add_child(Ibu)

#Traversing (menelusuri) pohon keluarga
def traverse(node, level=0):
    print(" " * level + "- " + node.name + " (" + node.gender + ")")
    for child in node.children:
        traverse(child, level + 1)
        
traverse(Nenek)
traverse(Kakek)
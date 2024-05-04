class Treenode:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
#Membangun pohon keluarga

#kakek nenek
Kakek = Treenode("bayu", "Laki-laki")
Nenek = Treenode("kurnia", "Perempuan")

#Anak pertama, kemudian memiliki keturunan
Abi = Treenode("yudiyono", "Laki-laki")
Abi.add_child(Treenode("putri", "Perempuan"))
Abi.add_child(Treenode("Agus", "Laki-laki"))

#Anak kedua, Kemudian memiliki keturunan
Bulek = Treenode("fauziah", "Perempuan")
Bulek.add_child(Treenode("keyrana", "Perempuan"))

Kakek.add_child(Abi)
Kakek.add_child(Bulek)

#Traversing (menelusuri) pohon keluarga
def traverse(node, level=0):
    print(" " * level + "- " + node.name + " (" + node.gender + ")")
    for child in node.children:
        traverse(child, level + 1)
        
traverse(Nenek)
traverse(Kakek)
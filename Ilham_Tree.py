class Treenode:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
# Membangun pohon keluarga

# Kakek
Kakek = Treenode("Suraji", "laki-laki")

# Nenek
Nenek = Treenode("Siti", "perempuan")

# Anak pertama, kemudian memiliki keturunan
Ayah = Treenode("ilham", "laki-laki")
Ayah.add_child(Treenode("efinda", "perempuan"))
Ayah.add_child(Treenode("akbar", "laki-laki"))

# Anak kedua, kemudian memiliki keturunan
Ibu = Treenode("anisa", "perempuan")
Ibu.add_child(Treenode("azizah", "perempuan"))

# Menambahkan anak-anak ke kakek
Kakek.add_child(Ayah)
Kakek.add_child(Ibu)

# Traversing (menelusuri) pohon keluarga
def traverse(node, level=0):
    print(" " * level + "- " + node.name + " (" + node.gender + ")")
    for child in node.children:
        traverse(child, level + 1)
        
traverse(Nenek)
traverse(Kakek)
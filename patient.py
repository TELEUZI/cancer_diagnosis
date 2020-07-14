class Classification_chars:
    def __init__(self, p = [0 for n in range(1,11)]):
        self.clump_thickness = p[1]
        self.uniformity_of_cell_size = p[2]
        self.uniformity_of_cell_shape = p[3]
        self.marginal_adhension = p[4]
        self.single_epithelial_cell_size = p[5]
        self.bare_nuclei = p[6]
        self.bland_chromatin = p[7]
        self.normal_nucleoli = p[8]
        self.mitoses = p[9]
    def __add__(self, other):
        self.clump_thickness += other.clump_thickness
        self.uniformity_of_cell_size += other.uniformity_of_cell_size
        self.uniformity_of_cell_shape += other.uniformity_of_cell_shape
        self.marginal_adhension += other.marginal_adhension
        self.single_epithelial_cell_size += other.single_epithelial_cell_size
        self.bare_nuclei += other.bare_nuclei
        self.bland_chromatin += other.bland_chromatin
        self.normal_nucleoli += other.normal_nucleoli
        self.mitoses += other.mitoses
        return self

    def __truediv__(self, other):
        self.clump_thickness /= other
        self.uniformity_of_cell_size /= other
        self.uniformity_of_cell_shape /= other
        self.marginal_adhension /= other
        self.single_epithelial_cell_size /= other
        self.bare_nuclei /= other
        self.bland_chromatin /= other
        self.normal_nucleoli /= other
        self.mitoses /= other
        return self

    def __gt__(self, other):
        if ((self.clump_thickness > other.clump_thickness)or (self.uniformity_of_cell_size > other.uniformity_of_cell_size) or (self.uniformity_of_cell_shape > other.uniformity_of_cell_shape) or (self.marginal_adhension > other.marginal_adhension) or (self.single_epithelial_cell_size > other.single_epithelial_cell_size) or (self.bare_nuclei > other.bare_nuclei) or (self.bland_chromatin > other.bland_chromatin) or (self.normal_nucleoli > other.normal_nucleoli) or (self.mitoses > other.mitoses)):
            return self

class Patient_chars(Classification_chars):

    def __init__(self, p = [0 for n in range(11)]):
        super().__init__(p)
        self.id = p[0]
        self.patient_class = p[10]

    def __str__(self):
        return f'{self.id}, {self.clump_thickness}, {self.uniformity_of_cell_size}, {self.uniformity_of_cell_shape}, {self.marginal_adhension}, {self.single_epithelial_cell_size}, {self.bare_nuclei}, {self.bland_chromatin}, {self.normal_nucleoli}, {self.mitoses}, {self.patient_class}'
   
    
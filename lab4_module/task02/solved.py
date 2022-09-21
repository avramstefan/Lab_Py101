class Image():
    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=[[]]):
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels
    def __str__(self):
        # use this for debugging
        image = ""
        image += f"{self.format}{self.rows} {self.columns}\n{self.max_value}\n"
        for i in range(self.rows):
            for j in range(3 * self.columns):
                image += f"{self.pixels[i][j]} "
            image += "\n"
        return image
    def sepia(self):
        for i in range(0, self.rows):
            for j in range(0, 3 * self.columns, 3):
                r = self.pixels[i][j]
                g = self.pixels[i][j + 1]
                b = self.pixels[i][j + 2]
                sepia_r = (int)(0.393*r + 0.769*g + 0.189*b)
                sepia_g = (int)(0.349*r + 0.686*g + 0.168*b)
                sepia_b = (int)(0.272*r + 0.534*g + 0.131*b)
                if sepia_r > 255:
                    sepia_r = 255
                if sepia_b > 255:
                    sepia_b = 255
                if sepia_g > 255:
                    sepia_g = 255
                self.pixels[i][j] = sepia_r
                self.pixels[i][j + 1] = sepia_g
                self.pixels[i][j + 2] = sepia_b
    def read(self, filename):
        file = open(filename, 'r')

        self.format = file.readline()

        line = file.readline()
        self.rows = int(line[0])
        self.columns = int(line[2])

        line = file.readline()
        self.max_value = int(line)

        self.pixels = [[0] * 3 * self.columns for i in range(self.rows)]
        i = 0
        while i < self.rows:
            line = file.readline()
            j = 0
            list = line.split()
            while j < 3 * self.columns:
                self.pixels[i][j] = int(list[j])
                j = j + 1
            i = i + 1
            
        file.close()
    def write(self, filename):
        file = open(filename, 'w')
        lines = []
        lines.append(f"{self.format}")
        lines.append(f"{self.rows} {self.columns}\n")
        lines.append(f"{self.max_value}\n")
        i = 0
        while i < self.rows:
            j = 0
            line = ""
            while j < 3 * self.columns:
                line += f"{self.pixels[i][j]} "
                j =  j + 1
            line += "\n"
            lines.append(line)
            i = i + 1
        file.writelines(lines)
        file.close()
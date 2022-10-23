
class Complex:

    def __init__(self, real_part: int = 0, imaginary_part: int = 0, var_name: str = 'var') -> None:
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        self.var_name = var_name

    def __str__(self) -> str:

        tmp = self.imaginary_part
        ret_string = ""
    
        if self.imaginary_part == 1 or self.imaginary_part == -1:
            if self.imaginary_part == -1 and self.real_part == 0:
                self.imaginary_part = "-"
            else:
                self.imaginary_part = ""
        elif self.imaginary_part < 0:
            self.imaginary_part *= -1
        

        if tmp == 0 and self.real_part == 0:
            ret_string = f"{self.var_name} = 0"
        elif self.real_part == 0:
            if tmp < 0:
                ret_string = f"{self.var_name} = -{self.imaginary_part}i"
            else:
                ret_string = f"{self.var_name} = {self.imaginary_part}i"
        elif tmp == 0:
            ret_string = f"{self.var_name} = {self.real_part}"
        elif tmp < 0:
            ret_string = f"{self.var_name} = {self.real_part} - {self.imaginary_part}i"
        else:
            ret_string =  f"{self.var_name} = {self.real_part} + {self.imaginary_part}i"
    
        self.imaginary_part = tmp
        return ret_string

    def add_complex_numbers(self, other) -> None:
        self.real_part += other.real_part
        self.imaginary_part += other.imaginary_part

    def substract_complex_numbers(self, other) -> None:
        self.real_part -= other.real_part
        self.imaginary_part -= other.imaginary_part

    def multiply_complex_numbers(self, other) -> None:
        
        """
        We know you all love Math. :)
        """
        old_real_part_self = self.real_part
        old_img_part_self = self.imaginary_part

        old_real_part_other = other.real_part
        old_img_part_other = other.imaginary_part

        self.real_part = self.real_part * other.real_part - \
                    self.imaginary_part * other.imaginary_part

        self.imaginary_part = old_real_part_self * old_img_part_other + \
                        old_img_part_self * old_real_part_other

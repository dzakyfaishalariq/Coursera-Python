import numpy as np
import pandas as pd

import os


class myPermainan:
    informasi = "permainan kalkulator"
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tambah(self):
        return self.a + self.b

    def kurang(self):
        return self.a - self.b

    def kali(self):
        return self.a * self.b

    def bagi(self):
        return self.a / self.b

    def sisa(self):
        return self.a % self.b

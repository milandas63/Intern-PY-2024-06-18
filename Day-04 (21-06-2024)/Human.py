class Human:
    def __init__(self):
            print('Line from Human class')

class Male(Human):
    def __init__(self):
            super().__init__()
            print('Line from Male class')

m = Male()

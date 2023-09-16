class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.massage = 'Файл items.csv поврежден'

    def __str__(self):
        return self.massage

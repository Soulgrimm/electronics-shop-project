class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.massage = args[0] if args else 'Замена сообщения ошибки'

    def __str__(self):
        return self.massage

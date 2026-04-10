class Erros:
    def __init__(self):
        pass
    @staticmethod
    def missing_args(where):
        print(f'ERROR: missing_args in "{where}"')
    @staticmethod
    def app_not_found(app):
        print(f'ERROR:  "{app}" app_not_found. ')
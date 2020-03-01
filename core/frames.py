from pandas import DataFrame


class FileFrame(DataFrame):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class Direction_ERROR(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __str__(self) -> str:
        return "Direction {0} not accepted. Only Print_Forward and Print_Backward accepted".format(self.args)
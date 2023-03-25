from typing import Optional
import json


class Temp:
    def __init__(self, name: Optional[str]) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"The Temp Object ->{self.name}.."

    @classmethod
    def save(cls) -> None:
        """_summary_
        The method should save on DB or file or any other destination
        for example "print" method can save data :) 
        """
        print(f"save data {json.dumps(str(cls))}")


if __name__ == "__main__":
    t1 = Temp("test")
    t1.save()

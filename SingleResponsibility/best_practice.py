from typing import Optional
import json
from abc import ABC


class TempSaver(ABC):

    def __init__(self) -> None:
        pass

    def save(self, temp) -> None:
        pass


class Temp:
    def __init__(self, name: Optional[str], temp_store: TempSaver) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"The Temp Object ->{self.name}.."


class TempFileSaver(TempSaver):

    def __init__(self) -> None:
        pass

    def save(self, temp: Temp) -> None:
        print(f"save data {json.dumps(str(temp))}")


class TempPostgresSaver(TempSaver):

    def save(self, temp: Temp) -> None:
        """
        You can now override save method based on you need and save it on Postgres Sql
        """
        pass


if __name__ == "__main__":
    ts1 = TempFileSaver()
    t1 = Temp(name="test",
              temp_store=ts1)

    ts1.save(temp=t1)

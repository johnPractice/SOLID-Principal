## Definition
#### SRP (Single Responsibiliy Principle):
"A class should have<b> one and one</b> reason to change."
or 
"Every classes and methons or functions should have only one and only reason to change."

A bad example:
```
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

```
### Bad Things 🚫
1. First of all if we want to change the destination of saving source imagine we need to save data on DB like "Postgres SQL" or "Mongo DB".
In this scenario we must change <i>save</i> method on <b>Temp</b> class.
2. <b>Temp</b> class have two job 
    1) <b>init</b> Temp object.
    2) and save data with <b>save</b> method.
### Solution ✅
```

class TempSaver(ABC):

    def __init__(self) -> None:
        pass

    def save(self, temp) -> None:
        pass


class Temp:
    def __init__(self, name: Optional[str], temp_store: TempSaver) -> None:
        self.name = name
        self.obj_store = temp_store

    def __repr__(self) -> str:
        return f"The Temp Object ->{self.name}.."

    def save(self) -> None:
        self.obj_store.save(self)


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

```
1. Create new class for save <b>Temp</b> class object and give over the responsibilty of store logic on this class.
2. Inject tho stor class on <b>initialization</b> method of Temp class after that without knowing the logic of storing data and save Temp object.
If we want anther method for saving data or anther destination we can init new class and add logic to the <b>save</b> method.
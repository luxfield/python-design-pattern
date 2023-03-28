import Animal

class AnimalFactory:
    def create(name: str) -> Animal:
        match name.lower():
            case "tiger":
                Animal.Tiger().speak()
            case "cat":
                Animal.Cat().speak()
            case "dog":
                Animal.Dog().speak()
            case _:
                pass

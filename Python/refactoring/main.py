__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

'''
alice_name = "Alice Aliceville"
alice_profession = "electrician"
bob_name = "Bob Bobsville"
bob_profession = "painter"
craig_name = "Craig Craigsville"
craig_profession = "plumber"

alfred_name = "Alfred Alfredson"
alfred_address = "Alfredslane 123"
alfred_needs = ["painter", "plumber"]
bert_name = "Bert Bertson"
bert_address = "Bertslane 231"
bert_needs = ["plumber"]
candice_name = "Candice Candicedottir"
candice_address = "Candicelane 312"
candice_needs = ["electrician", "painter"]

alfred_contracts = []
for need in alfred_needs:
    if need == alice_profession:
        alfred_contracts.append(alice_name)
    elif need == bob_profession:
        alfred_contracts.append(bob_name)
    elif need == craig_profession:
        alfred_contracts.append(craig_name)

bert_contracts = []
for need in bert_needs:
    if need == alice_profession:
        bert_contracts.append(alice_name)
    elif need == bob_profession:
        bert_contracts.append(bob_name)
    elif need == craig_profession:
        bert_contracts.append(craig_name)

candice_contracts = []
for need in candice_needs:
    if need == alice_profession:
        candice_contracts.append(alice_name)
    elif need == bob_profession:
        candice_contracts.append(bob_name)
    elif need == craig_profession:
        candice_contracts.append(craig_name)

print("Alfred's contracts:", alfred_contracts)
print("Bert's contracts:", bert_contracts)
print("Candice's contracts:", candice_contracts)
'''


def main():
    print(alfred.contracts())
    print(bert.contracts())
    print(candice.contracts())
    print(electriciens[0].name)
    print(best_electrician())


class Homeowner():
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs

    def contracts(self):
        contracts = []
        first_name = self.name[:self.name.find(' ')]
        for need in self.needs:
            if need == "electrician":
                contracts.append(best_electrician())
            elif need == "painter":
                contracts.append(best_painter())
            elif need == "plumber":
                contracts.append(best_plumber())
        return f"{first_name}'s contracts: {contracts}"


alfred = Homeowner(
    "Alfred Alfredson",
    "Alfredslane 123",
    ["painter", "plumber"])
bert = Homeowner(
    "Bert Bertson",
    "Bertslane 231",
    ["plumber"])
candice = Homeowner(
    "Candice Candicedottir",
    "Candicelane 312",
    ["electrician", "painter"]
    )


class Specialist():
    def __init__(self, name, profession, rate):
        self.name = name
        self.profession = profession
        self.rate = rate


class Electrician(Specialist):
    pass


def best_electrician():
    best = ""
    for object in electriciens:
        if best == "":
            best = object
        elif object.rate < best.rate:
            best = object
    return best.name


electriciens = [
    Electrician("Alice Aliceville", "electrician", "40"),
    Electrician("Jan Janssen", "electrician", "30"),
    Electrician("Henk", "electrician", "20")
    ]


class Painter(Specialist):
    pass


def best_painter():
    best = ""
    for object in painters:
        if best == "":
            best = object
        elif object.rate < best.rate:
            best = object
    return best.name


painters = [
    Painter("Bob Bobsville", "painter", "30")
    ]


class Plumber(Specialist):
    pass


def best_plumber():
    best = ""
    for object in plumbers:
        if best == "":
            best = object
        elif object.rate < best.rate:
            best = object
    return best.name


plumbers = [
    Plumber("Craig Craigsville", "plumber", "80")
    ]


if __name__ == "__main__":
    main()

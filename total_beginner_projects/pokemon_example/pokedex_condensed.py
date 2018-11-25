import pokemon_moves

class Pokemon:
    def __init__(
            self, nickname, monster_type, elemental_type, base_hp,
            base_attack, base_defense, move_class_list):
        self.nickname = nickname
        self.monster_type = monster_type
        self.elemental_type = elemental_type
        self.base_hp = base_hp
        self.hp = base_hp
        self.base_attack = base_attack
        self.attack = base_attack
        self.base_defense = base_defense
        self.defense = base_defense
        self.level = 1
        self.experience = 0
        self.exp_required_for_level = 50
        self.move_dict = {}
        for pokemon_move_class in move_class_list:
            new_move = pokemon_move_class(self)
            self.move_dict[new_move.move_name] = new_move

    def use(self, move_name, target):
        self.move_dict[move_name].use_on(target)


class Cyndaquil(Pokemon):
    def __init__(self, nickname):
        move_classes = [
                pokemon_moves.Tackle, pokemon_moves.CombHair,
                pokemon_moves.Growl]
        super().__init__(
                nickname, "cyndaquil", "fire", 24, 8, 2, move_classes)
        

class Machamp(Pokemon):
    def __init__(self, nickname):
        move_classes = [pokemon_moves.Tackle, pokemon_moves.CombHair]
        super().__init__(
                nickname, "machamp", "fighting", 40, 13, 6, move_classes)


class Ganja(Pokemon):
    def __init__(self, nickname):
        move_classes = [
                pokemon_moves.Tackle, pokemon_moves.CombHair,
                pokemon_moves.Vinewhip, pokemon_moves.LightUp]
        super().__init__(
                nickname, "ganja", "grass", 28, 5, 5, move_classes)


class Geodude(Pokemon):
    def __init__(self, nickname):
        move_classes = [pokemon_moves.Tackle]
        super().__init__(
                nickname, "geodude", "rock", 32, 8, 6, move_classes)

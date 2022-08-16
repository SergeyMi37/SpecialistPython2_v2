# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
    def __repr__(self): 
        return self.to_str()
    def to_str(self):
        symbols = {
            "Hearts":   "\u2665",
            "Diamonds": "\u2666",
            "Spades":   "\u2663",
            "Clubs":    "\u2660"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit==other_card.suit

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for val in values:
            for suit in suits:
                self.cards.append(Card(val,suit))
    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_list = []
        for card in self.cards:
            cards_list.append(card.to_str())
        return f"cards[{len(self.cards)}]{' ,'.join(cards_list)}"


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())

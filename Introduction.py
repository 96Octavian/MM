class Introduction:
    def __init__(self):
        self.greeting = "Ciao! Complimenti per il tuo primo file python"
        self.name = ""

    def greet(self):
        if self.name:
            print(f'Ciao {self.name}! Complimenti per il tuo primo file python!')
        else:
            print(self.greeting)

    def meet(self):
        while(True):
            self.name = input("Qual è il tuo nome?\n").upper()
            if self.name:
                break
            print("Dai non puoi non avere un nome")
        print(f'Molto piacere {self.name}')

if __name__ == '__main__':
    first = Introduction()
    first.greet()
    first.meet()
    first.greet()

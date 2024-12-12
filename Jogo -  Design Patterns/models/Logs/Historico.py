from models.Logs import Memento

class Historico():
    def AddMemento(self, memento: Memento):
        self.historico.append(memento)

    def ShowMemento(self):
        for memento in self.historico:
            print(memento)

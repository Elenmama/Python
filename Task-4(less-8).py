class Sklad:
    _sklad = {}
    def add(self, group, name):
        try:
            self._sklad[group].append(name)
        except:
            self._sklad[group] = [name]

    def delete(self, group, name):

        self._sklad[group].remove(name)
s = Sklad()
s.delete("a", "b")

class NotNumsInList(Exception):

    def __init__(self, msg):
        self.msg = msg


q = input()
w = []
while True:
    if q == "stop" or q == "стоп":
        break
    try:
        try:
            int(q)
            w.append(int(q))
        except ValueError:
            raise NotNumsInList("Введено не число.")
    except NotNumsInList as d:
        print(d)
    finally:
        print("")
    q = input()
print(*w)

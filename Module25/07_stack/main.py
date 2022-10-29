class Stack(list):

    def push(self, element):
        self.append(element)

    def pop(self, *args):
        if len(self) != 0:
            return self.remove(self[-1])
        else:
            return None


class TaskManager(dict):

    def __str__(self):
        display = []
        if self:
            for i_priority in sorted(self.keys()):
                display.append(f"{i_priority} {self[i_priority]}\n")
        return "".join(display)

    def new_task(self, task, priority):
        if priority not in self:
            self[priority] = Stack()
        self[priority].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

"""
File: erapp.py
"""

from ermodel import ERModel, Patient, Condition

class ERView(object):
    """视图"""

    def __init__(self, model):
        self.model = model

    def run(self):
        menu = "Main menu\n" + \
               "  1  Schedule a patient\n" + \
               "  2  Treat the next patient\n" + \
               "  3  Treat all patients\n" \
               "  4  Exit the program"
        while True:
            command = self.get_command(4, menu)
            if command == 1:    self.schedule()
            elif command == 2:  self.treat_next()
            elif command == 3:  self.treat_all()
            else:   break

    def treat_next(self):
        """治疗下一个"""
        if self.model.isEmpty():
            print("No patients available to treat.")
        else:
            patient = self.model.treat_next()
            print(patient, "is being treated.")

    def treat_all(self):
        """治疗所有等待的患者"""
        if self.model.isEmpty():
            print("No patients available to treat.")
        else:
            while self.model.isEmpty() == False:
                self.treat_next()
            print()

    def schedule(self):
        """输入用户信息并调度用户"""
        name = input("\nEnter ther patinet's name: ")
        condition = self.get_condition()
        self.model.schedule(Patient(name, condition))
        print(name, "is added to the", condition, "list\n")

    def get_condition(self):
        """获得状态信息"""
        menu = "Patient's condition:\n" + \
               "  1  Critical\n" + \
               "  2  Serious\n" + \
               "  3  Fair"
        number = self.get_command(3, menu)
        return Condition(number)

    def get_command(self, high, menu):
        """返回一个状态"""
        prompt = "Enter a number [1-" + str(high) + "]: "
        command_range = list(map(str, range(1, high + 1)))
        error = "Error, number must be 1 to " + str(high)
        while True:
            print(menu)
            command = input(prompt)
            if command in command_range:
                return int(command)
            else:
                print(error)

def main():
    model = ERModel()
    view = ERView(model)
    view.run()

if __name__ == '__main__':
    main()
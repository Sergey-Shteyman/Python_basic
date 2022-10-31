import random


class Karma:

    __nirvana = 500
    __errors_file_name = "karma.log"

    def get_karma(self):
        return self.__nirvana

    def one_day(self):
        disaster = random.choice([
            KillError(), DrunkError(),
            CarCrashError(), GluttonyError(),
            DepressionError()
        ])
        disaster_point = random.randint(1, 10)
        if disaster_point != 10:
            nirvana_point = random.randint(1, 7)
            return nirvana_point
        else:
            self.handle_error(disaster)

    def handle_error(self, error):
        with open(self.__errors_file_name, "a") as errors:
            errors.write(error.__str__())
        raise error


class KillError(BaseException):

    def __str__(self):
        message = "\nKillError\nВы случайно умерли. Придется начать жить заново)"
        return message


class DrunkError(BaseException):

    def __str__(self):
        message = "\nDrunkError\nВы случайно перепили. Придется начать жить заново)"
        return message


class CarCrashError(BaseException):

    def __str__(self):
        message = "\nCarCrashError\nВы разбились на машине. Придется начать жить заново)"
        return message


class GluttonyError(BaseException):

    def __str__(self):
        message = "\nGluttonyError\nВы случайно переели и умерли(. Придется начать жить заново)"
        return message


class DepressionError(BaseException):

    def __str__(self):
        message = "\nGluttonyError\n"
        message += "Вы словили депрессию и не смогли из нее выбраться живым.\nПридется начать жить заново)"
        return message

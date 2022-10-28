import random


class Karma:

    __nirvana = 500

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
            return disaster


class KillError(BaseException):

    def __str__(self):
        message = "\nKillError\n" \
                  "Вы случайно умерли. Придется начать жить заново)"
        return message


class DrunkError(BaseException):

    def __str__(self):
        message = "\nDrunkError\n" \
                  "Вы случайно перепили. Придется начать жить заново)"
        return message


class CarCrashError(BaseException):

    def __str__(self):
        message = "\nCarCrashError\n" \
                  "Вы разбились на машине. Придется начать жить заново)"
        return message


class GluttonyError(BaseException):

    def __str__(self):
        message = "\nGluttonyError\n" \
                  "Вы случайно переели и умерли(. Придется начать жить заново)"
        return message


class DepressionError(BaseException):

    def __str__(self):
        message = "\nGluttonyError\n" \
                  "Вы словили депрессию и не смогли из нее выбраться живым.\n" \
                  "Придется начать жить заново)"
        return message

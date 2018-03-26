#!/usr/bin/python3.6

class ProgramWash:

    def __init__(self, **kwargs):
        """
        Constructor

        :param str material: Material
        :param int duration: Material
        :param bool pre_washing: Material
        """
        self.material = kwargs.get('material', 'unknown')
        self.duration = kwargs.get('duration')
        self.pre_washing = kwargs.get('pre_washing', False)

    def __repr__(self):
        return "material %s, duration %d, enabled pre %s" % (self.material, self.duration, self.pre_washing)


class DelicateProgramWash(ProgramWash):
    """
    Program for delicate or weakly dirt clothes
    """

    def __init__(self):
        super().__init__(duration=45, pre_washing=False)


class HardProgramWash(ProgramWash):
    """
    Program for dirty clothes
    """

    def __init__(self):
        super().__init__(material='cotton', duration=120, pre_washing=True)


class ProgramChangingException(Exception):
    pass


class WashMachine:
    def __init__(self, **kwargs):
        """
        Constructor

        :param ProgramWash program: Particular program
        :param int turns: Amount of turns
        """
        self.program = kwargs.get('program', None)
        self.turns = kwargs.get('turns', None)
        self.started = False

    def start(self):
        print("Washing has been started program %s , turns %s" % (self.program, self.turns))

    def finish(self):
        print("Washing completed\n")

    def change_program(self, program):
        """
        Changes program

        :param ProgramWash program: A new program
        :raise: ProgramChangingException is thrown if machine is in active state
        """
        if self.started:
            raise ProgramChangingException("Program cannot be changed in active state")
        assert program
        self.program = program

print("Demonstrates delicate program")
program = DelicateProgramWash()
machine = WashMachine(program=program, turns=1000)
machine.start()
machine.finish()

print("Demonstrates hard program")
program = HardProgramWash()
machine.change_program(program)
machine.start()
machine.finish()

print("Demonstrates custom program")
program = ProgramWash(material = 'silk', duration = 30)
machine.change_program(program)
machine.start()
machine.finish()

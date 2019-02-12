class FileSizeDisplay:
    def __init__(self, number, output=None, short=True, decimal=2, divisor=1000):
        self._number = number

        #display
        self.output = output
        self.short = short
        self.decimal = decimal

        self._divsor = divisor

        self._levels = [
            ('KB', 'Kilobytes'),
            ('MB', 'Megabytes'),
            ('GB', 'Gigabytes'),
            ('TB', 'Terabytes'),
            ('PB', 'Pedabytes'),
        ]

        self.display_num = self._number
        self.raw_display_num = self._number

        self.display_unit = 'B'
        if not short:
            self.display_unit = 'Bytes'

        self.convert()

    def __str__(self):
        num = self.format_raw_display()
        return '{} {}'.format(num, self.display_unit)

    def format_raw_display(self):

        rv = round(self.raw_display_num, self.decimal)

        if not (self.raw_display_num % 1):
            rv = int(self.raw_display_num)



        return rv

    def convert(self):

        _display_num = self._number

        _iter = 0
        while _display_num >= self._divsor:

            abv, name = self._levels[_iter]

            _display_num = float(_display_num/self._divsor)

            self.display_unit = abv
            if not self.short:
                self.display_unit = name

            if self.output in [abv, name]:
                break

            _iter += 1

        self.raw_display_num = _display_num


print(FileSizeDisplay(1001, short=False, output='MB'))
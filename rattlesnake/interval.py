from itertools import cycle, takewhile, dropwhile
from rattlesnake.note import Note


class Interval(object):

    perfect, minor, major, diminished, augmented = intervals = ['Perfect', 'Minor', 'Major', 'Diminished', 'Augmented']


    def __init__(self, note, number, quality):
        self._note = note
        self._number = number
        self._quality = quality

        self._validate_interval()


    def _validate_interval(self):
        real_number = self._number % 7
        if real_number == 0:
            real_number = 7
        elif real_number == 1:
            real_number = 8

        if real_number < 1:
            raise ValueError("Interval number must be higher than 0.")

        if real_number == 1:
            if self._quality not in [self.perfect, self.augmented]:
                raise ValueError("Invalid quality for unison interval: %s" % self._quality)

        elif real_number % 4 == 0:
            if self._quality in [self.minor, self.major]:
                raise ValueError("Invalid quality for fourth interval: %s" % self._quality)

        elif real_number % 5 == 0:
            if self._quality in [self.minor, self.major]:
                raise ValueError("Invalid quality for fifth interval: %s" % self._quality)

        elif real_number % 8 == 0:
            if self._quality != self.perfect:
                raise ValueError("Invalid quality for octave interval: %s" % self._quality)

        elif self._quality == self.perfect:
            raise ValueError("Only unison, fourths, fifths and octaves can be perfect.")


    _interval_to_distance = {
        (1, perfect) : 0,
        (1, augmented) : 1,

        (2, diminished) : 0, # ?
        (2, minor) : 1,
        (2, major) : 2,
        (2, augmented) : 3,

        (3, diminished) : 2, # ?
        (3, minor) : 3,
        (3, major) : 4,
        (3, augmented) : 5,

        (4, diminished) : 4,
        (4, perfect) : 5,
        (4, augmented) : 6,

        (5, diminished) : 6,
        (5, perfect) : 7,
        (5, augmented) : 8,

        (6, diminished) : 7,
        (6, minor) : 8,
        (6, major) : 9,
        (6, augmented) : 10,

        (7, diminished) : 9,
        (7, minor) : 10,
        (7, major) : 11,
        (7, augmented) : 12, # ?

        (8, perfect) : 12
    }
    def distance(self):
        if self._number <= 8:
            return self._interval_to_distance[(self._number, self._quality)]


        interval = self._number % 7
        if interval == 0:
            interval = 7
        elif interval == 1:
            interval = 8

        octaves = self._number // 8
        if interval in [7, 8]:
            octaves += 1

        return octaves * 12 + self._interval_to_distance[(interval, self._quality)]


    _number_to_name = {
        1 : 'Unison',
        2 : 'Second',
        3 : 'Third',
        4 : 'Fourth',
        5 : 'Fifth',
        6 : 'Sixth',
        7 : 'Seventh',
        8 : 'Octave',
    }
    def name(self):
        if self._number <= 8:
            return ' '.join([self._quality, self._number_to_name[self._number]])

        return ' '.join(['Compound', self._quality, self._number_to_name[self._pure_interval()]])


    def _pure_interval(self):
        interval = self._number % 7
        if interval == 0:
            interval = 7
        elif interval == 1:
            interval = 8

        return interval


    def _octaves_range(self):
        return (self._number - 1) // 7


    _notes_distances = [2, 2, 1, 2, 2, 2, 1]
    def target_note(self):
        source_note_index = Note.notes.index(self._note._note)
        target_note_index = source_note_index + self._number - 1

        should_ignore = lambda i: i[0] < source_note_index
        should_use = lambda i: i[0] < target_note_index
        distance = sum((x[1] for x in takewhile(should_use, dropwhile(should_ignore, enumerate(cycle(self._notes_distances))))))

        missing_distance = self.distance() - distance
        accidental_diference = Note.accidentals.index(self._note._accidental) + missing_distance

        target_note = Note.notes[target_note_index % 7]
        target_octave = self._octaves_range() + self._note._octave
        target_interval = Note.accidentals[accidental_diference]

        return Note(target_note, accidental=target_interval, octave=target_octave)


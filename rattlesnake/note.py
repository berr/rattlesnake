import re


class Note(object):

    C, D, E, F, G, A, B = notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    double_flat, flat, natural, sharp, double_sharp = accidentals = ['bb', 'b', '', '#', 'x']


    def __init__(self, note, **kwargs):
        if len(kwargs) == 0:
            note, accidental, octave = self._get_parameters_from_usual_notation(note)
        else:
            accidental = kwargs.pop('accidental', self.natural)
            octave = kwargs.pop('octave', 4)
            if len(kwargs) != 0:
                raise ValueError('Invalid parameters: %s' % list(kwargs.value()))

        if note not in self.notes:
            raise ValueError('Invalid note: %s' % note)
        self._note = note

        if accidental not in self.accidentals:
            raise ValueError('Invalid accidental: %s' % accidental)
        self._accidental = accidental

        if octave < 1:
            raise ValueError('Invalid octave: %s' % octave)
        self._octave = octave


    def _get_parameters_from_usual_notation(self, notation):
        notes_pattern = r'([a-gA-G])(bb|b|#|x)?(\d+)?'
        note, accidental, octave = re.match(notes_pattern, notation).groups()

        note = note.upper()
        if accidental is None:
            accidental = ''
        if octave is None:
            octave = 4
        else:
            octave = int(octave)

        return note, accidental, octave


    def from_c1(self):
        octaves = self._octave - 1
        semitones = octaves * 12

        note_to_semitone_distance = [0, 2, 4, 5, 7, 9, 11]
        note_index = self.notes.index(self._note)
        semitones += note_to_semitone_distance[note_index]

        quality_index = self.accidentals.index(self._accidental)
        semitones += quality_index - 2

        return semitones







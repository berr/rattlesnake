import pytest
from rattlesnake.interval import Interval
from rattlesnake.note import Note


@pytest.mark.parametrize('bass_note, number, quality, expected_distance, expected_name, expected_note', [
    (Note('C'), 1, Interval.perfect, 0, 'Perfect Unison', Note('C')),
    (Note('C'), 1, Interval.augmented, 1, 'Augmented Unison', Note('C#')),

    (Note('C'), 2, Interval.diminished, 0, 'Diminished Second', Note('Dbb')),
    (Note('C'), 2, Interval.minor, 1, 'Minor Second', Note('Db')),
    (Note('C'), 2, Interval.major, 2, 'Major Second', Note('D')),
    (Note('C'), 2, Interval.augmented, 3, 'Augmented Second', Note('D#')),

    (Note('C'), 3, Interval.diminished, 2, 'Diminished Third', Note('Ebb')),
    (Note('C'), 3, Interval.minor, 3, 'Minor Third', Note('Eb')),
    (Note('C'), 3, Interval.major, 4, 'Major Third', Note('E')),
    (Note('C'), 3, Interval.augmented, 5, 'Augmented Third', Note('E#')),

    (Note('C'), 4, Interval.diminished, 4, 'Diminished Fourth', Note('Fb')),
    (Note('C'), 4, Interval.perfect, 5, 'Perfect Fourth', Note('F')),
    (Note('C'), 4, Interval.augmented, 6, 'Augmented Fourth', Note('F#')),

    (Note('C'), 5, Interval.diminished, 6, 'Diminished Fifth', Note('Gb')),
    (Note('C'), 5, Interval.perfect, 7, 'Perfect Fifth', Note('G')),
    (Note('C'), 5, Interval.augmented, 8, 'Augmented Fifth', Note('G#')),

    (Note('C'), 6, Interval.diminished, 7, 'Diminished Sixth', Note('Abb')),
    (Note('C'), 6, Interval.minor, 8, 'Minor Sixth', Note('Ab')),
    (Note('C'), 6, Interval.major, 9, 'Major Sixth', Note('A')),
    (Note('C'), 6, Interval.augmented, 10, 'Augmented Sixth', Note('A#')),

    (Note('C'), 7, Interval.diminished, 9, 'Diminished Seventh', Note('Bbb')),
    (Note('C'), 7, Interval.minor, 10, 'Minor Seventh', Note('Bb')),
    (Note('C'), 7, Interval.major, 11, 'Major Seventh', Note('B')),
    (Note('C'), 7, Interval.augmented, 12, 'Augmented Seventh', Note('B#')),

    (Note('C4'), 8, Interval.perfect, 12, 'Perfect Octave', Note('C5')),

    (Note('D'), 3, Interval.minor, 3, 'Minor Third', Note('F')),
    (Note('D'), 3, Interval.major, 4, 'Major Third', Note('F#')),

    (Note('D'), 3, Interval.augmented, 5, 'Augmented Third', Note('Fx')),
    (Note('D#'), 3, Interval.diminished, 2, 'Diminished Third', Note('F')),
    (Note('Dx'), 3, Interval.diminished, 2, 'Diminished Third', Note('F#')),

    (Note('E'), 2, Interval.minor, 1, 'Minor Second', Note('F')),
    (Note('E'), 2, Interval.major, 2, 'Major Second', Note('F#')),

    (Note('G'), 4, Interval.diminished, 4, 'Diminished Fourth', Note('Cb')),
    (Note('G'), 4, Interval.perfect, 5, 'Perfect Fourth', Note('C')),
    (Note('G'), 4, Interval.augmented, 6, 'Augmented Fourth', Note('C#')),

    (Note('C'), 9, Interval.major, 14, 'Compound Major Second', Note('D5')),
    (Note('C'), 16, Interval.major, 26, 'Compound Major Second', Note('D6')),
])
def test_interval(bass_note, number, quality, expected_distance, expected_name, expected_note):
    interval = Interval(bass_note, number, quality)

    assert interval.distance() == expected_distance
    assert interval.name() == expected_name
    assert str(interval.target_note()) == str(expected_note)



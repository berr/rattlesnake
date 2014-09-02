import pytest
from rattlesnake.interval import Interval
from rattlesnake.note import Note



@pytest.mark.parametrize('bass_note, number, quality, expected_distance, expected_name, expected_note', [
    (Note('C'), 3, Interval.minor, 3, 'Minor Third', Note('Eb')),
    (Note('C'), 3, Interval.major, 4, 'Major Third', Note('E')),
    (Note('C'), 4, Interval.perfect, 5, 'Perfect Fourth', Note('F')),
    (Note('C'), 5, Interval.perfect, 7, 'Perfect Fifth', Note('G')),

    (Note('C'), 2, Interval.minor, 1, 'Minor Second', Note('Db')),


    (Note('C'), 9, Interval.major, 14, 'Compound Major Second', Note('D5')),
    (Note('C'), 16, Interval.major, 26, 'Compound Major Second', Note('D6')),


])
def test_interval(bass_note, number, quality, expected_distance, expected_name, expected_note):
    interval = Interval(bass_note, number, quality)

    assert interval.distance() == expected_distance
    assert interval.name() == expected_name



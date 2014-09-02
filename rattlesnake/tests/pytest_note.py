import pytest
from rattlesnake.note import Note



@pytest.mark.parametrize('note, expected_note, expected_accidental, expected_octave', [
    ('c', Note.C, Note.natural, 4),
    ('C', Note.C, Note.natural, 4),
    ('C#1', Note.C, Note.sharp, 1),
    ('D#', Note.D, Note.sharp, 4),
    ('E7', Note.E, Note.natural, 7),
    ('Fx', Note.F, Note.double_sharp, 4),
    ('Gb', Note.G, Note.flat, 4),
    ('Abb2', Note.A, Note.double_flat, 2),
    ('bx3', Note.B, Note.double_sharp, 3),
    ('bb3', Note.B, Note.flat, 3),
    ('bbb4', Note.B, Note.double_flat, 4),
])
def test_instantiation(note, expected_note, expected_accidental, expected_octave):
    note = Note(note)
    assert note._note == expected_note
    assert note._accidental == expected_accidental
    assert note._octave == expected_octave


@pytest.mark.parametrize('note, expected_distance', [
    ('C1', 0),
    ('C#1', 1),
    ('Cx1', 2),
    ('C2', 12),
    ('D2', 14),
    ('E2', 16),
    ('E#2', 17),
    ('Ex2', 18),
    ('Eb2', 15),
    ('Ebb2', 14),
    ('B1', 11)
])
def test_distance(note, expected_distance):
    note = Note(note)
    assert note.from_c1() == expected_distance

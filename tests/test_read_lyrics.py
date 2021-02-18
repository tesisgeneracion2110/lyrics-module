from sample.read_lyrics import delete_empty_lines
import pytest


@pytest.mark.parametrize('data, result', [
    ('first line\n\nsecond line\n', 'first line\n\nsecond line\n'),
    ('first line\nsecond line\n', 'first line\nsecond line\n'),
    ('', '')
])
def test_delete_empty_lines(data, result):
    assert delete_empty_lines(data) == result

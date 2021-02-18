import sample.adjust
import pytest


@pytest.mark.parametrize('data, result', [
    ('first line\n\nsecond line\n', 'first line\n\nsecond line\n'),
    ('first line\nsecond line\n', 'first line\nsecond line\n'),
    ('', '')
])
def test_delete_empty_lines(data, result):
    assert sample.adjust.delete_empty_lines(data) == result

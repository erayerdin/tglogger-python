def test_not_empty(meta_archive):
    assert len(meta_archive.namelist()) != 0


def test_first_file(meta_first_file):
    assert meta_first_file.read() == b"foo"

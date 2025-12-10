from src.file_ops import uppercase_file

def test_uppercase(tmp_path):
    infile = tmp_path / "in.txt"
    outfile = tmp_path / "out.txt"

    infile.write_text("hello")

    uppercase_file(infile, outfile)

    assert outfile.read_text() == "HELLO"

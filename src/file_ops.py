def uppercase_file(infile, outfile):
    outfile.write_text(infile.read_text().upper())

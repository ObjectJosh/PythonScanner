with open('input.py') as input_file:
    line_num = 1
    for line in input_file:
        tab = line.find('\t')
        stripped = line.strip('\n')
        line_length = len(line)
        if line_length > 1:
            last_char = stripped[len(stripped) - 1]
        if line_length > 79:
            print("Line too long: %d Characters: %d"%(line_num, line_length))
        if tab != -1:
            print("Tab found in line: %d"%(line_num))
        if last_char == " ":
            print("Trailing whitespace at end of line: %d"%(line_num))
        if last_char == ";":
            print("Found semicolon at end of line: %d"%(line_num))
        line_num += 1
input_file.close()
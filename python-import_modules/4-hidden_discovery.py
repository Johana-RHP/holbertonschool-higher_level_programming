#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for line in dir(hidden_4):
        if line[:0] != '_' and line[:1] != '_':
            print(line)

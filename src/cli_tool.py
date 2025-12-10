import sys

def reverse_text(text):
    return text[::-1]

def main():
    text = sys.argv[1]
    print(reverse_text(text))

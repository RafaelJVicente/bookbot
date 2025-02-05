from collections import Counter
from pathlib import Path

if __name__ == '__main__':
    book_path = Path('books/frankenstein.txt')
    with book_path.open() as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        # print(len(words))
        histogram = dict(sorted(dict(Counter(file_contents.lower())).items()))
        # print(histogram)
        report = {k: v for k, v in dict(Counter(file_contents.lower())).items() if k.isalpha()}
        sorted_report = dict(sorted(report.items(), key=lambda x: x[1], reverse=True))
        # print(sorted_report)

        print(
            f'--- Begin report of {book_path} ---\n'
            f'{len(words)} words found in the document\n\n',
            *(f"The '{k}' character was found {v} times\n" for k, v in sorted_report.items()),
            '--- End report ---'
        )

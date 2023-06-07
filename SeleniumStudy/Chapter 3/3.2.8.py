def test_substring(full_string, substring):
    assert substring in full_string, f'expected \'{substring}\' to be substring of \'{full_string}\''





if __name__ == '__main__':
    print(test_substring('fulltext', 'some_value'))
    print(test_substring('some', 'some_text'))
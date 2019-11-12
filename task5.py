"""
@Makers
Write a function string_length that takes in a string and returns its length.
HINT:
Question: What do you mean by length?
Answer: The character count of a string.
Ex: string_length('hello!') # --> 6
Explanation: calling string_length() function on the string 'hello!'
should give me back 6.
"""
def string_length(word):
    return len(word)
#write your code here...
#DO NOT remove lines below here, this is designed to test your code.
def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_string_length()
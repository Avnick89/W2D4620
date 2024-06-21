'''
1. **Dot (.)**
    - The wildcard: Matches any single character except newline (`\n`).
    - Imagine it as a shape-shifter, able to become any character you need, just for a moment.
2. **Caret (^)**
    - The anchor for the start of a string.
    - Like a sentinel, standing guard at the beginning of your text.
3. **Dollar ($)**
    - The anchor for the end of a string.
    - The sentinel at the gates, ensuring nothing goes beyond the end of your text.
4. **Asterisk (*)**
    - Matches zero or more occurrences of the pattern left to it.
    - Think of it as a multiplier, creating copies of the character before it.
5. **Plus (+)**
    - Matches one or more occurrences of the pattern left to it.
    - Similar to the asterisk, but insists on at least one occurrence.
6. **Question Mark (?)**
    - It makes the preceding character optional.
    - It's the symbol of uncertainty, allowing flexibility in your patterns.
7. **Backslash (\)**
    - Escapes special characters or signals a special sequence.
    - The key to differentiating between a literal character and a magical symbol.
8. **Square Brackets ([])**
    - A set of characters. Matches any one character in the brackets.
    - Like choosing one tool from a toolbox, it selects one character from a set.
9. **Pipe (|)**
    - The OR operator. It matches either the pattern before or after it.
    - A fork in the road, giving you a choice between paths.
10. **Parentheses (())**
    - Groups patterns together and captures them.
    - Think of them as binding a spell, containing its power within.
11. **Curly Braces ({})**
    - Curly braces are used to define the exact number of times a character or a pattern must occur for a match to be found.
    - It's like telling your magic spell exactly how much power to use.
'''
### **Simple Exercises for Understanding**


'''
1.  **Dot (.) - The Wildcard Character**
    - **Task**: Find any three-character sequence in a text, where the middle character can be anything, the first has to be ‘c’ and the last has to be ‘t’.
    - **Regex Pattern**: `c.t`
    - **Test Sentence**: "I found a cat, a cot, and a cut in the room and the cat was cute, ctt cct coot colt"
    - **Expected Matches**: `['cat', 'cot', 'cut', cat, cut]`
    - **Explanation**: The dot `.` matches any single character (except newline), so it finds sequences where 'c' and 't' are separated by any character.
2. **Caret (^) - The Beginning Anchor**
    - **Task**: Find strings that start with 'Py'.
    - **Regex Pattern**: `^Py`
    - **Test Sentence**: "Python is fun"
    - **Expected Matches**: `[’Py’]` from 'Python' at the beginning of the sentence.
    - **Explanation**: The caret `^` ensures that the match must occur at the start of the string or line.
3. **Dollar ($) - The End Anchor**
    - **Task**: Identify strings that end with 'fun'.
    - **Regex Pattern**: `fun$`
    - **Test Sentence**: "Learning regex is fun"
    - **Expected Matches**: `['fun']` from 'Learning regex is fun.'
    - **Explanation**: The dollar `$` ensures that 'fun' is matched only if it's at the end of the string or line.
4. **Asterisk (*) - Zero or More Occurrences**
    - **Task**: Match a character followed by zero or more 'a's.
    - **Regex Pattern**: `ba*`
    - **Test Sentence**: "I saw a bat, and a ball in my bed, baaah!"
    - **Expected Matches**: `['ba', 'ba', 'b', 'baaa']` from ‘bat’, ‘ball’, ‘bed’, and ‘baaah!’.
    - **Explanation**: The pattern starts with the literal character 'b'. This means it will first look for occurrences of 'b' in the text. Following the 'b', we have 'a*'. Then, the asterisk  `*` which matches zero or more occurrences of the preceding character ('a' in this case).
5. **Plus (+) - One or More Occurrences**
    - **Task**: Find a character followed by one or more 'a's.
    - **Regex Pattern**: `ba+`
    - **Test Sentence**: "The battle of ba and baat."
    - **Expected Matches**: `['ba', 'ba', 'baa']` from ‘battle’, ‘ba’, and ‘baat’.
    - **Explanation**: The plus `+` matches one or more occurrences of the preceding character ('a' in this case).
6. **Question Mark (?) - Zero or One Occurrence**
    - **Task**: Match 'colour' or 'color'.
    - **Regex Pattern**: `colou?r`
    - **Test Sentence**: "The color is nice. I like this colour."
    - **Expected Matches**: `['color', 'colour']`
    - **Explanation**: The question mark `?` makes the preceding character ('u' in this case) optional.
7. **Backslash (\) - Escaping Special Characters**
    - **Task**: Match a period character in a sentence.
    - **Regex Pattern**: **`\.`**
    - **Test Sentence**: "End of sentence. Start of a new one."
    - **Expected Matches**: The periods `[.]` at the end of 'sentence.' and before 'Start'.
    - **Explanation**: In regex, the period (.) is a special character used as a wildcard. To match an actual period, the backslash **`\`** is used to escape the special meaning of the period, treating it as a literal character. The pattern **`\.`** specifically looks for the period character in the text.
8. **Square Brackets ([]) - Character Sets**
    - **Task**: Find all vowels in a word.
    - **Regex Pattern**: `[aeiou]`
    - **Another Pattern**: `[A-Za-z+]` - 
    - **Test Word**: "Regular"
    - **Expected Matches**: `['e', 'u', 'a']`
    - **Explanation**: The square brackets `[]` define a set of characters, any of which can be matched.
9. **Pipe (|) - The OR Operator**
    - **Task**: Match 'cat' or 'dog'.
    - **Regex Pattern**: `cat|dog`
    - **Test Sentence**: "I have a cat and a dog."
    - **Expected Matches**: `['cat', 'dog']`
    - **Explanation**: The pipe `|` acts as an OR operator, matching either the pattern before or after it.
10. **Parentheses (()) - Grouping**
    - **Task**: Find repetitions of 'woof' or 'meow'.
    - **Regex Pattern**: `(woof|meow)+`
    - **Test Sentence**: "The pets say woof woof and meow."
    - **Expected Matches**: `['woof’,  'woof', 'meow']`
    - **Explanation**: Parentheses `()` group patterns, allowing the plus `+` to apply to the entire group.
11. **Curly Braces ({}) - Specifying Exact Occurrences**
    - **Task**: Match a word where 'l' is followed by exactly two 'o's.
    - **Regex Pattern**: **`lo{2}`**
    - **Regex Pattern**: **`[L|lo{2}]`**
    - **Regex Pattern**: **`[A-Z|a-zo{2}]`**
    - **Test Sentence**: "Look at the loom and the balloon in the room, loser."
    - **Expected Matches**: ['loo', 'loo']
    - **Explanation**: The pattern **`lo{2}`** searches for an 'l' followed by exactly two 'o's. In our test sentence, it successfully identifies 'loo' within the words 'loom' and 'balloon', demonstrating the ability of curly braces **`{}`** to specify an exact number of occurrences.

'''

"""1. **\d - The Digit Hunter**
    - Hunts down digits (0-9) in your text.
    - It's like a metal detector that beeps only when it finds numbers.
2. **\w - The Word Wizard**
    - Finds word characters (letters, digits, and underscores).
    - Imagine it as a magnet that attracts only words and numbers, leaving everything else behind.
3. **\s - The Space Scout**
    - Seeks out whitespace (spaces, tabs, newlines).
    - Think of it as a radar that pings whenever it detects open space in your text.

### **Putting Special Sequences to the Test**

1. **The Digit Hunter in Action**:
    - **Task**: Extract all phone numbers from a text for a phone number in the format 'XXX-XXX-XXXX', where each 'X' is a digit
    - **Regex Pattern**: `\d{3}-\d{3}-\d{4}`
    - **Test Sentence**: "Call me at 123-456-7890 or 987-654-3210."
    - **Expected Matches**: `['123-456-7890', '987-654-3210']`
    - **Explanation**: The `\d` sequence finds digits, and `{3}` specifies exactly three digits. The hyphen `-` is a literal character, It separates different segments of the phone number. Overall, this pattern searches for sequences like a U.S. standard phone number format.
2. **The Word Wizard’s Spell**:
    - **Task**: Identify words containing numbers.
    - **Regex Pattern**: `\w+\d+\w*`
    - **Test Sentence**: "My username is user123 and my password is pass99word. my really cool username is Rhoadehouse10 fhosdhflsjdhfljsdhf"
    - **Expected Matches**: `['user123', 'pass99word', "Rhoadehouse]`
    - **Explanation**: `\w*` matches any word character zero or more times, and `\d` ensures there's at least one digit. This pattern finds words mixed with numbers.
3. **The Space Scout’s Exploration**:
    - **Task**: Split a sentence into words.
    - **Regex Pattern**: `\s+`
    - **Test Sentence**: "Welcome to the world of        regex!"
    - **Expected Matches**: The spaces between ' ', ' ', ' ', ' ', '        '’
    - **Explanation**: `\s+` matches one or more whitespace characters. It does not match the characters of the words themselves but the empty space that separates them, allowing us to see where one-word ends and another begins.

### **More Special Sequences**

1. **\D - The Non-Digit Detector**
    - Finds any character that is not a digit.
    - Like a filter that lets everything but coins pass through.
2. **\W - The Non-Word Character Identifier**
    - Matches any character that is not a word character (opposite of \w).
    - Imagine it as a tool that highlights everything in the text that isn't a word or number.
3. **\S - The Non-Whitespace Finder**
    - Identifies any character that is not a whitespace.
    - It's like a spotlight that ignores spaces and shines on everything else.
4. **\b - The Word Boundary Beacon** " as."
    pattern = "\b[as]\b
    - A marker for the positions between a word and a non-word character.
    - Think of it as a flare that lights up the borders of each word.
5. **\B - The Non-Word Boundary Signal**
    - Matches positions where a word boundary does not occur.
    - It’s the silent guardian that watches over continuous strings of word characters without interruption.
6. **\A - The Beginning Sentinel**
    - Matches only at the start of the string.
    - It’s like a gatekeeper that only allows patterns that appear right at the opening of your text.
7. **\Z - The End Guardian**
    - Matches only at the end of the string, before the final newline, if one exists.
    - Think of it as the final checkpoint at the very end of your textual journey.

    """
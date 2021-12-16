"""Advent of code: https://adventofcode.com/2021/day/10
Day 10 Puzzle 1
You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:
Syntax error in navigation subsystem on line: all of them
You bring up a copy of the navigation subsystem (your puzzle input).
The navigation subsystem syntax is made of several lines containing chunks.
There are one or more chunks on each line, and chunks contain zero or more other chunks.
Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any)
can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:
If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is [].
More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]],
and even (((((((((()))))))))).
Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.
A corrupted line is one where a chunk closes with the wrong character -
that is, where the characters it opens and closes with do not form
one of the four legal pairs listed above.
Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]).
Such a chunk can appear anywhere within a line, and its presence
causes the whole line to be considered corrupted.
For example, consider the following navigation subsystem:
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore
these lines for now. The remaining five lines are corrupted:
{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.
Did you know that syntax checkers actually have contests to see who can get
the high score for syntax errors in a file? To calculate the syntax error score
for a line, take the first illegal character on the line and look it up in the following table:
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points),
an illegal ] was found once (57 points), an illegal } was found once (1197 points),
and an illegal > was found once (25137 points). So, the total syntax error score
for this file is 6+57+1197+25137 = 26397 points.
Find the first illegal character in each corrupted line of the navigation subsystem.
What is the total syntax error score for those errors?
"""

file_path = 'day_10_data.txt'

errors = {')': 3, ']': 57, '}': 1197, '>': 25137}


def analyze_sequence(seq: str) -> int:
    """Function checks validity of a bracket sequence
    and returns error score for the first invalid element or 0,
    if the sequence is valid or incomplete.
    :param seq: String containing a sequence of opening and closing brackets
    :return: Error score for the sequence
    """
    opening_brackets = {'(', '[', '{', '<'}
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

    # Check the 1st element.
    if seq[0] not in opening_brackets:
        return errors[seq[0]]

    stack = seq[0]

    for bracket in seq[1:]:
        # Any opening element is added to stack.
        if bracket in opening_brackets:
            stack += bracket
        else:
            # Closing elements are compared with the last element in stack.
            opening_bracket = pairs[bracket]
            if opening_bracket != stack[-1]:
                return errors[bracket]
            else:  # Remove the last element if it matches the new bracket.
                stack = stack[:-1]
    return 0


total_score = 0

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        score = analyze_sequence(line.strip())
        total_score += score

print(total_score)

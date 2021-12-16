"""Advent of code: https://adventofcode.com/2021/day/10
Day 10 Puzzle 2
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
Some lines are incomplete, but others are corrupted.
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
Discard the corrupted lines. The remaining lines are incomplete.
Incomplete lines don't have any incorrect characters - instead, they're missing
some closing characters at the end of the line. To repair the navigation subsystem,
you just need to figure out the sequence of closing characters that complete all open chunks in the line.
You can only use closing characters (), ], }, or >), and you must add them
in the correct order so that only legal pairs are formed and all chunks end up closed.
In the example above, there are five incomplete lines:
[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? The score is determined
by considering the completion string character-by-character. Start with a total score of 0.
Then, for each character, multiply the total score by 5 and then increase the total score
by the point value given for the character in the following table:
): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:
Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:
}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores
and then taking the middle score. (There will always be an odd number of scores to consider.)
In this example, the middle score is 288957 because there are
the same number of scores smaller and larger than it.
Find the completion string for each incomplete line, score the completion strings,
and sort the scores. What is the middle score?
"""

file_path = 'day_10_data.txt'

errors = {')': 1, ']': 2, '}': 3, '>': 4}


def analyze_sequence(seq: str) -> str:
    """Function checks validity of a bracket sequence
    and returns missing elements if the sequence is incomplete
    or an empty string if the sequence is valid or corrupt.
    :param seq: String containing a sequence of opening and closing brackets
    :return: String containing missing values if needed
    """
    opening_brackets = {'(', '[', '{', '<'}
    opening_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    closing_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    # Check the 1st element.
    if seq[0] not in opening_brackets:
        return ''

    stack = seq[0]

    for bracket in seq[1:]:
        # Any opening element is added to stack.
        if bracket in opening_brackets:
            stack += bracket
        else:
            # Closing elements are compared with the last element in stack.
            opening_bracket = opening_pairs[bracket]
            if opening_bracket != stack[-1]:
                return ''
            else:  # Remove the last element if it matches the new bracket.
                stack = stack[:-1]

    # Reverse the remaining elements and return missing brackets.
    missing_brackets = ''
    if len(stack) > 0:
        for bracket in stack[::-1]:
            missing_brackets = missing_brackets + closing_pairs[bracket]

    return missing_brackets


scores = []

with open(file_path, 'r') as file_handler:
    for line in file_handler:
        autocomplete = analyze_sequence(line.strip())

        score = 0
        for element in autocomplete:
            score = score * 5 + errors[element]

        if score != 0:
            scores.append(score)

# Find the score in the middle.
scores.sort()
mid_index = len(scores) // 2
print(scores[mid_index])

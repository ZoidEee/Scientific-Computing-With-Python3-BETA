def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first_operand, operator, second_operand = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)

        if show_answers:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))
            else:
                result = str(int(first_operand) - int(second_operand))
            results.append(result)

    arranged_problems = []
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for i in range(len(problems)):
        first_operand = first_operands[i]
        second_operand = second_operands[i]
        operator = operators[i]

        width = max(len(first_operand), len(second_operand)) + 2
        first_line.append(first_operand.rjust(width))
        second_line.append(operator + second_operand.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            answers.append(results[i].rjust(width))

    arranged_problems.append('    '.join(first_line))
    arranged_problems.append('    '.join(second_line))
    arranged_problems.append('    '.join(dashes))

    if show_answers:
        arranged_problems.append('    '.join(answers))

    return '\n'.join(arranged_problems)


# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
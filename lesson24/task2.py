sequence = input('Enter sequence: ')
# ((3 + 2) + [(4638 * 34926)] / {{2638}})
stack = []
is_correct = True
for elem in sequence:
    if elem in '([{':
        stack.append(elem)
    elif elem in ')]}':
        if len(stack) == 0:
            is_correct = False
            break

        last_elem = stack.pop()
        if last_elem == '(' and elem == ')':
            continue
        if last_elem == '[' and elem == ']':
            continue
        if last_elem == '{' and elem == '}':
            continue

        is_correct = False
        break

if is_correct and len(stack) == 0:
    print('sequence is correct')
else:
    print('sequence is incorrect')


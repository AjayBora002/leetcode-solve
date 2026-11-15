def insert_at_position(stack, target_index, item):
    temp_stack = Stack()

    # 1. Pop elements above the target position into temp_stack
    while stack.size() > target_index:
        temp_stack.push(stack.pop())

    # 2. Push the new item at the desired position
    stack.push(item)

    # 3. Put the popped elements back on top
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
# Trắc nghiệm
# 1.B
# 2.A
# 3.B
# 4.C
# 5.A
# 6.A
# 7.B
# 8.D
# 9.C
# 10.A
# 11.A
# 12.A
# 13.B
# 14.A
# 15.B
# 16.A
# 17.A
# 18.B
# 19.A
# 20.A

# Thực hành 1
def enqueue_print_job(queue, job):
    queue.append(job)

def dequeue_print_job(queue):
    if queue:
        return queue.pop(0)  
    else:
        return "Không có công việc in nào!"

print_queue = []

enqueue_print_job(print_queue, "Văn bản 1")
enqueue_print_job(print_queue, "Văn bản 2")
enqueue_print_job(print_queue, "Văn bản 3")

while print_queue:
    current_job = dequeue_print_job(print_queue)
    print(f"Đang in tác vụ: {current_job}")

# Thực hành 2
def record_move(stack, move):
    stack.append(move)

def undo_move(stack):
    if len(stack) > 0:
        return stack.pop()
    else:
        return "Không có di chuyển nào để hoàn tác!"

move_stack = []

record_move(move_stack, "Đi lên")
record_move(move_stack, "Đi qua phải")
record_move(move_stack, "Đi xuống")

print("Lịch sử di chuyển:", move_stack)

last_move = undo_move(move_stack)
print("Di chuyển vừa hoàn tác:", last_move)

print("Lịch sử di chuyển mới:", move_stack)
def merge_queues(queue1, queue2):
    merged_queue = []

    for i in range(min(len(queue1), len(queue2))):
        merged_queue.append(queue1[i])
        merged_queue.append(queue2[i])

    if len(queue1) > len(queue2):
        merged_queue.extend(queue1[len(queue2):])
    elif len(queue2) > len(queue1):
        merged_queue.extend(queue2[len(queue1):])

    return merged_queue

queue1 = [3, 6, 8]
queue2 = ['b', 'y', 'u', 't', 'r', 'o']
merged_queue = merge_queues(queue1, queue2)
print(merged_queue)

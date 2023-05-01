import itertools

# 人的名字分别为A、B、C、D、E、F
names = ['A', 'B', 'C', 'D', 'E', 'F']

# 每个人花费的金额
costs = [2, 1, 1, 1, 1, 2]

# resort
name_cost_pairs = list(zip(names, costs))
name_cost_pairs.sort(key=lambda x: x[1])
names, costs = zip(*name_cost_pairs)

average_cost = sum(costs) / len(names)

diff = [cost - average_cost for cost in costs]

pairs = [pair for pair in itertools.combinations(names, 2)]

for pair in pairs:
    payer = pair[0]
    receiver = pair[1]
    payer_index = names.index(payer)
    receiver_index = names.index(receiver)
    amount = min(abs(diff[payer_index]), abs(diff[receiver_index]))
    if diff[payer_index] > 0 and diff[receiver_index] < 0:
        diff[payer_index] -= amount
        diff[receiver_index] += amount
        print(f"{payer}需要从{receiver}收到{amount}元")
    elif diff[payer_index] < 0 and diff[receiver_index] > 0:
        diff[payer_index] += amount
        diff[receiver_index] -= amount
        print(f"{payer}需要向{receiver}支付{amount}元")
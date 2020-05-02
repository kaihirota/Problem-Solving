n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

# assert len(a) == n, "length doesn't match n"

# n = # of products
# m = # of products to be selected
# a = votes for product 1 >= i >= n

minimum_vote = sum(a) / (4 * m)
# print(minimum_vote)

eligible = list(filter(lambda x: x >= minimum_vote, a))
# print(eligible)

if len(eligible) >= m:
    print("Yes")
else:
    print("No")

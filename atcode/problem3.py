n, k = list(map(int, input().split()))
results = set([n])
counter = 0
switch = False

while counter < 50:
    # print(n)

    if n == 0 or n == k or k == 0:
        print(n)
        switch = True
        break

    # test
    if n % k == 0:
        print('0')
        switch = True
        break


    n = min(n, abs(n - k))

    # detect loop
    if n in results:
        print(min(results))
        switch = True
        break
    else:
        results.add(n)

    counter += 1


if not switch:
    # print('loop ended n:', n)
    results = list(results)
    print(min(min(results), min(results) % k))

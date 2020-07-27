import bisect

def compute_previous_intervals(jobs: List[Tuple]):
    '''
    For every interval j, compute the rightmost mutually compatible interval i, where i < j

    input:
        jobs: list of jobs sorted by earliest finish time
    '''
    start = [job[0] for job in jobs]
    finish = [job[1] for job in jobs]

    p = []
    for j in range(len(jobs)):
        i = bisect.bisect_right(finish, start[j]) - 1 # rightmost interval f_i <= s_j
        p.append(i)

    return p

def compute_solution(jobs, OPT, p, ret, j):
    if j >= 0:  # will halt on OPT[-1]
        if jobs[j][-1] + OPT[p[j]] > OPT[j - 1]:
            ret += jobs[j],
            compute_solution(jobs, OPT, p, ret, p[j])
        else:
            compute_solution(jobs, OPT, p, ret, j - 1)
    return ret

def findMaxSubsetJobs(jobs):
    jobs.sort(key=lambda x: x[0])
    p = compute_previous_intervals(jobs)

    # compute OPTs iteratively in O(n), here we use DP
    OPT = defaultdict(int)
    OPT[-1] = 0
    OPT[0] = 0
    for j in range(1, len(jobs)):
        OPT[j] = max(jobs[j][-1] + OPT[p[j]], OPT[j - 1])

    # given OPT and p, find actual solution intervals in O(n)
    ret = []
    ret = compute_solution(jobs, OPT, p, ret, len(jobs) - 1)

    return sorted(ret, key=lambda x: x[1])

jobs = [(0, 6, 1), (1, 4, 10), (3, 5, 5), (3, 8, 8), (4, 7, 15), (5, 9, 12), (6, 10, 17), (8, 11, 4)]
findMaxSubsetJobs(jobs)


import heapq

class Solution:
    # def jobScheduling(self, startTime, endTime, profit):
    def jobScheduling(self, jobs):
        # Sort the jobs by start time, (NOT end time).
        # jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        jobs = sorted(jobs, key=lambda v: v[0])
        hp = []
        total = 0

        """
        Iterate through the jobs, use a heap to maintain all the job schedules,
        which are represented by (end, totalProfit) entries.
        At each iteration, pop out all the job schedules that are compatible with the next
        job, and keep the 'ans' updated to the max totalProfit we can achieve from all schedules.
        At the end of each iteration, we add the job and its profit as our latest schedule.
        """
        for s,e,p in jobs:
            while hp and hp[0][0] <= s:
                popd = heapq.heappop(hp)
                total = max(total, popd[1])

            heapq.heappush(hp, (e, p + total))

        while hp:
            popd = heapq.heappop(hp)
            total = max(total, popd[1])

        return total


jobs = [(0, 6, 1), (1, 4, 10), (3, 5, 5), (3, 8, 8), (4, 7, 15), (5, 9, 12), (6, 10, 17), (8, 11, 4)]
Solution().jobScheduling(jobs)

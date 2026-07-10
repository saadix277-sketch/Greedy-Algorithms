class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs):
    # Sort jobs by profit (highest first)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    schedule = [None] * max_deadline
    total_profit = 0

    for job in jobs:
        # Find the latest available slot
        for slot in range(job.deadline - 1, -1, -1):
            if schedule[slot] is None:
                schedule[slot] = job
                total_profit += job.profit
                break

    return schedule, total_profit


def main():
    jobs = [
        Job("J1", 2, 100),
        Job("J2", 1, 19),
        Job("J3", 2, 27),
        Job("J4", 1, 25),
        Job("J5", 3, 15)
    ]

    schedule, profit = job_sequencing(jobs)

    print("Selected Jobs:")
    for job in schedule:
        if job:
            print(f"{job.job_id} | Deadline: {job.deadline} | Profit: {job.profit}")

    print(f"\nTotal Profit: {profit}")


if __name__ == "__main__":
    main()

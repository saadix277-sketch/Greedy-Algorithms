# Job Sequencing with Deadlines using Greedy Algorithm

## Description
This project implements the Job Sequencing with Deadlines problem using a Greedy Algorithm. The goal is to schedule jobs before their deadlines while maximizing the total profit.

## Features
- Sorts jobs by profit in descending order.
- Assigns each job to the latest available time slot before its deadline.
- Calculates the maximum total profit.

## Algorithm
1. Sort all jobs by profit.
2. Find the maximum deadline.
3. Create available time slots.
4. Schedule each job in the latest free slot before its deadline.
5. Display selected jobs and total profit.

## Time Complexity
O(n log n + n × d)

where:
- n = Number of jobs
- d = Maximum deadline

## Language
Python

## Author
Mirza Saad Ul Hassan Baig

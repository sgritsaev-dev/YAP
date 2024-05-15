'''ID решения 114030549'''


def count_platforms(sorted_robots: list, limit: int) -> int:
    '''A function which takes a sorted list of robots weights and an weight
    limit one platform can take, returns amount of platforms
    needed to carry all robots.'''
    counter = 0
    left_flag = 0
    right_flag = len(sorted_robots)-1
    if sorted_robots[left_flag] == limit:
        return len(sorted_robots)
    while left_flag <= right_flag:
        if sorted_robots[right_flag] + sorted_robots[left_flag] > limit:
            right_flag -= 1
            counter += 1
        elif sorted_robots[right_flag] + sorted_robots[left_flag] <= limit:
            right_flag -= 1
            left_flag += 1
            counter += 1

    return counter


if __name__ == '__main__':
    robots = [int(robot_weight) for robot_weight in input().split()]
    limit = int(input())
    print(count_platforms(sorted(robots), limit))

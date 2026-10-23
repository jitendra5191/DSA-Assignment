"""
Question 1: Daily Temperatures

Given an array of integers temperatures representing the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer


if __name__ == "__main__":
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Input : {temps1}")
    print(f"Output: {daily_temperatures(temps1)}")

    temps2 = [30, 40, 50, 60]
    print(f"\nInput : {temps2}")
    print(f"Output: {daily_temperatures(temps2)}")

    temps3 = [30, 60, 90]
    print(f"\nInput : {temps3}")
    print(f"Output: {daily_temperatures(temps3)}")

    temps4 = [70, 70, 70]
    print(f"\nInput : {temps4}")
    print(f"Output: {daily_temperatures(temps4)}")

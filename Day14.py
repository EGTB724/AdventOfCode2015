def main():
    lines = []
    with open('day14.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    reindeers = []
    for line in lines:
        tmp = line.split()
        rate = int(tmp[3])
        duration = int(tmp[6])
        rest = int(tmp[13])

        reindeers.append(Reindeer(rate, duration, rest))

    distance = [0 for i in range(len(reindeers))]
    points = [0 for i in range(len(reindeers))]


    for elapsedTime in range(0, 2503):
        for index, reindeer in enumerate(reindeers):
            if elapsedTime % reindeer.total < reindeer.duration:
                distance[index] += reindeer.rate

        furthest = max(distance)
        for index, reindeer in enumerate(reindeers):
            if distance[index] == furthest:
                points[index] += 1



    print(points)
    print(max(points))

class Reindeer:
    def __init__(self, rate, duration, rest):
        self.rate = rate
        self.duration = duration
        self.rest = rest
        self.total = duration + rest

if __name__ == "__main__":
    main()
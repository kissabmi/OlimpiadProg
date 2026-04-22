import bisect


def solve():
    try:
        with open("trains.in", "r") as f:
            lines = f.read().split()
    except FileNotFoundError:
        return

    if not lines:
        return

    L = int(lines[0])
    N = int(lines[1])

    times = []
    speeds = []
    idx = 2
    for _ in range(N):
        times.append(int(lines[idx]))
        speeds.append(int(lines[idx + 1]))
        idx += 2

    # Прекалькуляция
    cum_times = [0.0] * (N + 1)
    cum_dists = [0.0] * (N + 1)
    for i in range(N):
        cum_times[i + 1] = cum_times[i] + times[i]
        cum_dists[i + 1] = cum_dists[i] + times[i] * speeds[i]

    total_time = cum_times[N]
    total_dist = cum_dists[N]

    def get_pos(t):
        if t <= 0:
            return 0.0
        if t >= total_time:
            return total_dist

        # Быстрый поиск нужного отрезка пути
        idx = bisect.bisect_right(cum_times, t) - 1
        if idx < 0:
            idx = 0
        if idx >= N:
            idx = N - 1

        return cum_dists[idx] + (t - cum_times[idx]) * speeds[idx]

    def check(delta_t):
        # Если второй поезд выезжает после того, как первый уже прибыл на конечную - это 100% безопасно
        if delta_t >= total_time:
            return True

        # Собираем точки излома функции расстояния (где меняются скорости обоих поездов)
        test_points = [delta_t, total_time]
        for ct in cum_times:
            if delta_t < ct < total_time:
                test_points.append(ct)
            if delta_t < ct + delta_t < total_time:
                test_points.append(ct + delta_t)

        # Проверяем расстояние строго в узловых точках
        for t in test_points:
            dist = get_pos(t) - get_pos(t - delta_t)
            # Строгое неравенство безопаснее для бинарного поиска и обхода погрешностей float
            if dist < L:
                return False
        return True

    # Бинарный поиск
    # Максимально необходимый интервал — это время полного прохождения ветки (total_time)
    low = 0.0
    high = float(total_time)

    for _ in range(100):
        mid = (low + high) / 2.0
        if check(mid):
            high = mid
        else:
            low = mid

    with open("trains.out", "w") as f:
        f.write("{:.6f}\n".format(high))


if __name__ == "__main__":
    solve()

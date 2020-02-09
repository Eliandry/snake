states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "са", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()
while states_needed:
    best = None
    states_covered = set()  # все штаты обслуживаемые текущей станцией
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # пересечение.множество штатов, не входящих в покрытие, которые покрываются текущей станuией
        if len(covered) > len(states_covered):  # проверяем, покрывает ли эта станция больше штатов, чем текущая станция
            best = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best)
print(final_stations)

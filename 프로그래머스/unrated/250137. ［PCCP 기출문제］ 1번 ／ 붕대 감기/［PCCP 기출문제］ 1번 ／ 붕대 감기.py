def solution(bandage, health, attacks):
    end_time = attacks[-1][0]
    max_health = health
    attacks = { attack[0]:attack[1] for attack in attacks}
    success_time = 1

    for time in range(1,end_time+1):
        if time in attacks:
            success_time = 1
            health -= attacks[time]
            if health <= 0:
                return -1
        else:
            health = min(max_health,health+bandage[1])
            if success_time == bandage[0]:
                health = min(max_health,health+bandage[2])
                success_time = 1
            else:
                success_time += 1

    return health

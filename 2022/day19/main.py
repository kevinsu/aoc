import re
import sys
from common.perf import profiler


class State:
    def __init__(self):
        self.minutes = 0
        self.ore_count = 0
        self.clay_count = 0
        self.geode_count = 0
        self.obsidian_count = 0
        self.ore_bots = 1
        self.clay_bots = 0
        self.obsidian_bots = 0
        self.geode_bots = 0
        self.path = []

    def __str__(self):
        return f'min: {self.minutes}, ore_count: {self.ore_count}, clay_count: {self.clay_count}, obsidian_count: {self.obsidian_count}, geode_count: {self.geode_count}, ore_bots: {self.ore_bots}, clay_bots: {self.clay_bots}, obsidian_bots: {self.obsidian_bots}, geode_bots: {self.geode_bots}'

    def collect(self):
        self.ore_count += self.ore_bots
        self.clay_count += self.clay_bots
        self.geode_count += self.geode_bots
        self.obsidian_count += self.obsidian_bots

    def copy(self):
        state = State()
        state.minutes = self.minutes
        state.ore_count = self.ore_count
        state.clay_count = self.clay_count
        state.obsidian_count = self.obsidian_count
        state.geode_count = self.geode_count
        state.ore_bots = self.ore_bots
        state.clay_bots = self.clay_bots
        state.obsidian_bots = self.obsidian_bots
        state.geode_bots = self.geode_bots
        state.path = self.path.copy()
        return state

    def can_build_ore_bot(self, ore_cost, max_ore_cost, limit):
        # Time remaining * ore_bots + ore_count > time remaining * ore_cost
        time_remaining = limit - self.minutes - 1
        #print(time_remaining, str(self))
        #print(self.ore_count >= ore_cost, self.ore_bots <= 4, (time_remaining * self.ore_bots + self.ore_count < time_remaining * 4))        
        return self.ore_count >= ore_cost and self.ore_bots <= max_ore_cost and (time_remaining * self.ore_bots + self.ore_count < time_remaining * max_ore_cost)

    def can_build_clay_bot(self, ore_cost, max_clay_cost, limit):
        time_remaining = limit - self.minutes - 1
        return self.ore_count >= ore_cost and self.clay_bots <= max_clay_cost and (time_remaining * self.clay_bots + self.clay_count < time_remaining * max_clay_cost)

    def can_build_obsidian_bot(self, ore_cost, clay_cost, limit):
        return self.ore_count >= ore_cost and self.clay_count >= clay_cost

    def can_build_geode_bot(self, ore_cost, obsidian_cost):
        return self.ore_count >= ore_cost and self.obsidian_count >= obsidian_cost


class Manager:
    def __init__(self, blueprint):
        matches = re.findall('\d+', blueprint)
        self.index = int(matches[0])
        self.ore_ore_cost = int(matches[1])
        self.clay_ore_cost = int(matches[2])
        self.obsidian_ore_cost = int(matches[3])
        self.obsidian_clay_cost = int(matches[4])
        self.geode_ore_cost = int(matches[5])
        self.geode_obsidian_cost = int(matches[6])
        self.max_ore_cost = max(self.ore_ore_cost, self.clay_ore_cost)

    def get_max_geodes(self, limit):
        queue = [State()]
        max_geodes = 0
        path = []
        visited = set()
        while queue:
            state = queue.pop()
            if str(state) in visited:
                continue
            visited.add(str(state))
            time_remaining = limit - state.minutes
            max_extra_geodes = (time_remaining - 1) * time_remaining / 2
            if state.geode_count + time_remaining * state.geode_bots + max_extra_geodes < max_geodes:
                continue
            if state.minutes == limit:
                max_geodes = max(max_geodes, state.geode_count)
                path = state.path
                continue
            state_copy = state.copy()
            state_copy.path.append(str(state) + ' wait')            
            state_copy.collect()
            state_copy.minutes += 1
            queue.append(state_copy)
            if state.can_build_geode_bot(self.geode_ore_cost, self.geode_obsidian_cost):
                state_copy = state.copy()
                state_copy.path.append(str(state_copy) + ' geode')
                state_copy.ore_count -= self.geode_ore_cost
                state_copy.obsidian_count -= self.geode_obsidian_cost
                state_copy.collect()
                state_copy.geode_bots += 1                
                state_copy.minutes += 1
                queue.append(state_copy)
            if state.can_build_obsidian_bot(self.obsidian_ore_cost, self.obsidian_clay_cost, limit):
                state_copy = state.copy()
                state_copy.path.append(str(state_copy) + ' obsidian')                
                state_copy.ore_count -= self.obsidian_ore_cost
                state_copy.clay_count -= self.obsidian_clay_cost
                state_copy.collect()
                state_copy.obsidian_bots += 1                
                state_copy.minutes += 1
                queue.append(state_copy)
            if state.can_build_clay_bot(self.clay_ore_cost, self.obsidian_clay_cost, limit):
                state_copy = state.copy()
                state_copy.path.append(str(state_copy) + ' clay')
                state_copy.ore_count -= self.clay_ore_cost
                state_copy.collect()
                state_copy.clay_bots += 1                
                state_copy.minutes += 1
                queue.append(state_copy)
            if state.can_build_ore_bot(self.ore_ore_cost, self.max_ore_cost, limit):
                state_copy = state.copy()
                state_copy.path.append(str(state_copy) + ' ore')
                state_copy.ore_count -= self.ore_ore_cost
                state_copy.collect()
                state_copy.ore_bots += 1                
                state_copy.minutes += 1                
                queue.append(state_copy)
            
        #print("PATH")
        #for s in path:
        #    print(s)        
        return max_geodes


def part1(managers):
    sum = 0
    for manager in managers:
        max_geodes = manager.get_max_geodes(24)
        print(manager.index, max_geodes)
        sum += manager.index * max_geodes
    return sum

def part2(managers):
    return managers[0].get_max_geodes(32) * managers[1].get_max_geodes(32) * managers[2].get_max_geodes(32)

@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    managers = []
    for line in file.readlines():
        managers.append(Manager(line))
    
    #print(part1(managers))
    print(part2(managers))


if __name__ == "__main__":
    main(sys.argv[1:])

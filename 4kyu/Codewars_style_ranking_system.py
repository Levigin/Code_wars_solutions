class User:

    def __init__(self, rank=-8):
        self.rank = rank
        self.progress = 0
        self.max_rank = False

    def inc_progress(self, rank_solved_task):
        if rank_solved_task < -8 or rank_solved_task > 8 or rank_solved_task == 0:
            raise Exception('error')

        if self.rank == 8:
            self.progress = 0
            return

        diff = rank_solved_task - self.rank

        if rank_solved_task > 0 > self.rank:
            diff -= 1
        elif rank_solved_task < 0 < self.rank:
            diff += 1

        if diff == -1:
            self.progress += 1
        elif diff == 0:
            self.progress += 3
        elif diff < -1:
            pass
        else:
            self.progress += 10 * (diff ** 2)

        print(f'progress = {self.progress}')

        if self.progress > 99:
            temporal_rank = self.progress // 100
            self.progress = self.progress % 100

            if self.rank < 0 < self.rank + temporal_rank:
                self.rank += 1

            if temporal_rank + self.rank > 7:
                self.rank = 8
                self.progress = 0
                self.max_rank = True
                return

            self.rank += temporal_rank

            if self.rank == 0:
                self.rank += 1


user = User()
print(f'before rank = {user.rank}')
print(f'before progress = {user.progress}')
user.inc_progress(-2)
print(f'after rank = {user.rank}')
print(f'after progress = {user.progress}')
print()
print(f'before rank = {user.rank}')
print(f'before progress = {user.progress}')
user.inc_progress(7)
print(f'after rank = {user.rank}')
print(f'after progress = {user.progress}')
print()
# print(f'before rank = {user.rank}')
# print(f'before progress = {user.progress}')
# user.inc_progress(4)
# print(f'after rank = {user.rank}')
# print(f'after progress = {user.progress}')

# print(f'before rank = {user.rank}')
# print(f'before progress = {user.progress}')
# user.inc_progress(2)
# print(f'after rank = {user.rank}')
# print(f'after progress = {user.progress}')

# user.inc_progress(-9)
# user.inc_progress(0)
# user.inc_progress(-9)

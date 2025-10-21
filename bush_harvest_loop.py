for i in range(get_world_size(), 99):
	for j in range(get_world_size()):
		harvest()
		plant(Entities.Bush)
		move(North)
	move(East)
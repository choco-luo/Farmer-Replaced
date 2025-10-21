for i in range(get_world_size(), 99):
	for j in range(get_world_size()):
		#在每个地块上翻转一次
		harvest()
		plant(Entities.Bush)
		move(North)
	move(East)
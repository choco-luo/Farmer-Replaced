# 讓機器在小麥可以採收時才執行動作(此動作剛好1秒間隔所以可以邊移動邊採收)
# 當前對應進度: Save0_backup149
while True:
	if can_harvest():
		harvest()
		move(North)
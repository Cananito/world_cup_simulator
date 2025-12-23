CFLAGS=-Wall -Wextra -Werror

build: world_cup_simulator

run: world_cup_simulator
	./world_cup_simulator

world_cup_simulator: main.o
	$(CC) $(CFLAGS) main.o -o world_cup_simulator

main.o: main.c
	$(CC) $(CFLAGS) -c main.c -o main.o

clean:
	rm -f *.o
	rm -f world_cup_simulator
	rm -rf world_cup_simulator.dSYM/

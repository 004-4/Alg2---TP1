CC=g++
CFLAGS=-I. -Wall -Wextra -Werror -std=c++17 -pedantic -O2

main:
	$(CC) alg2.cpp -o tp1 $(CFLAGS)

clean:
	rm -f *.o main

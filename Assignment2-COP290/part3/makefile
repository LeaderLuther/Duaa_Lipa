list:
	gcc -o obj/list_test test/list_test.c src/list.c
	./obj/list_test  -I include/
doc:
	doxygen Doxyfile
clean:
	rm -f obj/*
	rm -fr doc/*

files = $(shell ls data | sed "s/^/data\//")

test:
	gcc -g3 -o obj/main.o test/main_pthreads.c src/list.c src/hm.c src/mythread.c -I include/ -pthread
	./obj/main.o $(files)

speed:
	gcc -g3 -o obj/speed_test.o test/speed_test.c src/list.c src/hm.c src/mythread.c -I include/ -pthread
	./obj/speed_test.o $(files)

.PHONY: all test clean

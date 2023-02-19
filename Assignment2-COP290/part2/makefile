files = $(shell ls data | sed "s/^/data\//")

main:
	gcc -o obj/main test/main.c src/list.c src/hm.c src/mythread.c 
	./obj/main $(files)

speed:
	gcc -o obj/speed_test test/speed_test.c src/list.c src/hm.c src/mythread.c 
	./obj/speed_test $(files)


list:
	gcc -o obj/list_test test/list_test.c src/list.c
	./obj/list_test

hashmap:
	gcc -o obj/hashmap test/hashmap_test.c src/hm.c src/list.c src/mythread.c
	./obj/hashmap
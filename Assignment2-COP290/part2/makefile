number = $(shell ls data| wc -l)
files = $(shell ls data)

main:
	gcc -o obj/main test/main.c src/list.c src/hm.c src/mythread.c 
	./obj/main $(number) $(files)

list:
	gcc -o obj/list_test test/list_test.c src/list.c
	./obj/list_test

mythread:
	gcc -o obj/mythread test/mythread_test.c src/mythread.c src/list.c
	./obj/mythread
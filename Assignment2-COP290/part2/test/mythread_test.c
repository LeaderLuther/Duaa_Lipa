#include <stdio.h>
#include "../include/mythread.h"
#include "../include/list.h"

void func(void* n){
    int* n_point = (int*) n;
    
    for (int i=0; i<*n_point; i++) {
    printf("%s %d", "Called with ", *n_point);
    printf("%d\n", *n_point+i);
    // mythread_yield();
    }
}

int main() {
    mythread_init();
    int args[2] = {4, 5};

    mythread_create(func, args);
    mythread_create(func, args+sizeof(int));

    print_thread_list();
    mythread_join();
    return 0;
}
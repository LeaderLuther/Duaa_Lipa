#include <stdio.h>
#include "../include/mythread.h"
#include "../include/list.h"

void func(void* n){
    int* n_point = (int*) n;
    printf("%d", *n_point);
}

int main() {
    mythread_init();
    int args[2] = {4, 5};

    mythread_create(func, args);
    mythread_create(func, args+sizeof(int));
    return 0;
}
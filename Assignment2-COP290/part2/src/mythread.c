#include <stdio.h>
#include <stdlib.h>
#include <ucontext.h>
#include "../include/list.h"

struct list threads_list;

void mythread_init() {
    threads_list = *list_new();
}

ucontext_t* mythread_create(void func(void*), void* arg) {
    char* stack1 = malloc(4096*sizeof(char));
    ucontext_t* new_context = malloc(sizeof(ucontext_t));
    
    getcontext(new_context);

    new_context->uc_stack.ss_sp = stack1;
    new_context->uc_stack.ss_size = sizeof(stack1);

    makecontext(new_context,(void (*)(void)) func, 1, arg);
    printf("%s", "Context created\n");

    if (!threads_list.head){
        return list_add(&threads_list, new_context)->data;
    }
    else {
        ucontext_t* last_context  = (ucontext_t*) threads_list.tail->data;
        new_context->uc_link = last_context;
        return list_add(&threads_list, new_context)->data;
    }
}

void mythread_join() {
    return;
}

void mythread_yield() {
    return;
}
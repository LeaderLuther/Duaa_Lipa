#ifndef THREAD_H
#define THREAD_H

#include<stdio.h>
#include<stdlib.h>
#include<ucontext.h>
#include<signal.h>
#include<sys/time.h>
#include<unistd.h>
#include "../include/list.h"


void mythread_init();
ucontext_t* mythread_create(void func(void*), void* arg);
void mythread_join(); 
void mythread_yield();  
void print_thread_list(); 

struct lock {
	ucontext_t* ctx;
};
struct lock* lock_new();
void lock_acquire(struct lock* lk);
int lock_release(struct lock* lk);

#endif

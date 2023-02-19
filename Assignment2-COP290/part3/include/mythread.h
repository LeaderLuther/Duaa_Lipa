#ifndef THREAD_H
#define THREAD_H

#include<stdio.h>
#include<stdlib.h>
#include<ucontext.h>
#include<signal.h>
#include<sys/time.h>
#include<unistd.h>


/*! \file mythread.h
    \brief Implementation of threads using contexts
    
    Contains functions related to running and managing threads to be ran concurrently using
    context from ucontext library.
*/

/*! \fn void mythread_init()
    \brief Initialize threads list.
    
	Creates and allocates memory for an empty list that is global to the mythread functions
*/

/*! \fn ucontext_t* mythread_create(void func(void*), void* arg)
    \brief Create a new thread
    
	Creates a new thread by creating a new context and adding it to the threads list.
    Returns pointer to the newly created context 
    \param func Pointer to the function/routine that needs to be ran in this thread
	\param arg Pointer to the arguments that needs to be passed to the function/routine
*/

/*! \fn void mythread_join()
    \brief Waits for other thread to complete. It is used in case of dependent threads.
    
	Starts running all the threads and ends only when all current threads are completed
*/

/*! \fn void mythread_yield()
    \brief Performs context switching
    
	Switches thread from current thread to the next thread in threads list in a cyclic form,
    i.e., if the current thread is last in the list, switches to first thread in list, otherwise
    switches to next context 
*/

/*! \struct lock
    \brief Lock struct which includes a pointer the context which has acquired this lock

    \param ctx Pointer to the context which has acquired this lock. Is NULL if lock is released
*/

/*! \fn struct lock* lock_new()
    \brief Initializes a lock struct.
    
	Creates and allocates memory for a new lock struct. Returns the newly created lock
*/

/*! \fn void lock_acquire(struct lock* lk)
    \brief Attempts to acquire the lock, yields if already acquired
    
	If the passed lock is not acquired by any other thread, acquires this lock by pointing lock context
    to current context. If it is aquired by another thread, then yields to other threads.
	\param lk Pointer to the lock that needs to be accessed
*/

/*! \fn int lock_release(struct lock* lk)
    \brief  Releases the lock
    
	Releases passed lock to be used by other threads. Sets context pointed by lock to NULL
	\param lk Pointer to the lock that needs to be accessed
*/


void mythread_init();
void* mythread_create(void func(void*), void* arg);
void mythread_join();
void mythread_yield();

struct lock {
	void* c;
};
struct lock* lock_new();
void lock_acquire(struct lock* lk);
int lock_release(struct lock* lk);

#endif

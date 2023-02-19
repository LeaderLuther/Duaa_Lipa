#ifndef THREAD_H
#define THREAD_H

#include<stdio.h>
#include<stdlib.h>
#include<ucontext.h>
#include<signal.h>
#include<sys/time.h>
#include<unistd.h>


/*! \file mythread.h
    \brief A Documented file.
    
    Details.
*/

/*! \fn void mythread_init()
    \brief nitialize threads list.
    
	Details.
*/

/*! \fn ucontext_t* mythread_create(void func(void*), void* arg)
    \brief Create a new thread
    
	Details.
    \param func
	\param arg
*/

/*! \fn void mythread_join()
    \brief Waits for other thread to complete. It is used in case of dependent threads.
    
	Details.
*/

/*! \fn void mythread_yield()
    \brief Perform context switching here
    
	Details.
*/

/*! \fn void print_thread_list()
    \brief brief
    
	Details.
*/

/*! \struct lock
    \brief It is a struct.

    A struct for storing addresses of context.
    \param ctx Address of context.
*/

/*! \fn struct lock* lock_new()
    \brief Return an initialized lock object
    
	Details.
*/

/*! \fn void lock_acquire(struct lock* lk)
    \brief Set lock. Yield if lock is acquired by some other thread.
    
	Details.
	\param lk
*/

/*! \fn int lock_release(struct lock* lk)
    \brief  Release lock
    
	Details.
	\param lk
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

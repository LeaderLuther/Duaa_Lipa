#define _XOPEN_SOURCE 600
#include <stdio.h>
#include <stdlib.h>
//#include <sys/ucontext.h>
#include <ucontext.h>
#include "../include/list.h"

#define MEM 4096*1024

static struct list* threads_list;      // A list that stores all the pending/unfinished threads
static ucontext_t* ctx_main;          // This will store where current thread should go back to
static struct listentry* curr_ctx_entry = NULL;    // The listentry of the context which is currently running

void mythread_init() {
    threads_list = list_new();  // Initializes memory for a list of different threads
    ctx_main = malloc(sizeof(ucontext_t));
    getcontext(ctx_main);       // Initializes main_ctx
}

ucontext_t* mythread_create(void func(void*), void* arg) {
    char* stack1 = malloc(MEM*sizeof(char));    // Stack of size MEM for the new context
    ucontext_t* new_ctx = malloc(sizeof(ucontext_t));   // New context object, to be added to threadslist
    
    getcontext(new_ctx);        // Initializing

    new_ctx->uc_stack.ss_sp = stack1;
    new_ctx->uc_stack.ss_size = MEM*sizeof(char);     // Assigning new stack to the new context
    new_ctx->uc_link = ctx_main;                     // When finished, context returns to wherever ctx_main is

    makecontext(new_ctx,(void (*)(void)) func, 1, arg); // Creates new context which will execute given functipn with givenargs
    
    return list_add(threads_list, (void*) new_ctx)->data;      // Add context pointer to list and return
}

void mythread_join() {
    if (is_empty(threads_list)) return;     // If no threads to run, simply return

    curr_ctx_entry = threads_list->head;    // Will start running the first context in list
    while (!is_empty(threads_list)) {
        curr_ctx_entry = threads_list->head;    // Will start running the first context in list
        swapcontext(ctx_main, (ucontext_t*) curr_ctx_entry -> data);  // Start the first context
        struct listentry* x = curr_ctx_entry;

        list_rm(threads_list, x);      // Once a context finishies, delete the node of that context
                    
    }
    return;         // Reaches here when all threads are finished and list is empty
}

void mythread_yield() {
    // If threadA is running currently, curr_ctx_entry points to A
    // Need to change running thread and curr_ctx_entry to next node B
    if (curr_ctx_entry->next == NULL) curr_ctx_entry = threads_list->head;  // Set the next context to run
    else curr_ctx_entry = curr_ctx_entry -> next;                          // In a cyclic manner
    // Now curr_ctx_entry points to B but thread A is running still
    swapcontext((ucontext_t*)curr_ctx_entry->prev->data, (ucontext_t*)curr_ctx_entry->data);
    // Store current context in context of thread A, and start running thread B
    // listenty of thread A is prev of listentry of thread B
    return;
}

void print_thread_list() {
    if (is_empty(threads_list)) return;

    struct listentry* cur = threads_list->head;

    while (cur != NULL) {
        cur = cur->next;
    }
}
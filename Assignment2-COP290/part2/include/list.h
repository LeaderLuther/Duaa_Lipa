#ifndef LIST_H
#define LIST_H

/** @brief Creates hashmap in heap.

    A hashmap is created in heap, with functions create, put, get, iterator and locks for threading
    @author OM DEHLAN, SARWAGYA PRASAD, AMAIYA SINGHAL
    @date Feb 2023
    */

/*! \struct list
    \brief It is a struct 

    A struct for storing addresses of key, value pair.
*/
struct list {
	struct listentry* head;
	struct listentry* tail;
};

struct listentry {
	void *data;
	struct listentry *prev;
	struct listentry *next;
};

void list_rm(struct list* l, struct listentry* e);    // Remove an item from the list
struct listentry* list_add(struct list* l, void* data);  // Add an item to the list
struct list* list_new();  // Return an initialized list
int is_empty(struct list* l);  // Check if list is empty or not
#endif

#ifndef LIST_H
#define LIST_H
#include <stdlib.h>

struct list {
	struct listentry* head;
	struct listentry* tail;
};

struct listentry {
	void *data;
	struct listentry *prev;
	struct listentry *next;
};

void list_rm(struct list* l, struct listentry* e){ // Remove an item from the list
	
	struct listentry* p = l -> head; //initialise p as the head of the list
	
	if (p == e){ // if head of the list is equal to e
		
		l -> head = e -> next; // set head of the tail equal to e -> next
		
		if (l -> head == NULL){ // if the list is empty after removal of e
			l -> tail = NULL; // set tail also as NULL
		}else{
			(l -> head) -> prev = NULL; // Else set prev of head as NULL
		}
		
	}else{ // if head of the list is not e
		
		while(p != l -> tail){ //while p is not the tail of the list
			if (p -> next == e){ // if p -> next is e
				p -> next = e -> next; // set p -> next as e -> next
				(p -> next) -> prev = p; // set as (p -> next) -> prev as p
				break; // break out of the loop
			}else p = p -> next; // else set p as p -> next
		}
		// Reaching here means p is now equal to the tail of the list
		// All elements of the list have been checked and e was not found
	}
	
	free(e); // Free the space
}    

struct listentry* list_add(struct list* l, void* data){ // Add an item to the list
	
	struct listentry *p = malloc(sizeof(struct listentry)); // Initialise a list entry element
	
	if (l -> head){ //If list is non empty
		
		p -> data = data; // p -> data is set to data
		(l -> tail) -> next = p; // Next of the Tail of the list is set to p
		p -> prev = l -> tail; // Prev of p is set to the old tail
		p -> next = NULL; // Next of p is NULL as it is the last element
		l -> tail = p; // Updating tail to new element
		
	}else{
		
		p -> data = data; // p -> data is set to data
		p -> prev = NULL; // p -> prev is NULL as only element of list
		p -> next = NULL; // p -> next is NULL as only element of list
		l -> head = p; // Head of list is now p
		l -> tail = p; // Tail of list is now p
		
	}
	
	return p;
}
  
struct list* list_new(){ // Return an initialized list

	struct list* l = malloc(sizeof(struct list)); // Declaring a new list
	
	l -> head = NULL; // Set head as NULL
	l -> tail = NULL; // Set tail as NULL
	return l;
}  

int is_empty(struct list* l){ // Check if list is empty or not
	
	if (l -> head == NULL) return 1; // If head is NULL then list is empty
	else return 0;
}  

#endif


#ifndef LIST_H
#define LIST_H


/*! \file list.h
    \brief Header file for doubly linked list.
    
    Contains implementation of a doubly linked list and related functions.
*/

/*! \struct list
    \brief The list struct corresponding to a doubly linked lists.

    \param head Pointer to the first listentry node
    \param tail Pointer to the last listentry node
*/

/*! \struct listentry
    \brief The listentry struct contains data and pointers to adjacent nodes.

    \param data Pointer to the data in the listentry node
    \param next Pointer to the next listentry in list
    \param prev Pointer to the previous listentry in list
*/

/*! \fn void list_rm(struct list* l, struct listentry* e)
    \brief Removes a listentry node from list
    
	Deletes a listentry node from the list and frees it's memory
    \param l Pointer to the list which needs to be accessed
	\param e Pointer to the listentry node which needs to be deleted
*/

/*! \fn struct listentry* list_add(struct list* l, void* data)
    \brief Adds a new listentry node at the tail of list
    
	Creates and allocates memory for a new listentry node containing the passed data,
    and adds it to the end of the list. Returns pointer to the newly added listentry node.
    \param l Pointer to the list which needs to be accessed
	\param data Pointer to the data which needs to be inserted
*/

/*! \fn struct list* list_new()
    \brief Initializes a new list.
    
	Creates and allocates memory to a new empty list. Returns pointer to the newly created list
*/

/*! \fn int is_empty(struct list* l)
    \brief Check if list is empty or not.
    
	Returns 1 if list is empty, 0 otherwise
    \param l Pointer to the list which needs to be accessed
*/


struct list {
	struct listentry *head; ///< head of the list
	struct listentry *tail; ///< tail of the list
};

struct listentry {
	void *data;		///< data for this entry
	struct listentry *prev; ///< previous entry
	struct listentry *next; ///< next entry
};

void list_rm(struct list *l, struct listentry *e);		// Remove an item from the list
struct listentry *list_add(struct list *l, void *data); 	// Add an item to the list
struct list *list_new();					// Return an initialized list
int is_empty(struct list *l);					// Check if list is empty or not
#endif

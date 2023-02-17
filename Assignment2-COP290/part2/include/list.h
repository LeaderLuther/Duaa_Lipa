#ifndef LIST_H
#define LIST_H

/*! \file list.h
    \brief A Documented file.
    
    Details.
*/

/*! \struct list
    \brief It is a struct .

    A struct for storing addresses of key, value pair.
*/

/*! \struct listentry
    \brief It is a struct.

    A struct for storing addresses of node, next node and previous node.
*/

/*! \fn void list_rm(struct list* l, struct listentry* e)
    \brief Remove an item from the list.
    
	Details.
    \param l
	\param e
*/

/*! \fn struct listentry* list_add(struct list* l, void* data)
    \brief Add an item to the list.
    
	Details.
    \param l
	\param data
*/

/*! \fn struct list* list_new()
    \brief Return an initialized list.
    
	Details.
*/

/*! \fn int is_empty(struct list* l)
    \brief Check if list is empty or not.
    
	Details.
    \param l

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

void list_rm(struct list* l, struct listentry* e);    
struct listentry* list_add(struct list* l, void* data);   
struct list* list_new(); 
int is_empty(struct list* l); 
#endif

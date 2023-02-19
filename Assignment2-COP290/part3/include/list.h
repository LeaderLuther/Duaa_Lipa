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

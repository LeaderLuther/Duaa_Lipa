#include "mythread.h"
#include "list.h"

/*! \def SZ
    \brief used for memory allocation
*/
#define SZ 4096

/** @brief Creates hashmap in heap.

    A hashmap is created in heap, with functions create, put, get, iterator and locks for threading
    @author OM DEHLAN, SARWAGYA PRASAD, AMAIYA SINGHAL
    @date Feb 2023
    */

/*! \struct hashmap_element_s
    \brief It is a struct 

    A struct for storing addresses of key, value pair.
    \param key Address of key string
    \param data Address of data
*/
struct hashmap_element_s {
  char *key; 
  void *data; 
};


/*! \struct hashmap_s
    \brief It is a struct 

    A struct for storing address of struct list and struct lock.
    \param table Address of struct list
    \param lk Address of struct lock
*/
struct hashmap_s {
  struct list* table[SZ]; 
  struct lock* lk[SZ]; 
};

/*! \fn hashmap_create
    \brief Initialize a hashmap

    Initializes a hashmap and returns 0 on completion.
*/
int hashmap_create(struct hashmap_s *const out_hashmap);

/*! \fn hashmap_put
    \brief Set value of the key as data in hashmap

    Hashes key and stores key, value pair, where value is data, also resolving conflicts, returns 0 at completion
*/
int hashmap_put(struct hashmap_s *const hashmap, const char* key, void* data); 

/*! \fn hashmap_get
    \brief Fetch value of a key from hashmap

    Returns the address of the value of the key stored in the hashmap or returns NULL when key not found
*/
void* hashmap_get(struct hashmap_s *const hashmap, const char* key); 

/*! \fn hashmap_iterator
    \brief Execute argument function on each key-value pair in hashmap

    Executes the argument function on each key-value pair in hashmap
*/
void hashmap_iterator(struct hashmap_s* const hashmap, 
                        int (*f)(struct hashmap_element_s *const)); 

int acquire_bucket(struct hashmap_s *const hashmap, const char* key);   // Acquire lock on a hashmap slot
int release_bucket(struct hashmap_s *const hashmap, const char* key);   // Release acquired lock

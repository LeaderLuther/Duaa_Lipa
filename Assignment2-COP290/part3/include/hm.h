#include "mythread.h"
#include "list.h"


/*! \file hm.h
    \brief A header file containing implementation of Hashmap compatible with threads and locks.
    
    This file contains a struct and related functions to use a hashmap. It also includes acquire_bucket
    and release_bucket functions to be used when multiple threads use a hashmap, implementing locks for
    each list in the hashmap.
*/

/*! \def SZ
    \brief Macro for defining hashmap Size
*/

/*! \struct hashmap_element_s
    \brief A struct containing a key-value pair

    A struct for storing addresses of key, value pair.
    \param key Address of key string.
    \param data Address of data.
*/

/*! \struct hashmap_s
    \brief It defines a hashmap struct.

    Hashmap struct contains two arrays: 
        table - containing SZ linked lists containing the key-value pairs hashmap_elemnt_s.
        lk - Array of length SZ containing locks for each linked list in table.

    \param table Address of struct list.
    \param lk Address of struct lock.
*/

/*! \fn int hashmap_create(struct hashmap_s *const out_hashmap)
    \brief Initialize a hashmap.
    
    Initializes a hashmap by allocating memory for each linked list in table and lock in lk.
    Returns 0 on successful creation, 1 if an error is encountered.
    \param out_hashmap Stores and returns address of hashmap here.
*/

/*! \fn int hashmap_put(struct hashmap_s *const hashmap, const char *key,void *data)
    \brief Set value of the key as data in hashmap.

    If key already exists then updates the key-value pair to new data,
    If key does not exist, creates a new listentry for the key-value pair.
    returns 0 at completion.

    \param hashmap Pointer to the hashmap.
    \param key key string of the pair.
    \param data Pointer to the data value of the pair.
*/

/*! \fn void* hashmap_get(struct hashmap_s *const hashmap, const char *key)
    \brief Fetch value of a key from hashmap.

    Returns a pointer to the value of the data corresponding to key passed stored in the hashmap 
    or returns NULL when key not found.
    \param hashmap Pointer to hashmap which needs to be accessed
    \param key Key string which is to be searched
*/

/*! \fn void hashmap_iterator(struct hashmap_s* const hashmap, int (*f)(struct hashmap_element_s *const))
    \brief Execute argument function on each key-value pair in hashmap.

    Executes the argument function on each key-value pair in hashmap.
    \param hashmap Pointer to hashmap which needs to be accessed
    \param f Pointer to the function which needs to be executed for every pair
*/

/*! \fn int acquire_bucket(struct hashmap_s *const hashmap, const char *key)
    \brief Acquire lock on a hashmap slot.

    Sets the lock to point to the current thread, so that no other thread can
    access this particular bucket in hashmap
    \param hashmap Pointer to hashmap which needs to be accessed
    \param key Key string. Acquires lock of the bucket corresponding to this key
*/

/*! \fn int release_bucket(struct hashmap_s *const hashmap, const char *key)
    \brief Release acquired lock.

    Releases the lock by setting the context pointer to NULL, so that other threads
    can access this bucket.
    \param hashmap Pointer to hashmap which needs to be accessed
    \param key Key string. Releases lock of the bucket corresponding to this key
*/


#define SZ 4096

struct hashmap_element_s {
  char *key;
  void *data;
};

struct hashmap_s {
  struct list* table[SZ];
  struct lock* lk[SZ];
};


int hashmap_create(struct hashmap_s *const out_hashmap);
int hashmap_put(struct hashmap_s *const hashmap, const char* key, void* data);
void* hashmap_get(struct hashmap_s *const hashmap, const char* key);
void hashmap_iterator(struct hashmap_s* const hashmap, 
                        int (*f)(struct hashmap_element_s *const));

int acquire_bucket(struct hashmap_s *const hashmap, const char* key);
int release_bucket(struct hashmap_s *const hashmap, const char* key);
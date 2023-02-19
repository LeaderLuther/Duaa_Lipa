#include "mythread.h"
#include "list.h"


/*! \file hm.h
    \brief A Documented file.
    
    Details.
*/

/*! \def SZ
    \brief used for memory allocation.
*/

/*! \struct hashmap_element_s
    \brief It is a struct.

    A struct for storing addresses of key, value pair.
    \param key Address of key string.
    \param data Address of data.
*/

/*! \struct hashmap_s
    \brief It is a struct.

    A struct for storing address of struct list and struct lock.
    \param table Address of struct list.
    \param lk Address of struct lock.
*/

/*! \fn int hashmap_create(struct hashmap_s *const out_hashmap)
    \brief Initialize a hashmap.
    
    Initializes a hashmap and returns 0 on completion.
    \param out_hashmap Stores address of hashmap here.
*/

/*! \fn int hashmap_put(struct hashmap_s *const hashmap, const char *key,void *data)
    \brief Set value of the key as data in hashmap.

    Hashes key and stores key, value pair, where value is data, also resolving conflicts, returns 0 at completion.
    \param hashmap The address to the hashmap.
    \param key
    \param data
*/

/*! \fn void* hashmap_get(struct hashmap_s *const hashmap, const char *key)
    \brief Fetch value of a key from hashmap.

    Returns the address of the value of the key stored in the hashmap or returns NULL when key not found.
    \param hashmap d.
    \param key d.
*/

/*! \fn void hashmap_iterator(struct hashmap_s* const hashmap, int (*f)(struct hashmap_element_s *const))
    \brief Execute argument function on each key-value pair in hashmap.

    Executes the argument function on each key-value pair in hashmap.
    \param hashmap d.
    \param f d.
*/

/*! \fn int acquire_bucket(struct hashmap_s *const hashmap, const char *key)
    \brief Acquire lock on a hashmap slot.

    Details.
    \param hashmap d.
    \param key d.
*/

/*! \fn int release_bucket(struct hashmap_s *const hashmap, const char *key)
    \brief Release acquired lock.

    Details.
    \param hashmap d.
    \param key d.
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
//#include "mythread.h"
#include "list.h"
#define SZ 4096
#include <stdlib.h>
#include <string.h>


struct hashmap_element_s {
  const char *key; // I have changed this!
  void *data;
};

struct hashmap_s {
  struct list* table[SZ];
  // struct lock* lk[SZ];
};

int hash_func(const char* key){ // Hash function for the hash map
    int i = 0;
    int sum = 0;
    int prod = 0;
    
    while (*(key + i) != '\0'){
      if (i % 4 == 0){
        sum += prod;
        prod = *(key + i);
      }else{
        prod = prod*100 + *(key + i);
      }
      i++;
    }
    sum += prod;
    return (sum % SZ);
    
}

int hashmap_create(struct hashmap_s *const out_hashmap){ // Initialize a hashmap
  
  for (int i = 0; i < SZ; i++){ // For i from 0 to 4095 (size of table)
    *((out_hashmap -> table) + i) = list_new() ; // ith index of the table contains pointer to an empty list now
  }
  
  return 0; // No reason for this to fail, hence. no return -1
}   

int hashmap_put(struct hashmap_s *const hashmap, const char* key, void* data){ // Set value of the key as data in hashmap. You can use any method to resolve conflicts. Also write your own hashing function
  
  int hash_value = hash_func(key); // Calculating the hash value for the given key

  struct list* l = *((hashmap -> table) + hash_value); // Pointer to the linked list at the corresponding hash value in the table
  struct listentry *p = l -> head; // Pointer to the head of that list
  
  while(p){ // While p is not NULL
    struct hashmap_element_s* x = p -> data; // Pointer to the hashmap element at p
    if (strcmp(x -> key, key) == 0){ // If key of the hashmap element matches the argument key
      x -> data = data; // Update the data for the key
      return 0; // Successful update
    }
    p = p -> next; // p goes to p -> next
  }
  
  // Code comes here when the key doesn't already exist
  struct hashmap_element_s *t = malloc(sizeof(struct hashmap_element_s)); // Declaring the memory for the hashmap element
  t -> key = key; // t -> key is set as key
  t -> data = data; // t -> data is set as data
    
  list_add(*((hashmap -> table) + hash_value), t); // Append the hashmap element to the corresponding hash value list
  
  return 0; // Successful add
}
  
void* hashmap_get(struct hashmap_s *const hashmap, const char* key){ // Fetch value of a key from hashmap
  
  int hash_value = hash_func(key);
  
  struct list* l = *((hashmap -> table) + hash_value);
  struct listentry *p = l -> head;
  
  while(p){
    struct hashmap_element_s* t = p -> data;
    if (strcmp(t -> key, key) == 0) return (t -> data);
    p = p -> next;
  }
  
  int *z = malloc(sizeof(int));
  *z = -1;
  return z;
  
} 

void hashmap_iterator(struct hashmap_s* const hashmap, 
                        int (*f)(struct hashmap_element_s *const));  // Execute argument function on each key-value pair in hashmap

// int acquire_bucket(struct hashmap_s *const hashmap, const char* key);   // Acquire lock on a hashmap slot
// int release_bucket(struct  hashmap_s *const hashmap, const char* key);   // Release acquired lock

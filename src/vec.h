#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#define VEC_CAPACITY 8

typedef struct Vec {
    // Size of each item in the Vec
    size_t size;
    // Capacity of the current Vec buffer
    size_t capacity;
    // Length of the current buffer
    size_t length;
    // Memory buffer backing the Vec
    void* buff;
} Vec;

Vec* vec_create(size_t size) {
    // Allocate memory for 3 size_t variables (size, capacity, and
    // length), and then extra memory as flexible array member as the
    // Vec's memory buffer. 
    Vec* vec = (Vec *) malloc(sizeof(size_t) * 3 + size * VEC_CAPACITY);
    
    vec->size = size;
    vec->capacity = VEC_CAPACITY;
    vec->length = 0;
    memset(vec->buff, 0, VEC_CAPACITY);

    return vec;
}

void vec_destroy(Vec* vec) {
    free(vec);
}

void vec_push(Vec* vec, void* item) {
    if (vec == NULL) {
        fprintf(stderr, "error: vec_push() received null pointer for vec");
        abort();
    }

    if (vec->length == vec->capacity) {
        vec->capacity *= 2;
        vec->buff = realloc(vec->buff, vec->capacity * vec->size);
    }

    vec->length++;
    // TODO: Is casting to char* in the middle the right way to do this?
    void* offset = (char *) vec->buff + vec->length * vec->size;
    memcpy(offset, item, vec->size);
}

/**
 * Methods:
 *  - push()
 *  - pop()
 *  - length()
 *  - capacity()
 *  - size()
 * */

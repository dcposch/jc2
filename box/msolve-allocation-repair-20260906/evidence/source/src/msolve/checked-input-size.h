/* Checked file-input dimensions; no change to msolve's int32_t interfaces. */
#ifndef MSOLVE_CHECKED_INPUT_SIZE_H
#define MSOLVE_CHECKED_INPUT_SIZE_H
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

static inline void msolve_input_fail(const char *what)
{
    fprintf(stderr, "msolve input size/allocation error: %s\n", what);
    exit(EXIT_FAILURE);
}

/* The predicate does not allocate and leaves *out unchanged on failure. */
static inline int msolve_input_size_mul(size_t a, size_t b, size_t *out)
{
    if (a != 0 && b > SIZE_MAX / a)
        return 0;
    *out = a * b;
    return 1;
}

static inline size_t msolve_input_product(size_t a, size_t b)
{
    size_t result;
    if (!msolve_input_size_mul(a, b, &result))
        msolve_input_fail("size_t product overflow");
    return result;
}

static inline size_t msolve_input_array_bytes(size_t count, size_t width)
{
    size_t bytes = msolve_input_product(count, width);
    /* Keep pointer differences and the historical int64_t offsets valid. */
    if (bytes > PTRDIFF_MAX)
        msolve_input_fail("array exceeds PTRDIFF_MAX bytes");
    return bytes;
}

static inline size_t msolve_input_exponent_count(uint32_t terms, int32_t vars)
{
    if (vars <= 0)
        msolve_input_fail("nonpositive exponent dimension");
    size_t count = msolve_input_product((size_t)terms, (size_t)vars);
    (void)msolve_input_array_bytes(count, sizeof(int32_t));
    return count;
}

static inline size_t msolve_input_exponent_offset(int32_t index, uint32_t vars)
{
    if (index < 0 || vars > INT32_MAX)
        msolve_input_fail("invalid import exponent index/dimension");
    return msolve_input_exponent_count((uint32_t)index, (int32_t)vars);
}

static inline void *msolve_input_array(size_t count, size_t width, int clear)
{
    size_t bytes = msolve_input_array_bytes(count, width);
    /* The zero ideal may have zero entries; do not depend on malloc(0). */
    void *p = clear ? calloc(bytes ? count : 1, bytes ? width : 1)
                    : malloc(bytes ? bytes : 1);
    if (p == NULL)
        msolve_input_fail("allocator returned NULL");
    return p;
}

/* Q uses doubled signed-int32 coefficient positions; Fp uses single ones. */
static inline int msolve_input_terms_add(uint32_t a, uint32_t b,
                                        int rational, uint32_t *out)
{
    const uint32_t limit = rational ? INT32_MAX / 2 : INT32_MAX;
    if (a > limit || b > limit - a)
        return 0;
    *out = a + b;
    return 1;
}
#endif

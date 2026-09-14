/* Tiny direct controls: no request larger than 24 bytes reaches an allocator. */
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int fail_alloc;
static size_t allocations;
static void *test_malloc(size_t bytes)
{
    allocations++;
    if (bytes > 24) { fprintf(stderr, "UNEXPECTED_LARGE_ALLOCATION\n"); exit(99); }
    return fail_alloc ? NULL : malloc(bytes);
}
static void *test_calloc(size_t count, size_t width)
{
    allocations++;
    if (count > 24 || width > 24 || count * width > 24) {
        fprintf(stderr, "UNEXPECTED_LARGE_ALLOCATION\n"); exit(99);
    }
    return fail_alloc ? NULL : calloc(count, width);
}
#define malloc test_malloc
#define calloc test_calloc
#include "checked-input-size.h"
#undef malloc
#undef calloc
static void need(int ok, const char *why)
{
    if (!ok) { fprintf(stderr, "CHECK_FAILED %s\n", why); exit(2); }
}
int main(int argc, char **argv)
{
    need(argc == 2, "mode");
    if (!strcmp(argv[1], "overflow")) msolve_input_array(SIZE_MAX, 2, 0);
    else if (!strcmp(argv[1], "ptrdiff")) msolve_input_array((size_t)PTRDIFF_MAX+1, 1, 1);
    else if (!strcmp(argv[1], "exponent-overflow")) msolve_input_exponent_count(UINT32_MAX, INT32_MAX);
    else if (!strcmp(argv[1], "negative-dimension")) msolve_input_exponent_count(1, -1);
    else if (!strcmp(argv[1], "null-malloc")) { fail_alloc=1; msolve_input_array(2, 4, 0); }
    else if (!strcmp(argv[1], "null-calloc")) { fail_alloc=1; msolve_input_array(2, 4, 1); }
    else if (!strcmp(argv[1], "positive")) {
        size_t out=17;
        uint32_t total=19;
        need(sizeof(size_t)==8, "worker is 64-bit");
        need(msolve_input_size_mul(0, SIZE_MAX, &out) && out==0, "zero product");
        need(msolve_input_size_mul(SIZE_MAX, 1, &out) && out==SIZE_MAX, "size boundary");
        out=17;
        need(!msolve_input_size_mul(SIZE_MAX/2+1, 2, &out) && out==17, "overflow unchanged");
        need(msolve_input_size_mul(SIZE_MAX/4, 4, &out) && out==SIZE_MAX-3, "near boundary");
        size_t n=msolve_input_exponent_count(11299180U, 600);
        need(n==UINT64_C(6779508000), "full input exact count");
        need(msolve_input_array_bytes(n, sizeof(int32_t))==UINT64_C(27118032000), "full input exact bytes");
        uint32_t old=(uint32_t)11299180U*(uint32_t)600;
        need(old==UINT32_C(2484540704) && (size_t)old!=n, "old expression negative control");
        need(msolve_input_terms_add(INT32_MAX-1, 1, 0, &total) && total==INT32_MAX, "Fp count boundary");
        total=19;
        need(!msolve_input_terms_add(INT32_MAX, 1, 0, &total) && total==19, "Fp count overflow");
        need(msolve_input_terms_add(INT32_MAX/2-1, 1, 1, &total) && total==INT32_MAX/2, "Q count boundary");
        total=19;
        need(!msolve_input_terms_add(INT32_MAX/2, 1, 1, &total) && total==19, "Q double position overflow");
        need(!msolve_input_terms_add(UINT32_MAX, 1, 0, &total), "wrapped counter rejection");
        need(allocations==0, "all boundary checks allocate nothing");
        int32_t *a=msolve_input_array(6, sizeof(int32_t), 1);
        for(int i=0;i<6;i++) need(a[i]==0, "calloc preserved");
        free(a);
        void *b=msolve_input_array(0, sizeof(int32_t), 0); free(b);
        need(allocations==2, "tiny allocation count");
        puts("BOUNDARY_CONTROLS_PASS no allocation over 24 bytes");
        return 0;
    } else return 2;
    fprintf(stderr, "EXPECTED_REJECTION_DID_NOT_FIRE\n");
    return 3;
}

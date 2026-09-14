#include <stdint.h>
#include <stdio.h>
#include <stddef.h>
#include <inttypes.h>

int main(void) {
    /* These are the pinned source's actual typedefs.  No large allocation. */
    typedef uint32_t len_t;
    typedef len_t nelts_t;
    typedef int32_t nvars_t;
    nelts_t all_nterms = 11299180;
    nvars_t nvars = 600;
    size_t original_calloc_count = all_nterms * nvars;
    size_t widened_calloc_count = (size_t)all_nterms * nvars;
    _Static_assert(sizeof(nelts_t)==4 && sizeof(nvars_t)==4, "source type widths");
    printf("TERMS=%" PRIu32 " VARIABLES=%" PRId32 "\n",all_nterms,nvars);
    printf("ORIGINAL_COUNT=%zu WIDENED_COUNT=%zu\n",original_calloc_count,widened_calloc_count);
    printf("ORIGINAL_BYTES=%zu REQUIRED_BYTES=%zu\n",original_calloc_count*sizeof(int32_t),widened_calloc_count*sizeof(int32_t));
    if (original_calloc_count != 2484540704ULL || widened_calloc_count != 6779508000ULL) return 1;
    all_nterms=6448959; nvars=449;
    if ((size_t)(all_nterms*nvars)!=(size_t)all_nterms*nvars) return 2;
    puts("ALLOCATION_WRAP_CONFIRMED; prior smaller-input allocation is a negative control");
    return 0;
}

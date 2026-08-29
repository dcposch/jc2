#include <fstream>
#include <iostream>

#include <givaro/modular.h>
#include <linbox/matrix/sparse-matrix.h>
#include <linbox/solutions/methods.h>
#include <linbox/solutions/solve.h>
#include <linbox/util/matrix-stream.h>
#include <linbox/vector/vector-domain.h>

using namespace LinBox;

int main(int argc, char **argv) {
    if (argc != 5) {
        std::cerr << "usage: w35_n7_seed_extension_modp MATRIX RHS PRIME OUTPUT\n";
        return 125;
    }
    const unsigned long prime = std::stoul(argv[3]);
    if (prime != 65519) return 126;
    typedef Givaro::Modular<double> Field;
    typedef DenseVector<Field> FieldVector;
    Field field(static_cast<double>(prime));
    std::ifstream matrix_input(argv[1]);
    std::ifstream rhs_input(argv[2]);
    if (!matrix_input || !rhs_input) return 127;
    MatrixStream<Field> stream(field, matrix_input);
    SparseMatrix<Field> matrix(stream);
    FieldVector rhs(field, matrix.rowdim());
    FieldVector solution(field, matrix.coldim());
    for (auto &entry : rhs) {
        if (!field.read(rhs_input, entry)) return 128;
    }
    try {
        solve(solution, matrix, rhs, Method::SparseElimination());
    } catch (const std::exception &error) {
        std::cerr << error.what() << '\n';
        return 129;
    }
    FieldVector replay(field, matrix.rowdim());
    matrix.apply(replay, solution);
    VectorDomain<Field> vector_domain(field);
    if (!vector_domain.areEqual(replay, rhs)) return 130;
    std::ofstream output(argv[4]);
    if (!output) return 131;
    output << "A1_RHO0_W35_N7_SEED_EXTENSION_MODP\n" << prime << '\n'
           << solution.size() << '\n';
    for (const auto &entry : solution) field.write(output, entry) << '\n';
    output << "PASS_A1_RHO0_W35_N7_SEED_EXTENSION_MODP\n";
    return output ? 0 : 132;
}

#include <fstream>
#include <iostream>

#include <givaro/zring.h>
#include <linbox/matrix/sparse-matrix.h>
#include <linbox/solutions/methods.h>
#include <linbox/solutions/solve.h>
#include <linbox/util/matrix-stream.h>
#include <linbox/vector/vector-domain.h>

using namespace LinBox;

int main(int argc, char **argv) {
    if (argc != 4) {
        std::cerr << "usage: rho0_dual_linbox_v43 MATRIX RHS OUTPUT\n";
        return 125;
    }
    typedef Givaro::ZRing<Givaro::Integer> Integers;
    typedef DenseVector<Integers> IntegerVector;
    Integers ZZ;
    std::ifstream matrix_input(argv[1]);
    std::ifstream rhs_input(argv[2]);
    if (!matrix_input || !rhs_input) return 126;
    MatrixStream<Integers> stream(ZZ, matrix_input);
    SparseMatrix<Integers> matrix(stream);
    IntegerVector rhs(ZZ, matrix.rowdim());
    IntegerVector numerator(ZZ, matrix.coldim());
    for (auto &entry : rhs) {
        if (!(rhs_input >> entry)) return 127;
    }
    Givaro::ZRing<Givaro::Integer>::Element denominator;
    try {
        solve(numerator, denominator, matrix, rhs, Method::SparseElimination());
    } catch (const std::exception &error) {
        std::cerr << error.what() << '\n';
        return 128;
    }
    IntegerVector lhs(ZZ, matrix.rowdim());
    IntegerVector scaled_rhs(ZZ, rhs);
    MatrixDomain<Integers> matrix_domain(ZZ);
    VectorDomain<Integers> vector_domain(ZZ);
    matrix_domain.vectorMul(lhs, matrix, numerator);
    vector_domain.mulin(scaled_rhs, denominator);
    if (denominator == 0 || !vector_domain.areEqual(lhs, scaled_rhs)) return 129;
    std::ofstream output(argv[3]);
    if (!output) return 130;
    output << "V43_RHO0_DUAL_LINBOX_EXACT\n";
    output << denominator << '\n';
    output << numerator.size() << '\n';
    for (const auto &entry : numerator) output << entry << '\n';
    output << "PASS_A1_TOTAL_DVR_W30_V43_RHO0_DUAL_LINBOX\n";
    return output ? 0 : 131;
}

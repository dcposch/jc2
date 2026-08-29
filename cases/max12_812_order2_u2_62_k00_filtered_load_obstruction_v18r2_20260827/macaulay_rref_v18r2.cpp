#include <flint/flint.h>
#include <flint/fmpq.h>
#include <flint/fmpq_mat.h>
#include <flint/fmpz.h>
#include <flint/nmod_mat.h>
#include <flint/ulong_extras.h>

#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

struct Entry {
  slong row;
  slong column;
  std::string numerator;
  std::string denominator;
};

struct Input {
  slong rows;
  slong columns;
  slong nonzeros;
  slong cutoff;
  std::vector<Entry> entries;
};

Input read_input(const std::string& path) {
  std::ifstream in(path);
  if (!in) throw std::runtime_error("cannot open matrix input");
  Input value;
  in >> value.rows >> value.columns >> value.nonzeros >> value.cutoff;
  if (!in || value.rows <= 0 || value.columns <= 0 || value.nonzeros <= 0)
    throw std::runtime_error("malformed matrix header");
  value.entries.reserve(value.nonzeros);
  for (slong index = 0; index < value.nonzeros; ++index) {
    Entry entry;
    in >> entry.row >> entry.column >> entry.numerator >> entry.denominator;
    if (!in || entry.row < 0 || entry.row >= value.rows || entry.column < 0 ||
        entry.column > value.columns)
      throw std::runtime_error("malformed matrix entry");
    value.entries.push_back(entry);
  }
  std::string extra;
  if (in >> extra) throw std::runtime_error("trailing matrix input");
  return value;
}

void run_q(const Input& input, const std::string& solution_path) {
  fmpq_mat_t matrix, reduced;
  fmpq_mat_init(matrix, input.rows, input.columns + 1);
  fmpq_mat_init(reduced, input.rows, input.columns + 1);
  fmpz_t numerator, denominator;
  fmpz_init(numerator);
  fmpz_init(denominator);
  for (const auto& entry : input.entries) {
    if (fmpz_set_str(numerator, entry.numerator.c_str(), 10) != 0 ||
        fmpz_set_str(denominator, entry.denominator.c_str(), 10) != 0 ||
        fmpz_is_zero(denominator))
      throw std::runtime_error("invalid rational entry");
    fmpq_set_fmpz_frac(fmpq_mat_entry(matrix, entry.row, entry.column),
                       numerator, denominator);
  }
  const slong augmented_rank = fmpq_mat_rref(reduced, matrix);
  bool inconsistent = false;
  slong inconsistent_row = -1;
  for (slong row = 0; row < input.rows; ++row) {
    bool coefficient_nonzero = false;
    for (slong column = 0; column < input.columns; ++column) {
      if (!fmpq_is_zero(fmpq_mat_entry(reduced, row, column))) {
        coefficient_nonzero = true;
        break;
      }
    }
    if (!coefficient_nonzero &&
        !fmpq_is_zero(fmpq_mat_entry(reduced, row, input.columns))) {
      inconsistent = true;
      inconsistent_row = row;
      break;
    }
  }
  const slong rank = augmented_rank - (inconsistent ? 1 : 0);
  std::ofstream solution(solution_path);
  if (!solution) throw std::runtime_error("cannot open solution output");
  solution << "field Q\n";
  solution << "cutoff " << input.cutoff << "\n";
  solution << "rows " << input.rows << "\n";
  solution << "columns " << input.columns << "\n";
  solution << "rank " << rank << "\n";
  solution << "augmented_rank " << augmented_rank << "\n";
  solution << "consistent " << (inconsistent ? 0 : 1) << "\n";
  if (!inconsistent) {
    for (slong row = 0; row < input.rows; ++row) {
      slong pivot = -1;
      for (slong column = 0; column < input.columns; ++column) {
        if (!fmpq_is_zero(fmpq_mat_entry(reduced, row, column))) {
          pivot = column;
          break;
        }
      }
      if (pivot >= 0 && !fmpq_is_zero(fmpq_mat_entry(reduced, row, input.columns))) {
        char* text = fmpq_get_str(nullptr, 10, fmpq_mat_entry(reduced, row, input.columns));
        solution << "x " << pivot << " " << text << "\n";
        flint_free(text);
      }
    }
  } else {
    solution << "inconsistent_row " << inconsistent_row << "\n";
    fmpq_mat_clear(reduced);
    fmpq_mat_t transpose, transpose_reduced;
    fmpq_mat_init(transpose, input.columns, input.rows);
    fmpq_mat_init(transpose_reduced, input.columns, input.rows);
    for (slong row = 0; row < input.rows; ++row)
      for (slong column = 0; column < input.columns; ++column)
        fmpq_set(fmpq_mat_entry(transpose, column, row),
                 fmpq_mat_entry(matrix, row, column));
    const slong transpose_rank = fmpq_mat_rref(transpose_reduced, transpose);
    std::vector<slong> pivot_row(input.rows, -1);
    for (slong row = 0; row < transpose_rank; ++row) {
      for (slong column = 0; column < input.rows; ++column) {
        if (!fmpq_is_zero(fmpq_mat_entry(transpose_reduced, row, column))) {
          pivot_row[column] = row;
          break;
        }
      }
    }
    bool certificate_found = false;
    fmpq_t dot, term, coordinate;
    fmpq_init(dot);
    fmpq_init(term);
    fmpq_init(coordinate);
    for (slong free_column = 0; free_column < input.rows && !certificate_found;
         ++free_column) {
      if (pivot_row[free_column] >= 0) continue;
      fmpq_zero(dot);
      for (slong row = 0; row < input.rows; ++row) {
        if (row == free_column) {
          fmpq_one(coordinate);
        } else if (pivot_row[row] >= 0) {
          fmpq_neg(coordinate,
                   fmpq_mat_entry(transpose_reduced, pivot_row[row], free_column));
        } else {
          fmpq_zero(coordinate);
        }
        fmpq_mul(term, coordinate, fmpq_mat_entry(matrix, row, input.columns));
        fmpq_add(dot, dot, term);
      }
      if (!fmpq_is_zero(dot)) {
        certificate_found = true;
        char* dot_text = fmpq_get_str(nullptr, 10, dot);
        solution << "certificate_dot " << dot_text << "\n";
        flint_free(dot_text);
        for (slong row = 0; row < input.rows; ++row) {
          if (row == free_column) {
            fmpq_one(coordinate);
          } else if (pivot_row[row] >= 0) {
            fmpq_neg(coordinate,
                     fmpq_mat_entry(transpose_reduced, pivot_row[row], free_column));
          } else {
            fmpq_zero(coordinate);
          }
          if (!fmpq_is_zero(coordinate)) {
            char* text = fmpq_get_str(nullptr, 10, coordinate);
            solution << "y " << row << " " << text << "\n";
            flint_free(text);
          }
        }
      }
    }
    fmpq_clear(dot);
    fmpq_clear(term);
    fmpq_clear(coordinate);
    fmpq_mat_clear(transpose);
    fmpq_mat_clear(transpose_reduced);
    if (!certificate_found)
      throw std::runtime_error("failed to construct exact incompatibility certificate");
  }
  std::cout << "K00_MACAULAY_FIELD=Q\n";
  std::cout << "K00_MACAULAY_CUTOFF=" << input.cutoff << "\n";
  std::cout << "K00_MACAULAY_ROWS=" << input.rows << "\n";
  std::cout << "K00_MACAULAY_COLUMNS=" << input.columns << "\n";
  std::cout << "K00_MACAULAY_RANK=" << rank << "\n";
  std::cout << "K00_MACAULAY_AUGMENTED_RANK=" << augmented_rank << "\n";
  std::cout << "K00_MACAULAY_CONSISTENT=" << (inconsistent ? 0 : 1) << "\n";
  fmpz_clear(numerator);
  fmpz_clear(denominator);
  fmpq_mat_clear(matrix);
  if (!inconsistent) fmpq_mat_clear(reduced);
  flint_cleanup();
}

mp_limb_t parse_mod(const std::string& text, mp_limb_t prime) {
  fmpz_t value;
  fmpz_init(value);
  if (fmpz_set_str(value, text.c_str(), 10) != 0)
    throw std::runtime_error("invalid modular integer");
  const mp_limb_t result = fmpz_fdiv_ui(value, prime);
  fmpz_clear(value);
  return result;
}

void run_prime(const Input& input, mp_limb_t prime, const std::string& solution_path) {
  if (!n_is_prime(prime)) throw std::runtime_error("modulus is not prime");
  nmod_mat_t matrix, original;
  nmod_mat_init(matrix, input.rows, input.columns + 1, prime);
  nmod_mat_init(original, input.rows, input.columns + 1, prime);
  for (const auto& entry : input.entries) {
    const mp_limb_t numerator = parse_mod(entry.numerator, prime);
    const mp_limb_t denominator = parse_mod(entry.denominator, prime);
    if (denominator == 0) throw std::runtime_error("denominator vanishes modulo prime");
    const mp_limb_t value = n_mulmod2_preinv(numerator, n_invmod(denominator, prime), prime,
                                             matrix->mod.ninv);
    nmod_mat_entry(matrix, entry.row, entry.column) = value;
    nmod_mat_entry(original, entry.row, entry.column) = value;
  }
  const slong augmented_rank = nmod_mat_rref(matrix);
  bool inconsistent = false;
  for (slong row = 0; row < input.rows; ++row) {
    bool coefficient_nonzero = false;
    for (slong column = 0; column < input.columns; ++column) {
      if (nmod_mat_entry(matrix, row, column) != 0) {
        coefficient_nonzero = true;
        break;
      }
    }
    if (!coefficient_nonzero && nmod_mat_entry(matrix, row, input.columns) != 0) {
      inconsistent = true;
      break;
    }
  }
  const slong rank = augmented_rank - (inconsistent ? 1 : 0);
  std::ofstream solution(solution_path);
  if (!solution) throw std::runtime_error("cannot open modular solution output");
  solution << "field " << prime << "\n";
  solution << "cutoff " << input.cutoff << "\n";
  solution << "rows " << input.rows << "\n";
  solution << "columns " << input.columns << "\n";
  solution << "rank " << rank << "\n";
  solution << "augmented_rank " << augmented_rank << "\n";
  solution << "consistent " << (inconsistent ? 0 : 1) << "\n";
  if (!inconsistent) {
    for (slong row = 0; row < input.rows; ++row) {
      slong pivot = -1;
      for (slong column = 0; column < input.columns; ++column) {
        if (nmod_mat_entry(matrix, row, column) != 0) {
          pivot = column;
          break;
        }
      }
      if (pivot >= 0 && nmod_mat_entry(matrix, row, input.columns) != 0)
        solution << "x " << pivot << " " << nmod_mat_entry(matrix, row, input.columns) << "\n";
    }
  } else {
    nmod_mat_t transpose;
    nmod_mat_init(transpose, input.columns, input.rows, prime);
    for (slong row = 0; row < input.rows; ++row)
      for (slong column = 0; column < input.columns; ++column)
        nmod_mat_entry(transpose, column, row) = nmod_mat_entry(original, row, column);
    const slong transpose_rank = nmod_mat_rref(transpose);
    std::vector<slong> pivot_row(input.rows, -1);
    for (slong row = 0; row < transpose_rank; ++row) {
      for (slong column = 0; column < input.rows; ++column) {
        if (nmod_mat_entry(transpose, row, column) != 0) {
          pivot_row[column] = row;
          break;
        }
      }
    }
    bool certificate_found = false;
    std::vector<mp_limb_t> certificate(input.rows, 0);
    mp_limb_t certificate_dot = 0;
    for (slong free_column = 0; free_column < input.rows && !certificate_found;
         ++free_column) {
      if (pivot_row[free_column] >= 0) continue;
      std::fill(certificate.begin(), certificate.end(), 0);
      certificate[free_column] = 1;
      for (slong row = 0; row < input.rows; ++row) {
        if (pivot_row[row] >= 0) {
          const mp_limb_t value = nmod_mat_entry(transpose, pivot_row[row], free_column);
          certificate[row] = value == 0 ? 0 : prime - value;
        }
      }
      mp_limb_t dot = 0;
      for (slong row = 0; row < input.rows; ++row) {
        const mp_limb_t term = n_mulmod2_preinv(
            certificate[row], nmod_mat_entry(original, row, input.columns), prime,
            original->mod.ninv);
        dot = n_addmod(dot, term, prime);
      }
      if (dot != 0) {
        certificate_found = true;
        certificate_dot = dot;
      }
    }
    if (!certificate_found)
      throw std::runtime_error("failed to construct modular incompatibility certificate");
    solution << "certificate_dot " << certificate_dot << "\n";
    for (slong row = 0; row < input.rows; ++row)
      if (certificate[row] != 0)
        solution << "y " << row << " " << certificate[row] << "\n";
    nmod_mat_clear(transpose);
  }
  std::cout << "K00_MACAULAY_FIELD=" << prime << "\n";
  std::cout << "K00_MACAULAY_CUTOFF=" << input.cutoff << "\n";
  std::cout << "K00_MACAULAY_ROWS=" << input.rows << "\n";
  std::cout << "K00_MACAULAY_COLUMNS=" << input.columns << "\n";
  std::cout << "K00_MACAULAY_RANK=" << rank << "\n";
  std::cout << "K00_MACAULAY_AUGMENTED_RANK=" << augmented_rank << "\n";
  std::cout << "K00_MACAULAY_CONSISTENT=" << (inconsistent ? 0 : 1) << "\n";
  nmod_mat_clear(matrix);
  nmod_mat_clear(original);
  flint_cleanup();
}

int main(int argc, char** argv) {
  try {
    if (argc != 5 || std::string(argv[1]) != "--field")
      throw std::runtime_error("usage: macaulay_rref --field Q|PRIME MATRIX SOLUTION");
    const std::string field = argv[2];
    const Input input = read_input(argv[3]);
    if (field == "Q") {
      run_q(input, argv[4]);
    } else {
      const mp_limb_t prime = std::stoul(field);
      run_prime(input, prime, argv[4]);
    }
    std::cout << "K00_MACAULAY_ENGINE_ENDPOINT=PASS\n";
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "K00_MACAULAY_ENGINE_FAIL=" << error.what() << "\n";
    return 70;
  }
}

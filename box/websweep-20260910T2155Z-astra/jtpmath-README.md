# Sheaf-Theoretic Obstructions in Higher Dimensions and Topological Rigidity in the Affine Plane

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21893538.svg)](https://doi.org/10.5281/zenodo.21893538)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Author:** Jasmine S. Burns  
**Affiliation:** JTPMATH Incorporated  
**Contact:** jas@jtpmath.com  

---

## Abstract

For nearly nine decades, the Keller Jacobian conjecture stood as a fundamental open problem in affine algebraic geometry, proposing that a polynomial mapping $F: \mathbb{C}^n \to \mathbb{C}^n$ with a non-zero constant Jacobian determinant possesses a global polynomial inverse. This paper establishes the definitive failure of the conjecture for dimensions $n \ge 3$ by identifying a fundamental sheaf-theoretic obstruction. We demonstrate that while local analytic inverses exist by the Inverse Function Theorem, non-trivial monodromy around the branch locus of multi-sheeted coverings generates a non-vanishing Čech cohomology class in $H^1(\mathcal{U}, \mathcal{F})$ explicitly preventing the descent of these local patches into a global polynomial ring. Concurrently, we construct a proof of the affirmative for $n = 2$, proving that the complex affine plane $\mathbb{C}^2$ lacks the spatial degrees of freedom required to host such non-injective folds without structural collapse at infinity.

---

## Paper & Source Code

* **Preprint PDF:** [paper/compiled/manuscript.pdf](https://github.com/jtpmath/jacobian-conjecture-sheaf-obstructions/blob/main/paper/compiled/Manuscript.pdf)
* **Zenodo DOI:** [10.5281/zenodo.21893538](https://doi.org/10.5281/zenodo.21893538)

## Citation
If you reference this work or build upon the cohomological/resultant framework in your research, please cite:

@article{Burns2026Jacobian,
  author    = {Burns, Jasmine S.},
  
  title     = {Sheaf-Theoretic Obstructions in Higher Dimensions and Topological Rigidity in the Affine Plane},
  
  journal   = {Zenodo Preprint},
  
  year      = {2026},
  
  doi       = {10.5281/zenodo.21893538},
  
  publisher = {JTPMATH Incorporated}
  
  }

### Building from Source

To compile the LaTeX source locally:

```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

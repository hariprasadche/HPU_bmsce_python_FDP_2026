from pyscf import gto, dft

# 1. Define the molecule (geometry and basis set)
mol = gto.M(
    atom='O 0.0 0.0 0.0; H 0.0 0.757 0.586; H 0.0 -0.757 0.586',
    basis='6-31G',
    verbose=0
)

# 2. Select DFT method (Restricted Kohn-Sham)
mf = dft.RKS(mol)

# 3. Choose the functional (e.g., B3LYP)
mf.xc = 'b3lyp'

# 4. Run the calculation
energy = mf.kernel()

print(f"Total DFT energy: {energy} Hartree")
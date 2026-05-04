# CORDIAL
Predicts small molecule - protein interaction affinities using convolutional representations of distance-dependent interactions with attention learning (CORDIAL). 

First described in the paper "A generalizable deep learning framework for structure-based protein–ligand affinity ranking" <https://doi.org/10.1073/pnas.2508998122>

## Installation

CORDIAL is installable via pip from Github directly.

        pip install git+https://github.com/bpBrownLab/CORDIAL.git

Or alternatively, if you have cloned the repository onto your local machine,

        pip install -e .

It should also be runnable without installing, if you've installed all the needed dependencies.

## Usage

If installed with pip, the `cordial` command should be available:

        cordial --inference --input_ligand_protein_pair_file pair_file.lst ....

Altenatively, you can run the script in the root directory

        /path/to/install/run_protocols.py --inference --input_ligand_protein_pair_file pair_file.lst ....

If running without pip installing, you may need to provide the `--load_model` and `--load_normalization_data_pkl` options to specify the model in the `weights/` directory and normalization file in the `resources/normalization/` directory to use.


The `pair_file.lst` is a file with semi-colon separated pairs of protein and ligand filenames:

        prot1.pdb;lig1.sdf
        prot2.pdb;lig2.sdf
        prot3.pdb;lig3.sdf

Other input options exist. Use `--help` to see the list of options.

## Output

The script will output a `inference_results_predictions.csv` file, with results in the order that was given in the `pair_file.lst` input. For most uses, the two columns of interest are `Predicted_Probabilities` and `Predicted_Class_Index`, which contain the prediction of whether the compound will bind at (cumulative) pKd levels of 1 to 8.

That is, a `Predicted_Probabilities` entry of 

          [0.9999 0.9999 0.9990 0.9672 0.6657 0.2596 0.1034 0.0286]

indicates that the model thinks there a 96.7% probability of binding at 100μM or better, a 66.6% probability of binding at 10μM or better and a 26.0% chance of binding at 1μM or better. (The above vector was obtained for a complex with an experimental Ki of 50 μM, pKi=4.3) 

The `Predicted_Class_Index` column is a discretization of the predicted probabilities, yielding `1` for entries greater than 50% and 0 for entries less than 50%. 

Note that while the model should output results which are consistent with the overlapping/cumulative nature of the output bins (i.e. each bin should be at least as probable as any tighter-binding bins), there is a chance that some inputs may produce inconsistent outputs.


Cheat sheet:

          [<100mM <10mM <1mM <100μM <10μM <1μM <100nM <10nM] 

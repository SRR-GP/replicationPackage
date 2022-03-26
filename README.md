### Evolving Ranking-Based Failure Proximities
This is the repository containing the data and source code for the paper "Evolving Ranking-Based Failure Proximities for Better Clustering in Fault Isolation".

+ The folder `allFormulas` is threefold, including all individuals in each generation along with their fitness scores (in the training phase), the dominant EFFs' fitness scores (in the test phase), and the values of *k* in the scenario of "*k* ≠ *r*".
  * `allData (training).pdf` provides 2400 (160 individuals per generation * 15 generations)
      individuals' expressions and their fitness scores in the training phase.
    * `allData (test).pdf` provides 10 dominant EFFs' expressions and fitness scores
       in the test phase.
    * `deviation.pdf` provides the values of *k* (the estimated number of faults) when it is not
       equal to *r* (the number of faults contained in the program).
  
+ The folder `replicationResource` is the source code of the proposed evolution framework and the faulty versions used in experiments and empirical evaluation.
    * `code/dependencies.py` lists the modules utilized in the framework.
    * `code/registration.py` initializes the services of the GP model and configures the evolving operators.
    * `code/initialPopulation.py` produces the initial population when the evolving process starts.
    * `code/select.py` performs the selection step to determine parents.
    * `code/getNextGeneration.py` conducts the operations of crossover, copy, or mutation, to deliver the next generation.
    * `code/getDeviation.py` measures the bias when the estimated number of clusters *k* and the number of faults *r* are not identical.
    * `code/getExeResult.py` determines the execution result of test cases (i.e., passed or failed) by comparing the expected and the actual output.
    * `code/getMetrics.py` measures the outcome of clustering results based on the predefined metrics.
    * `code/getSpectrum.py` processes raw coverage data into spectrum information that can be fed into REF/EFF.
    * `code/SBFL_Formulas_baselines.py` lists the source code of existing SBFL risk evaluation formulas.
    * `code/SBFL_Formulas_evolved.py` lists the source code of the evolved fingerprinting functions.
    * `dataset/SIR/` lists the C benchmark projects used in the experiments and empirical evaluation.
    * `dataset/D4J/` lists the JAVA benchmark projects used in the empirical evaluation.

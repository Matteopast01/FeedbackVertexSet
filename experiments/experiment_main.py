from DoublingNodeExperiment import DoublingNodeExperiment 
from IncreasingFVSsizeExperiment import IncreasingFVSsizeExperiment
from RandomGraphExperiment import RandomGraphExperiment
from ValidityTestingExperiment import ValidityTestingExperiment
if __name__ == '__main__':
    """
    # Create an instance of IncreasingFVSsizeExperiment with a specific output CSV file
    experiment = DoublingNodeExperiment(50, 30000, "doubling_nodes_results.csv")

    
    # Run the experiment
    experiment.run()
    """

    #experiment = IncreasingFVSsizeExperiment(5000, "improving_fvs_size_results.csv")
    #experiment.run()

    #experiment = RandomGraphExperiment("random_graphs.csv")
    #experiment.run()

    experiment = ValidityTestingExperiment("validity_testing.csv")
    experiment.run()


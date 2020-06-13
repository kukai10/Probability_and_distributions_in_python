import distributions




def make_RV(distribution="Binomial", sample_num = 3, distribution_parameter = [0, 1/2]):
    distribution_object = None
    if distribution == "binomial":
        output_val = distribution_parameter[0]
        success_rate = distribution_parameter[1]
        distribution_object = distributions.binomial(output_val, success_rate)
        
    else:
        pass





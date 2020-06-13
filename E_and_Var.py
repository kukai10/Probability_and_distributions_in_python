# this is a file with functions related to expectations, variances, st.dev, moments, etc
import math

def square_outcome(outcomes):
    return [outcome*outcome for outcome in outcomes]

def expectation(outcomes, probabilities = []):
    if probabilities == []:
        num_of_items = len(outcomes)
        probabilities = [1/num_of_items for _ in range(num_of_items)]
    return sum(outcome*probability for outcome, probability in zip(outcomes, probabilities))


def variance(outcomes, probabilities = []):
    if probabilities == []:
        num_of_items = len(outcomes)
        probabilities = [1/num_of_items for _ in range(num_of_items)]
    average = expectation(outcomes,probabilities)
    return expectation([(outcome-average)*(outcome-average) for outcome in outcomes], probabilities)


def expanded_variance(outcomes, probabilities):
    # from the deravation below:
    # Var(X) = E[(X - mu)^2] => expand the (X-mu)^2 and by linearity of expected values we get 
    # Var(X) = E[X^2] - E[2*mu*E[X]] + E[mu^2]
    # since mu = E[X] we can replace all the mu, to get
    # Var(X) = e[X^2] - E[2*E[X]*E[X]] + E[X^2] 
    # since E[E[X]] = E[X], We get the following result
    # Var(X) = E[X^2] - E[X]^2 
    return expectation(square_outcome(outcomes), probabilities) - expectation(outcomes,probabilities)**2

def standard_deviation(outcomes, probabilities):
    return math.sqrt(variance(outcomes, probabilities))

def covariance(X_outcome, X_prob, Y_outcome, Y_prob):
    # return covariance of two RV
    average_X = expectation(X_outcome, X_prob)
    average_Y = expectation(Y_outcome, Y_prob)
    
def covariance_after_deravation(X_outcome, X_prob, Y_outcome, Y_prob):
    expected_x = expectation(X_outcome, X_prob)
    expected_y = expectation(Y_outcome, Y_prob)

def moment():
    pass



def main():
    outcome_space = [1, 2, 3, 4, 0.5]
    probability_space = []
    print(variance(outcome_space, probability_space))
    print(expanded_variance(outcome_space, probability_space))



if __name__ == "__main__":
    main()
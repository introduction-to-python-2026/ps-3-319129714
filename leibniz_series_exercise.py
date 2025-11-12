def approximate_pi(n_terms):
    leibniz_sum = 0.0
    for i in range(n_terms):
        sign = (-1)**i
        denominator = 2 * i + 1
        term = sign / denominator
        leibniz_sum += term
    pi_approximation = 4 * leibniz_sum
    
    return pi_approximation

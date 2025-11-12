def approximate_pi(n_terms):
    leibniz_series = []
    
    for i in range(n_terms):
        sign = (-1)**i
        denominator = 2 * i + 1
        term = sign / denominator
        leibniz_series.append(term)
  
    series_sum = sum(leibniz_series)
    pi_approximation = 4 * series_sum
 
    return pi_approximation

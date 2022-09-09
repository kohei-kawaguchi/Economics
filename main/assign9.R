# Assignment 9: Auction #

rm(list = ls())
library(dplyr)
library(foreach)
library(latex2exp)
library(ggplot2)
library(Economics)
### 19.1 ###

## 1. Set the constants and parameters
# set seed
set.seed(1)
# number of auctions
T <- 100
# parameter of value distribution
alpha <- 2
beta <- 2
# prameters of number of potential bidders
lambda <- 10


## 2. Draw a vector of valuations and reservation prices.
# number of bidders
N <- rpois(T, lambda)
# draw valuations
valuation <-
  foreach::foreach (tt = 1:T, .combine = "rbind") %do% {
    n_t <- N[tt]
    header <- expand.grid(t = tt, i = 1:n_t) 
    return(header)
  }
valuation <- valuation %>%
  tibble::as_tibble() %>%
  dplyr::mutate(x = rbeta(length(i), alpha, beta))

ggplot2::ggplot(valuation, aes(x = x)) + geom_histogram(fill = "steelblue", alpha = 0.8)

# draw reserve prices
reserve <- 0.2
reserve <- tibble::tibble(t = 1:T, r = reserve)

## 3. compute winning bids from second-price auction

df_second_w <-
  Economics::compute_winning_bids_second(valuation, reserve,T)
df_second_w

ggplot2::ggplot(df_second_w, aes(x = w)) + geom_histogram(fill = "steelblue", alpha = 0.8)

#lifecycle::last_lifecycle_warnings()

## 4. compute bid from first-price auction

n <- N[1]
m <- N[1]
x <- valuation[1, "x"] %>% as.numeric(); x
r <- reserve[1, "r"] %>% as.numeric(); r
b <- Economics::bid_first(x, r, alpha, beta, n); b
x <- r/2; x
b <- Economics::bid_first(x, r, alpha, beta, n); b
b <- Economics::bid_first(1, r, alpha, beta, n); b

## 5. compute bid data from first-price auctions

df_first <- 
  Economics::compute_bids_first(valuation, reserve, alpha, beta)
df_first

ggplot2::ggplot(df_first, aes(x = b)) + geom_histogram(fill = "steelblue", alpha = 0.8)


## 6. compute winning bids from first-price auctions
df_first_w <-
  Economics::compute_winning_bids_first(valuation, reserve, alpha, beta)
df_first_w

ggplot2::ggplot(df_first_w, aes(x = w)) + geom_histogram(fill = "steelblue", alpha = 0.8)


### 19.2 ###

## 1. compute probability density for winning bids from a second-price auction

w <- df_second_w[1, ]$w
r <- df_second_w[1, ]$r
m <- df_second_w[1, ]$m
n <- df_second_w[1, ]$n
Economics::compute_p_second_w(w, r, m, n, alpha, beta)

## 2. compute non-participation probability

Economics::compute_m0(r, n, alpha, beta)

## 2. compute log-likelihood for winning bids from second-price auctions

theta <- c(alpha, beta)
Economics::compute_loglikelihood_second_price_w(theta, df_second_w, T)

## 3. Compare the value of objective function around the true parameters

# label
label <- c("\\alpha", "\\beta")
label <- paste("$", label, "$", sep = "")
# compute the graph
library(doParallel)
doParallel::registerDoParallel()
graph <- foreach::foreach (i = 1:length(theta)) %do% {
  theta_i <- theta[i]
  theta_i_list <- theta_i * seq(0.8, 1.2, by = 0.05)
  objective_i <-
    foreach::foreach (j = 1:length(theta_i_list),
             .packages = c("Economics", "foreach", "magrittr"),
             .combine = "rbind") %dopar% {
               theta_ij <- theta_i_list[j]
               theta_j <- theta
               theta_j[i] <- theta_ij
               objective_ij <- 
                 compute_loglikelihood_second_price_w(
                   theta_j, df_second_w,T)
               return(objective_ij)
             }
  df_graph <- data.frame(x = as.numeric(theta_i_list), 
                         y = as.numeric(objective_i))
  g <- ggplot2::ggplot(data = df_graph, aes(x = x, y = y)) +
    geom_point() +
    geom_vline(xintercept = theta_i, linetype = "dotted") +
    ylab("objective function") + xlab(latex2exp::TeX(label[i]))
  return(g)
}
save(graph, file = "output/assign9/A9_second_parametric_graph.RData")
load(file = "output/assign9/A9_second_parametric_graph.RData")
graph


## 4. Estimate the parameters by maximizing the log-likelihood

result_second_parametric <-
  optim(
    par = theta,
    fn = compute_loglikelihood_second_price_w,
    df_second_w = df_second_w,
    T = T,
    method = "L-BFGS-B",
    control = list(fnscale = -1)
  )
save(result_second_parametric, file = "output/assign9/A9_result_second_parametric.RData")

load(file = "output/assign9/A9_result_second_parametric.RData")
result_second_parametric

comparison <-
  data.frame(
    true = theta,
    estimate = result_second_parametric$par
  )
comparison


## 5. estimate parameters from the winning bids data from first-price auctions

r <- df_first_w[1, "r"] %>% as.numeric()
n <- df_first_w[1, "n"] %>% as.integer()
b <- 0.5 * r + 0.5 
x <- 0.5
# compute invecrse bid equation
Economics::inverse_bid_equation(x, b, r, alpha, beta, n)

# compute inverse bid
Economics::inverse_bid_first(b, r, alpha, beta, n)


## 6. compute probability density for a winning bid from a first-price auction

w <- 0.5
Economics::compute_p_first_w(w, r, alpha, beta, n)

upper <- bid_first(1, r, alpha, beta, n)
Economics::compute_p_first_w(upper + 1, r, alpha, beta, n)


## 7. compute log-likelihood for winning bids for first-price auctions
Economics::compute_loglikelihood_first_price_w(theta, df_first_w,T)


## 8. Compare the value of the objective function around the true parameters.
theta <- c(alpha, beta)
# label
label <- c("\\alpha", "\\beta")
label <- paste("$", label, "$", sep = "")
# compute the graph
graph <- foreach::foreach (i = 1:length(theta)) %do% {
  theta_i <- theta[i]
  theta_i_list <- theta_i * seq(0.8, 1.2, by = 0.05)
  objective_i <-
    foreach::foreach (j = 1:length(theta_i_list),
             .combine = "rbind") %do% {
               theta_ij <- theta_i_list[j]
               theta_j <- theta
               theta_j[i] <- theta_ij
               objective_ij <- 
                 compute_loglikelihood_first_price_w(
                   theta_j, df_first_w,T)
               return(objective_ij)
             }
  df_graph <- data.frame(x = as.numeric(theta_i_list), 
                         y = as.numeric(objective_i))
  g <- ggplot2::ggplot(data = df_graph, aes(x = x, y = y)) +
    geom_point() +
    geom_vline(xintercept = theta_i, linetype = "dotted") +
    ylab("objective function") + xlab(latex2exp::TeX(label[i]))
  return(g)
}
save(graph, file = "output/assign9/A9_first_parametric_graph.RData")
load(file = "output/assign9/A9_first_parametric_graph.RData")
graph


## 9. Estimate the parameters by maximizing the log-likelihood.

result_first_parametric <-
  optim(
    par = theta,
    fn = compute_loglikelihood_first_price_w,
    df_first_w = df_first_w,
    T = T,
    method = "Nelder-Mead",
    control = list(fnscale = -1)
  )
save(result_first_parametric, file = "output/assign9/A9_result_first_parametric.RData")

load(file = "output/assign9/A9_result_first_parametric.RData")
result_first_parametric

comparison <-
  data.frame(
    true = theta,
    estimate = result_first_parametric$par
  )
comparison


## 10. non-parametrically estimate the distribution of the valuation of first-price bid data

# cumulative distribution
ggplot2::ggplot(df_first, aes(x = b)) + stat_ecdf(color = "steelblue") +
  xlab("bid") + ylab("cumulative distribution")

F_b <- ecdf(df_first$b)
F_b(0.4)
F_b(0.6)

# probability density
ggplot2::ggplot(df_first, aes(x = b)) + geom_density(fill = "steelblue")

f_b <- approxfun(density(df_first$b))
f_b(0.4)
f_b(0.6)


## 11. equilibrium distribution and density of the highest rival’s bid at point b
Economics::H_b(0.4, n, F_b)
Economics::h_b(0.4, n, F_b, f_b)


## 12. implied valuation given a bid
r <- df_first[1, "r"]
n <- df_first[1, "n"]
Economics::compute_implied_valuation(0.4, n, r, F_b, f_b)


## 13. Obtain the vector of implied valuations from the vector of bids 
### and draw the empirical cumulative distribution. 
### Overlay it with the true empirical cumulative distribution of the valuations.

valuation_implied <- df_first %>%
  dplyr::rowwise() %>%
  dplyr::mutate(x = compute_implied_valuation(b, n, r, F_b, f_b)) %>%
  dplyr::ungroup() %>%
  dplyr::select(x) %>%
  dplyr::mutate(type = "estimate")
valuation_true <- valuation %>%
  dplyr::select(x) %>%
  dplyr::mutate(type = "true")
valuation_plot <- rbind(valuation_true, valuation_implied)
ggplot2::ggplot(valuation_plot, aes(x = x, color = type)) + stat_ecdf()






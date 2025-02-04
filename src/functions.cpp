#include <RcppEigen.h>

// [[Rcpp::export]]
Eigen::MatrixXd compute_utility_rcpp(
    const Eigen::MatrixXd& covariate,
    const Eigen::VectorXd& beta
) {
    Eigen::MatrixXd utility = covariate * beta;
    return utility;
}

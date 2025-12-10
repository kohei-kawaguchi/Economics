import numpy as np
import os
from typing import Dict, Any


def make_equilibrium(
    num_simulation: int, 
    num_alternative: int, 
    num_covariate: int
) -> Dict[str, np.ndarray]:
    """
    Create equilibrium structure with covariates, beta, and choice matrices.
    
    Args:
        num_simulation: Number of simulations
        num_alternative: Number of choice alternatives
        num_covariate: Number of covariates
        
    Returns:
        Dictionary containing covariate, beta, and choice matrices
    """
    # Generate random covariates
    covariate = np.random.normal(
        size=(num_alternative * num_covariate)
    ).reshape(num_alternative, num_covariate)
    
    # Set beta coefficients to 1
    beta = np.ones(num_covariate).reshape(-1, 1)
    
    # Initialize choice matrix with zeros
    choice = np.zeros((num_simulation, num_alternative))
    
    # Return as dictionary
    equilibrium = {
        "covariate": covariate,
        "beta": beta,
        "choice": choice
    }
    
    return equilibrium


def compute_utility(
    covariate: np.ndarray,
    beta: np.ndarray
) -> np.ndarray:
    """
    Compute utility based on covariates and beta parameters.
    
    Args:
        covariate: Matrix of covariates
        beta: Vector of coefficients
        
    Returns:
        Vector of utilities
    """
    utility = covariate @ beta
    return utility


def compute_choice_probability(
    covariate: np.ndarray, 
    beta: np.ndarray
) -> np.ndarray:
    """
    Compute choice probabilities using multinomial logit formula.
    
    Args:
        covariate: Matrix of covariates
        beta: Vector of coefficients
        
    Returns:
        Vector of choice probabilities
    """
    utility = compute_utility(covariate, beta)
    
    # Apply exponential and normalize (softmax)
    exp_utility = np.exp(utility)
    choice_probability = exp_utility / np.sum(exp_utility)
    
    return choice_probability


def simulate_choice(
    seed: int,
    equilibrium: Dict[str, np.ndarray]
) -> Dict[str, np.ndarray]:
    """
    Simulate choices based on multinomial probability.
    
    Args:
        seed: Random seed for reproducibility
        equilibrium: Dictionary containing model components
        
    Returns:
        Updated equilibrium dictionary with simulated choices
    """
    np.random.seed(seed)
    
    choice_probability = compute_choice_probability(
        covariate=equilibrium["covariate"],
        beta=equilibrium["beta"]
    )
    
    num_simulation = equilibrium["choice"].shape[0]
    choice_matrix = np.zeros_like(equilibrium["choice"])
    
    # For each simulation, draw from multinomial distribution
    for i in range(num_simulation):
        choice_idx = np.random.choice(
            len(choice_probability), 
            p=choice_probability.flatten()
        )
        choice_matrix[i, choice_idx] = 1
    
    # Update equilibrium with simulated choices
    equilibrium["choice"] = choice_matrix
    
    return equilibrium 
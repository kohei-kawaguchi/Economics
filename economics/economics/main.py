# import libraries
import matplotlib.pyplot as plt
import numpy as np

from economics.economics.core import Equilibrium
import os

# Create range of n values
n_values = np.arange(1, 21, 0.01)

# Initialize lists to store results
results = {}
for theta in [2, 4]:
    results[theta] = {
        'vertically_integrated': {
            'delivery': [], 'price_high': [], 'price_low': [],
            'consumer': [], 'wholesaler': [], 'retailer': []
        },
        'wholesale': {
            'delivery': [], 'price_high': [], 'price_low': [], 
            'wholesale_price': [], 'total_delivery': [],
            'consumer': [], 'wholesaler': [], 'retailer': []
        },
        'maximum_rpm': {
            'delivery': [], 'price_high': [], 'price_low': [],
            'wholesale_price': [], 'price_ceiling': [], 'total_delivery': [],
            'consumer': [], 'wholesaler': [], 'retailer': []
        },
        'minimum_rpm': {
            'delivery': [], 'price_high': [], 'price_low': [],
            'wholesale_price': [], 'price_ceiling': [], 'total_delivery': [],
            'consumer': [], 'wholesaler': [], 'retailer': []
        }
    }
    
    # Calculate equilibrium values for each n
    for n in n_values:
        eq = Equilibrium({'theta': theta}, {'n': n})
        
        # Vertically integrated equilibrium
        eq.solve_vertically_integrated()
        for key in results[theta]['vertically_integrated'].keys():
            if key in ['consumer', 'wholesaler', 'retailer']:
                results[theta]['vertically_integrated'][key].append(eq.surplus.get(key, 0))
            else:
                results[theta]['vertically_integrated'][key].append(eq.endogenous.get(key, 0))
        
        # Wholesale equilibrium
        eq.solve_wholesale()
        for key in results[theta]['wholesale'].keys():
            if key in ['consumer', 'wholesaler', 'retailer']:
                results[theta]['wholesale'][key].append(eq.surplus.get(key, 0))
            else:
                results[theta]['wholesale'][key].append(eq.endogenous.get(key, 0))
            
        # Maximum RPM equilibrium    
        eq.solve_maximum_rpm()
        for key in results[theta]['maximum_rpm'].keys():
            if key in ['consumer', 'wholesaler', 'retailer']:
                results[theta]['maximum_rpm'][key].append(eq.surplus.get(key, 0))
            else:
                results[theta]['maximum_rpm'][key].append(eq.endogenous.get(key, 0))
            
        # Minimum RPM equilibrium
        eq.solve_minimum_rpm()
        for key in results[theta]['minimum_rpm'].keys():
            if key in ['consumer', 'wholesaler', 'retailer']:
                results[theta]['minimum_rpm'][key].append(eq.surplus.get(key, 0))
            else:
                results[theta]['minimum_rpm'][key].append(eq.endogenous.get(key, 0))

# Create plots
variables = ['delivery', 'price_high', 'price_low', 'wholesale_price', 'total_delivery', 
            'consumer', 'wholesaler', 'retailer']
titles = ['Delivery', 'High Price', 'Low Price', 'Wholesale Price', 'Total Delivery',
          'Consumer Surplus', 'Wholesaler Surplus', 'Retailer Surplus']
regimes = ['vertically_integrated', 'wholesale', 'maximum_rpm', 'minimum_rpm']
regime_labels = ['Vertically Integrated', 'Wholesale', 'Maximum RPM', 'Minimum RPM']
# Using a color palette common in academic journals
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B3']  # Blue, Green, Red, Purple

output_dir = 'draft/figuretable'
os.makedirs(output_dir, exist_ok=True)

for theta in [2, 4]:
    # Calculate threshold n for this theta
    eq = Equilibrium({'theta': theta}, {'n': 1})  # n value doesn't matter for threshold
    n_thresh = eq.n_threshold()
    
    for var, title in zip(variables, titles):
        plt.figure(figsize=(10, 6))
        
        plotted_lines = {}
        markers = ['o', 's', '^', 'D']  # Circle, Square, Triangle, Diamond
        for regime, label, color, marker in zip(regimes, regime_labels, colors, markers):
            if var in results[theta][regime]:  # Only plot if variable exists for regime
                line, = plt.plot(n_values, results[theta][regime][var], 
                               label=label,
                               color=color,
                               marker=marker,
                               markevery=100)
                plotted_lines[regime] = line
        
        # Add vertical line at threshold
        plt.axvline(x=n_thresh, color='#404040', linestyle='--', label=f'n* = {n_thresh:.2f}')
        
        plt.xlabel('Number of Retailers (n)')
        plt.ylabel(title)
        # plt.title(f'{title} vs Number of Retailers (θ={theta})')
        
        # Check for overlapping lines
        for i, regime1 in enumerate(regimes):
            for j, regime2 in enumerate(regimes):
                if i < j and var in results[theta][regime1] and var in results[theta][regime2]:
                    if np.allclose(results[theta][regime1][var], results[theta][regime2][var]):
                        # Change the label of the latter line to indicate overlap
                        plotted_lines[regime2].set_label(f'{regime_labels[j]} (overlaps with {regime_labels[i]})')
                        # Bring the former line to the front
                        plotted_lines[regime1].set_zorder(plotted_lines[regime2].get_zorder() + 1)
        
        plt.legend()
        
        # Save plot with a distinct name
        filename = os.path.join(output_dir, f'{title.replace(" ", "_").lower()}_theta_{theta}.png')
        plt.savefig(filename)
        plt.close()

    # Plot for Supply Surplus
    plt.figure(figsize=(10, 6))
    plotted_lines = {}
    for regime, label, color, marker in zip(regimes, regime_labels, colors, markers):
        if 'wholesaler' in results[theta][regime] and 'retailer' in results[theta][regime]:
            supply_surplus = np.array(results[theta][regime]['wholesaler']) + np.array(results[theta][regime]['retailer'])
            line, = plt.plot(n_values, supply_surplus, 
                           label=label,
                           color=color,
                           marker=marker,
                           markevery=100)
            plotted_lines[regime] = line

    # Add vertical line at threshold
    plt.axvline(x=n_thresh, color='#404040', linestyle='--', label=f'n* = {n_thresh:.2f}')
    
    plt.xlabel('Number of Retailers (n)')
    plt.ylabel('Supply Surplus')
    # plt.title(f'Supply Surplus vs Number of Retailers (θ={theta})')
    
    # Check for overlapping lines
    for i, regime1 in enumerate(regimes):
        for j, regime2 in enumerate(regimes):
            if i < j and 'wholesaler' in results[theta][regime1] and 'retailer' in results[theta][regime2]:
                supply_surplus1 = np.array(results[theta][regime1]['wholesaler']) + np.array(results[theta][regime1]['retailer'])
                supply_surplus2 = np.array(results[theta][regime2]['wholesaler']) + np.array(results[theta][regime2]['retailer'])
                if np.allclose(supply_surplus1, supply_surplus2):
                    # Change the label of the latter line to indicate overlap
                    plotted_lines[regime2].set_label(f'{regime_labels[j]} (overlaps with {regime_labels[i]})')
                    # Bring the former line to the front
                    plotted_lines[regime1].set_zorder(plotted_lines[regime2].get_zorder() + 1)
    
    plt.legend()
    
    # Save plot with a distinct name
    filename = os.path.join(output_dir, f'supply_surplus_theta_{theta}.png')
    plt.savefig(filename)
    plt.close()

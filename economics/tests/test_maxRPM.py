def n_threshold_high(self):
    return (1 + self.parameter["theta"] + np.sqrt((1 + self.parameter["theta"]) * (4 + self.parameter["theta"]))) / 3
  
def n_threshold_all(self):
    return (self.parameter["theta"] + 1) / (self.parameter["theta"] - 1)
      
def n_threshold(self):
    if self.parameter["theta"] >= 3:
      return self.n_threshold_high()
    else:
      return self.n_threshold_all()
      

def solve_maximum_rpm(self):
    if self.parameter["theta"] < 3 and self.exogenous["n"] < self.n_threshold_all():
        # \bar{p} = \frac{1}{1 + \theta}
        self.endogenous["price_ceiling"] = 1 / (1 + self.parameter["theta"])

        # p^{max}_w = \frac{1}{2}
        self.endogenous["wholesale_price"] = 0.5

        # d^{max} = \frac{\theta}{(1+\theta)}
        self.endogenous["delivery"] = (
            self.parameter["theta"] 
            / (1 + self.parameter["theta"])
        )

        # D^{max} = \frac{n\theta}{(1+\theta)}
        self.endogenous["total_delivery"] = (
            self.exogenous["n"] * self.parameter["theta"]
            / (1 + self.parameter["theta"])
        )

        # p^{max}_{H} = \frac{\theta}{1+\theta}
        self.endogenous["price_high"] = (
            self.parameter["theta"]
            / (1 + self.parameter["theta"])
        )

        # p^{max}_L = \frac{1}{\theta+ 1}
        self.endogenous["price_low"] = 1 / (1 + self.parameter["theta"])

        # \frac{\theta^2}{2(1+\theta)^2}
        self.surplus["consumer"] = (
            self.parameter["theta"] ** 2
            / (2 * (1 + self.parameter["theta"]) ** 2)
        )

        # Expected retailer surplus = 0
        self.surplus["retailor"] = 0

        # \frac{\theta}{(1+\theta)^2}
        self.surplus["wholesaler"] = (
            self.parameter["theta"]
            / ((1 + self.parameter["theta"]) ** 2)
        )
    else:
        # \bar{p} = \frac{1}{2}$
        self.endogenous["price_ceiling"] = 1 / 2

        # The wholesaler price  $ p_w^{max} =\frac{1}{4} + \frac{n^2}{(n + 1)^2}\frac{1}{\theta}$. 
        self.endogenous["wholesale_price"] = 1 / 4 + (self.exogenous["n"] ** 2) / ((self.exogenous["n"] + 1) ** 2) * 1 / self.parameter["theta"]

        # The delivery is $d^{max} = \frac{\theta}{2n}$. Total delivery $D^{max} = \frac{\theta }{2}$. 
        self.endogenous["delivery"] = self.parameter["theta"] / (2 * self.exogenous["n"])
        self.endogenous["total_delivery"] = self.parameter["theta"] / 2

        # Price $p^{Max}_{H} = \frac{1}{2}$, price $p^{max}_L = \frac{1}{n+ 1}$.
        self.endogenous["price_high"] = 1 / 2
        self.endogenous["price_low"] = 1 / (self.exogenous["n"] + 1)

        # Expected consumer surplus $\frac{\theta}{16} + \frac{n^2}{4(n + 1)^2}$. 
        self.surplus["consumer"] = (
            self.parameter["theta"] / 16 + (self.exogenous["n"] ** 2) / (4 * (self.exogenous["n"] + 1) ** 2)
        )

        # The expected (total) retailer surplus is 0. 
        self.surplus["retailor"] = 0

        # The surplus for the wholesaler $\frac{\theta}{8} + \frac{1}{2}\frac{n}{(n + 1)^2}$
        self.surplus["wholesaler"] = (
            self.parameter["theta"] / 8 + 0.5 * self.exogenous["n"] / ((self.exogenous["n"] + 1) ** 2)
        )

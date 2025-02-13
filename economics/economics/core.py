import numpy as np

class Equilibrium:
  def __init__(
      self, 
      parameter, 
      exogenous
    ):
    self.parameter = parameter
    self.exogenous = exogenous
    self.endogenous = {
      "delivery": 0,
      "total_delivery": 0,
      "price_high": 0,
      "price_low": 0,
      "wholesale_price": 0,
      "quantity_high": 0,
      "quantity_low": 0
    }
    self.surplus = {
      "consumer": 0,
      "wholesaler": 0,
      "retailer": 0
    }

  def solve_vertically_integrated(self):
    self.endogenous["delivery"] = self.parameter["theta"] / 2
    self.endogenous["total_delivery"] = self.exogenous["n"] *self.parameter["theta"] / 2
    self.endogenous["price_high"] = 1 / 2
    self.endogenous["price_low"] = 1 / 2
    self.endogenous["quantity_high"] = self.exogenous["n"] / 2
    self.endogenous["quantity_low"] = 1 / 2

    self.surplus["consumer"] = (1 + self.parameter["theta"]) / 16
    self.surplus["wholesaler"] = (1 + self.parameter["theta"]) / 8

  def solve_wholesale(self):
    # \end{itemize}
    if self.parameter["theta"] >= 3:
        # p^w = 1/4
        self.endogenous["wholesale_price"] = 1 / 4

        # d^O = theta / [2 * (n + 1)]
        self.endogenous["delivery"] = self.parameter["theta"] / (2 * (self.exogenous["n"] + 1))

        # D^O = theta*n / [2 * (n + 1)]  
        self.endogenous["total_delivery"] = self.parameter["theta"]* self.exogenous["n"]/ (2 * (self.exogenous["n"] + 1))
        # price p_H^O = 1 - [n / (2 * (n + 1))]
        self.endogenous["price_high"] = 1 - (self.exogenous["n"] / (2 * (self.exogenous["n"] + 1)))

        # price p_L^O = 1 / (n + 1)
        self.endogenous["price_low"] = 1 / (self.exogenous["n"] + 1)

        # consumer surplus = (1/16)*(theta*(n^2)/((n+1)^2)) + (1/4)*(n^2/((n+1)^2))
        self.surplus["consumer"] = (
            (1 / 16)
            * (self.parameter["theta"] * (self.exogenous["n"] ** 2) / ((self.exogenous["n"] + 1) ** 2))
            + (1 / 4)
            * ((self.exogenous["n"] ** 2) / ((self.exogenous["n"] + 1) ** 2))
        )

        # (total) retailer surplus = 1/2 * [(theta + 4) / (4 * (n + 1)^2)]
        self.surplus["retailer"] = 0.5 * (
            (self.parameter["theta"] + 4)* self.exogenous["n"] / (4 * ((self.exogenous["n"] + 1) ** 2))
        )

        # wholesaler surplus = (1/4)*[theta * n / (2 * (n + 1))]
        self.surplus["wholesaler"] = (1 / 4) * (
            (self.parameter["theta"] * self.exogenous["n"])
            / (2 * (self.exogenous["n"] + 1))
        )
    if self.parameter["theta"] < 3:
      # p^w = \frac{1}{2}
      self.endogenous["wholesale_price"] = 1 / 2

      # d^O = \frac{\theta}{(n + 1)(1 + \theta)}
      self.endogenous["delivery"] = (
          self.parameter["theta"] 
          / ((self.exogenous["n"] + 1) * (1 + self.parameter["theta"]))
      )
      # D^O = \frac{n\theta}{(n + 1)(1 + \theta)}
      self.endogenous["total_delivery"] = (
          self.parameter["theta"]*self.exogenous["n"] 
          / ((self.exogenous["n"] + 1) * (1 + self.parameter["theta"]))
      )

      # p_{H}^O = 1 - \frac{n}{(n+1)(1 + \theta)}
      self.endogenous["price_high"] = 1 - (
          self.exogenous["n"] 
          / ((self.exogenous["n"] + 1) * (1 + self.parameter["theta"]))
      )

      # p_{L}^O = 1 - \frac{\theta \, n}{(n+1)(1 + \theta)}
      self.endogenous["price_low"] = 1 - (
          self.parameter["theta"] * self.exogenous["n"] 
          / ((self.exogenous["n"] + 1) * (1 + self.parameter["theta"]))
      )

      # CS^O = \frac{1}{4} \cdot \frac{n^2 \, \theta}{(n+1)^2 (1 + \theta)}
      self.surplus["consumer"] = 0.25 * (
          (self.exogenous["n"] ** 2) * self.parameter["theta"]
          / (
              (self.exogenous["n"] + 1) ** 2
              * (1 + self.parameter["theta"])
          )
      )

      # \Pi_{retailer}^O = \frac{1}{2} \cdot \frac{n \, \theta}{(n+1)^2 (1 + \theta)}
      self.surplus["retailer"] = 0.5 * (
          (
              self.exogenous["n"] 
              * self.parameter["theta"]
          )
          / (
              (self.exogenous["n"] + 1) ** 2
              * (1 + self.parameter["theta"])
          )
      )

      # \Pi_{wholesaler}^O = \frac{1}{2} \cdot \frac{n \, \theta}{(n+1)(1 + \theta)}
      self.surplus["wholesaler"] = 0.5 * (
          (
              self.exogenous["n"] 
              * self.parameter["theta"]
          )
          / (
              (self.exogenous["n"] + 1)
              * (1 + self.parameter["theta"])
          )
      )
  
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
            / (self.exogenous["n"]*(1 + self.parameter["theta"]))
        )

        # D^{max} = \frac{n\theta}{(1+\theta)}
        self.endogenous["total_delivery"] = (
            self.parameter["theta"]
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
        self.surplus["retailer"] = 0

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

        # Price $p^{max}_{H} = \frac{1}{2}$, price $p^{max}_L = \frac{1}{n+ 1}$.
        self.endogenous["price_high"] = 1 / 2
        self.endogenous["price_low"] = 1 / (self.exogenous["n"] + 1)

        # Expected consumer surplus $\frac{\theta}{16} + \frac{n^2}{4(n + 1)^2}$. 
        self.surplus["consumer"] = (
            self.parameter["theta"] / 16 + (self.exogenous["n"] ** 2) / (4 * (self.exogenous["n"] + 1) ** 2)
        )

        # The expected (total) retailer surplus is 0. 
        self.surplus["retailer"] = 0

        # The surplus for the wholesaler $\frac{\theta}{8} + \frac{1}{2}\frac{n}{(n + 1)^2}$
        self.surplus["wholesaler"] = (
            self.parameter["theta"] / 8 + 0.5 * self.exogenous["n"] / ((self.exogenous["n"] + 1) ** 2)
        )

  def solve_minimum_rpm(self):
    if self.exogenous["n"] < self.n_threshold_all():
        self.solve_wholesale()
    else:
        # \underline{p} = $\frac{1}{2}$
        self.endogenous["price_ceiling"] = 1 / 2

        # The wholesaler price  $ p_w^{min} = \frac{1}{4} + \frac{1}{4}\frac{(n - 1)(n + 1)}{n^2\theta}$ 
        self.endogenous["wholesale_price"] = 1 / 4 + 1 / 4 * (self.exogenous["n"] - 1) * (self.exogenous["n"] + 1) / (self.exogenous["n"] ** 2 * self.parameter["theta"])

        # The delivery is $d^{min} = \frac{\theta}{2(n + 1)}$. Total delivery $D^{min} = \frac{\theta n}{2(n + 1)}$. 
        self.endogenous["delivery"] = self.parameter["theta"] / (2 * (self.exogenous["n"] + 1))
        self.endogenous["total_delivery"] = self.parameter["theta"] * self.exogenous["n"] / (2 * (self.exogenous["n"] + 1))

        # Price $p^{min}_{H} = 1 - \frac{n}{2(n+1)}$, price $p^{min}_L = \frac{1}{2}$.
        self.endogenous["price_high"] =  1 - self.exogenous["n"]  /(2 * (self.exogenous["n"] + 1))
        self.endogenous["price_low"] = self.endogenous["price_ceiling"]

        # Expected consumer surplus $\frac{\theta n^2}{16(n + 1)^2} + \frac{1}{16}$. 
        self.surplus["consumer"] = (
            self.parameter["theta"] * self.exogenous["n"] ** 2 / (16 * (self.exogenous["n"] + 1) ** 2) + 1 / 16
        )

        # The expected (total) retailer surplus is $\frac{n\theta}{8(n+1)^2} + \frac{1}{8n}$. 
        self.surplus["retailer"] = (
            self.exogenous["n"] * self.parameter["theta"] / (8 * (self.exogenous["n"] + 1) ** 2) + 1 / (8 * self.exogenous["n"])
        )

        # The surplus for the wholesaler $\frac{n\theta}{8(n+1)} + \frac{1}{8}\frac{n-1}{n}$.
        self.surplus["wholesaler"] = (
            self.exogenous["n"] * self.parameter["theta"] / (8 * (self.exogenous["n"] + 1)) + (self.exogenous["n"] - 1) / (8 * self.exogenous["n"])
        )



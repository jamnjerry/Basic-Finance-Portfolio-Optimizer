This `README.md` is based on the inferred structure of a constrained portfolio optimization project following the typical breakdown of data fetching, metric calculation, and solving the optimization problem.

````markdown
# 📈 Basic Finance Portfolio Optimizer

A comprehensive Python project designed for modern portfolio management. This tool implements a **Mean-Variance Optimization** framework, specifically targeting the minimization of portfolio risk (variance) while satisfying a predefined **Target Beta** constraint.

The project uses historical stock data to calculate key financial metrics (daily returns, covariance matrix, and individual asset Betas) and then employs the `scipy.optimize` library to mathematically determine the optimal capital allocation (weights) for a multi-asset portfolio.

---

## ✨ Features

* **Market Data Fetching:** Automatically pulls historical price data from a reliable source (e.g., Yahoo Finance).
* **Risk Metrics Calculation:** Generates the **Covariance Matrix** and individual asset **Beta** values.
* **Constrained Optimization:** Solves the mathematical problem: **Minimize Portfolio Variance** subject to:
    1.  The sum of weights equals 1 (fully invested portfolio).
    2.  The weighted average portfolio Beta equals a user-defined target (market exposure control).
* **Long-Only Constraint:** Optionally enforces non-negative weights (no short selling).
* **Modular Design:** Code is separated into distinct files for data, metrics, and the solver, making it easy to extend and maintain.

---

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

* **Python 3.8+**
* **Git**

---

## 🚀 Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jamnjerry/basicfinance.git](https://github.com/jamnjerry/basicfinance.git)
    cd basicfinance
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **Windows:** `venv\Scripts\activate`
    * **macOS/Linux:** `source venv/bin/activate`

4.  **Install dependencies:**
    This project requires common data science and finance libraries.
    ```bash
    pip install pandas numpy scipy yfinance statsmodels
    ```

---

## 💻 Usage

The primary goal is to execute the optimization engine, which relies on the data and metrics generated in the preceding scripts.

### Step 1: Data Preparation

The `data_manager.py` file contains the logic to fetch and process asset returns.

### Step 2: Metrics Calculation

The `metrics_calculator.py` file computes the Covariance Matrix and individual Betas.

### Step 3: Run the Optimizer

The `optimizer_engine.py` script contains the core optimization logic. You can modify the `TARGET_BETA` variable within this script to test different risk profiles (e.g., `1.0` for market-like risk, `< 1.0` for defensive, `> 1.0` for aggressive).

```bash
python optimizer_engine.py
````

### Example Output:

The final output will display the optimal asset weights, along with the risk (Standard Deviation) and Beta of the resulting portfolio.

```
--- Running Optimization for Target Beta: 1.10 ---

✅ Optimization Complete! Optimal Weights:
  AAPL: 0.01
  MSFT: 0.14
  GOOG: 0.40
  JPM: 0.45

--- Portfolio Metrics ---
Final Standard Deviation (Risk): 0.0160
Final Portfolio Beta: 1.10(Matches Target!)
```

-----

## 📂 Project Structure Breakdown

The project is structured in a logical flow, mirroring the steps required for a sophisticated quantitative analysis.

| File Name | Role (Project Week) | Description |
| :--- | :--- | :--- |
| `data_manager.py` | **Stage 1: Data** | Fetches historical price data and transforms it into daily log returns. |
| `metrics_calculator.py` | **Stage 2: Metrics** | Calculates the **Covariance Matrix** and individual asset **Beta** values, which are inputs for the solver. |
| `optimizer_engine.py` | **Stages 3 & 4: Solver** | Defines the objective function (`portfolio_variance`) and constraints (`sum_weights`, `target_beta`), and executes the `scipy.optimize.minimize` function to find the optimal weights. |
| `streamlit_app.py` | **Stage 5: Visualization (Planned)** | *(Optional)* A web application to interactively run the optimizer and visualize the results. |
| `requirements.txt` | **Dependencies** | Lists all required Python packages. |

-----

## 🔑 Core Financial Concepts

### Covariance Matrix

A square matrix showing the covariance between all pairs of assets. In optimization, it is crucial because it captures how assets move together, allowing the solver to find the combination with the **lowest overall risk** for a given return/constraint.

### Beta ($\beta$)

A measure of the volatility, or **systematic risk**, of an individual asset or a portfolio compared to the overall market (e.g., S\&P 500).

  * **$\beta > 1$**: Asset is more volatile than the market.
  * **$\beta < 1$**: Asset is less volatile than the market.
  * **Target Beta Constraint**: This feature allows the user to control the portfolio's sensitivity to market movements, a core objective for many institutional investors.

<!-- end list -->



**Co-piloted by Gemini**
```
```

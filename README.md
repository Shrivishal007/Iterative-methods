
# Iterative Methods for Solving Linear Equations

This Python program implements **three numerical methods** for solving systems of three linear equations:
- **Gauss-Jacobi Method**
- **Gauss-Seidel Method**
- **Successive Over-Relaxation (SOR) Method**

## 🧮 Formulas Used

📘 [View all formulas Here](Formula.ipynb)

## 📋 Features

- Takes user input for coefficients and constants.
- Checks for diagonal dominance (a requirement for convergence).
- Allows choice between GJ, GS, and SOR methods.
- Accepts precision for result accuracy.
- SOR method takes `ω` (relaxation factor) as input.
- Prints each iteration in a tabular format.
- Stops when values converge or maximum iteration (20) is reached.

## 🛠️ Requirements

- Python 3.x

No external libraries are required other than the Python standard library.

## 🚀 How to Run

1. Clone this repository:
   ```
   git clone https://github.com/Shrivishal007/Iterative-methods.git
   cd Iterative-methods
   ```

2. Run the script:
   ```
   python Iterative-methods.py
   ```

3. Input the coefficients and constants for each equation when prompted.

4. Choose the method to solve the equations:
   - `GJ` for Gauss-Jacobi
   - `GS` for Gauss-Seidel
   - `SOR` for Successive Over-Relaxation

5. Enter the desired precision and, if SOR is selected, the omega value.

## ✅ Notes

- Ensure the system of equations is **diagonally dominant**.
- The program terminates after 20 iterations if convergence is not reached.

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify. 
[MIT License](LICENSE)

## 🙌 Acknowledgements

Developed as part of coursework on **Numerical Methods**.

## 🤝 Contribution

This project was developed by Shrivishal. 🙌
If you would like to contribute:
1. Fork the repository. 🍴
2. Create a new branch (git checkout -b feature-name). 🌱
3. Commit your changes (git commit -am 'Add new feature'). 📦
4. Push to the branch (git push origin feature-name). 🚀
5. Create a new Pull Request. 🔄

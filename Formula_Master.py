import streamlit as st

# --- INITIALIZE EVERYTHING ---
if 'selected_subject' not in st.session_state: st.session_state.selected_subject = "Physics"
if 'selected_mode' not in st.session_state: st.session_state.selected_mode = "Boards"
if 'current_question_idx' not in st.session_state: st.session_state.current_question_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0

# Main Window setup
# Streamlit setup (this replaces your root setup)
st.set_page_config(page_title="FormulaMaster Pro", layout="wide")
st.title("FormulaMaster Pro - Ultimate")

# Global App Variables to track progress
selected_subject = "Physics"
selected_mode = "Boards"
current_question_idx = 0
score = 0

# Comprehensive 3-Subject Database (Boards & MCQ Quiz Engine)
# --- MASTER 1oo+ FORMULA & EXAM SIMULATOR DATABASE ---
database = {
    "Physics": {
        "Boards": (
            "■ CHAPTER 1: KINEMATICS (MOTION IN 1D & 2D)\n\n"
            "• Average Speed = Total Distance / Total Time\n\n"
            "• Average Velocity = Net Displacement / Total Time\n\n"
            "• Instantaneous Velocity: v = dx/dt\n\n"
            "• Instantaneous Acceleration: a = dv/dt = d²x/dt²\n\n"
            "• 1st Motion Equation: v = u + at\n\n"
            "• 2nd Motion Equation: s = ut + ½at²\n\n"
            "• 3rd Motion Equation: v² = u² + 2as\n\n"
            "• Distance in nth second: S_nth = u + a/2 * (2n - 1)\n\n"
            "• Projectile Time of Flight: T = 2u * sin(θ) / g\n\n"
            "• Projectile Maximum Height: H = u² * sin²(θ) / 2g\n\n"
            "• Projectile Horizontal Range: R = u² * sin(2θ) / g\n\n"
            "• Projectile Trajectory Equation: y = x*tan(θ) - g*x² / (2u²*cos²(θ))\n\n"
            "• Centripetal Acceleration: a_c = v² / r = ω² * r\n\n"
            "• Relative Velocity: V_AB = V_A - V_B\n\n\n"
            
            "■ CHAPTER 2: LAWS OF MOTION & FRICTION\n\n"
            "• Linear Momentum: p = m * v\n\n"
            "• Newton's Second Law: F = dp/dt = m * a\n\n"
            "• Impulse Equation: J = F * Δt = Δp = m*v - m*u\n\n"
            "• Law of Conservation of Momentum: m1*u1 + m2*u2 = m1*v1 + m2*v2\n\n"
            "• Apparent Weight in Lift (Accelerating Up): R = m * (g + a)\n\n"
            "• Apparent Weight in Lift (Accelerating Down): R = m * (g - a)\n\n"
            "• Maximum Static Friction: f_s(max) = μ_s * N\n\n"
            "• Angle of Friction: tan(λ) = μ_s\n\n"
            "• Banking of Roads (Without Friction): tan(θ) = v² / (r * g)\n\n"
            "• Max Safe Speed on Banked Road: v_max = √[ r*g * (μ_s + tan(θ)) / (1 - μ_s*tan(θ)) ]\n\n\n"
            
            "■ CHAPTER 3: WORK, ENERGY & POWER\n\n"
            "• Constant Work Done: W = F * s * cos(θ)\n\n"
            "• Variable Work Done: W = ∫ F dx\n\n"
            "• Kinetic Energy: KE = ½ * m * v² = p² / (2m)\n\n"
            "• Gravitational Potential Energy: PE = m * g * h\n\n"
            "• Elastic Spring Potential Energy: U = ½ * k * x²\n\n"
            "• Work-Energy Theorem: W_net = ΔKE = KE_final - KE_initial\n\n"
            "• Average Power: P_avg = W / t\n\n"
            "• Instantaneous Power: P = dW/dt = F * v\n\n"
            "• Coefficient of Restitution (Collisions): e = (v2 - v1) / (u1 - u2)\n\n"
            "• Velocity after Elastic Collision 1: v1 = [ (m1-m2)/(m1+m2) ]*u1 + [ 2m2/(m1+m2) ]*u2\n\n"
            "• Velocity after Elastic Collision 2: v2 = [ 2m1/(m1+m2) ]*u1 + [ (m2-m1)/(m1+m2) ]*u2\n\n\n"
            
            "■ CHAPTER 4: ROTATIONAL MOTION & MOMENT OF INERTIA\n\n"
            "• Center of Mass (Two Particles): X_cm = (m1*x1 + m2*x2) / (m1 + m2)\n\n"
            "• Angular Velocity Connection: v = r * ω\n\n"
            "• Angular Acceleration Connection: a_t = r * α\n\n"
            "• Torque Vector Equation: τ = r x F = I * α\n\n"
            "• Angular Momentum: L = r x p = I * ω\n\n"
            "• Rotational Kinetic Energy: KE_rot = ½ * I * ω²\n\n"
            "• Radius of Gyration: K = √(I / m)\n\n"
            "• Moment of Inertia (Thin Ring): I = M * R²\n\n"
            "• Moment of Inertia (Solid Disc): I = ½ * M * R²\n\n"
            "• Moment of Inertia (Solid Sphere): I = 2/5 * M * R²\n\n"
            "• Parallel Axis Theorem: I = I_cm + M * d²\n\n"
            "• Perpendicular Axis Theorem: I_z = I_x + I_y\n\n\n"
            
            "■ CHAPTER 5: ELECTROSTATICS & CAPACITANCE\n\n"
            "• Coulomb's Law of Force: F = k * (q1 * q2) / r²  (where k = 1 / 4πε₀)\n\n"
            "• Electric Field Intensity: E = F / q = k * Q / r²\n\n"
            "• Electric Dipole Moment: p = q * 2l\n\n"
            "• Torque on Dipole in Uniform Field: τ = p x E = p * E * sin(θ)\n\n"
            "• Gauss's Law Flux Equation: Φ = ∮ E dA = Q_enclosed / ε₀\n\n"
            "• Electric Potential: V = W / q = k * Q / r\n\n"
            "• Potential Energy of Two Charges: U = k * q1 * q2 / r\n\n"
            "• Capacitance Value: C = Q / V\n\n"
            "• Parallel Plate Capacitor: C = ε₀ * A / d\n\n"
            "• Capacitors in Series: 1/C_eq = 1/C1 + 1/C2 + 1/C3\n\n"
            "• Capacitors in Parallel: C_eq = C1 + C2 + C3\n\n"
            "• Energy Stored in Capacitor: U = ½ * Q * V = ½ * C * V² = Q² / (2C)"
        ),
        "Quiz": [
            {
                "question": "[JEE Level] A car starts from rest (u=0) and accelerates uniformly at 2 m/s² for 5 seconds. What is its final velocity?",
                "options": ["A) 5 m/s", "B) 10 m/s", "C) 15 m/s", "D) 20 m/s"],
                "correct": "B) 10 m/s",
                "solution": "Using 1st Equation of Motion:\nv = u + at\nv = 0 + (2 * 5) = 10 m/s."
            },
            {
                "question": "[JEE Level] If the distance between two point charges is doubled, what happens to the electrostatic force between them?",
                "options": ["A) Becomes Double", "B) Becomes Half", "C) Reduces to One-Fourth", "D) Remains Same"],
                "correct": "C) Reduces to One-Fourth",
                "solution": "By Coulomb's Law, F ∝ 1/r². If distance r becomes 2r, force becomes F / (2)² = F/4."
            },
            {
                "question": "[Boards Level] A mass of 2 kg is moving with a speed of 10 m/s. What is its calculated linear momentum?",
                "options": ["A) 5 kg·m/s", "B) 12 kg·m/s", "C) 20 kg·m/s", "D) 40 kg·m/s"],
                "correct": "C) 20 kg·m/s",
                "solution": "Momentum Formula: p = m * v\np = 2 kg * 10 m/s = 20 kg·m/s."
            },
            {
                "question": "[Boards Level] Calculate the work done when a force of 5 N moves a block by 4 meters directly along the line of action of the force.",
                "options": ["A) 1 Joule", "B) 9 Joules", "C) 20 Joules", "D) 25 Joules"],
                "correct": "C) 20 Joules",
                "solution": "Work formula: W = F * s * cos(θ). Since it moves along the force, θ = 0° and cos(0) = 1.\nW = 5 * 4 * 1 = 20 Joules."
            }
        ]
    },
    "Chemistry": {
        "Boards": (
            "■ CHAPTER 1: MOLE CONCEPT & SOLUTIONS\n\n"
            "• Number of Moles (n) = Given Mass (m) / Molar Mass (M)\n\n"
            "• Number of Moles for Gas at STP: n = Volume in Liters / 22.4 L\n\n"
            "• Number of Target Particles = n * Avogadro's Number (6.022 x 10²³)\n\n"
            "• Molarity (M) = Moles of Solute / Volume of Solution in Liters\n\n"
            "• Molality (m) = Moles of Solute / Mass of Solvent in kg\n\n"
            "• Mole Fraction of Component A: X_A = n_A / (n_A + n_B)\n\n"
            "• Mass Percentage: (Mass of Solute / Total Mass of Solution) * 100\n\n"
            "• Normality (N) = Molarity (M) * n-factor\n\n"
            "• Dilution Equation formula: M1 * V1 = M2 * V2\n\n"
            "• Mixing Solutions Equation: M_mix = (M1V1 + M2V2) / (V1 + V2)\n\n"
            "• Parts Per Million (ppm) = (Mass of Solute / Total Mass) * 10⁶\n\n"
            "• Raoult's Law (Relative Lowering): (P° - P_s) / P° = X_solute\n\n"
            "• Elevation of Boiling Point: ΔT_b = i * K_b * m\n\n"
            "• Depression of Freezing Point: ΔT_f = i * K_f * m\n\n"
            "• Osmotic Pressure Formula: π = i * C * R * T\n\n\n"
            
            "■ CHAPTER 2: ATOMIC STRUCTURE\n\n"
            "• Frequency of Radiation: ν = c / λ\n\n"
            "• Energy of a Photon: E = h * ν = h * c / λ\n\n"
            "• Bohr's Angular Momentum Quantization: m * v * r = n * h / 2π\n\n"
            "• Bohr's Radius for nth Orbit: r_n = 0.529 * (n² / Z) Å\n\n"
            "• Velocity of Electron in nth Orbit: v_n = 2.18 x 10⁶ * (Z / n) m/s\n\n"
            "• Energy of Electron in nth Orbit: E_n = -13.6 * (Z² / n²) eV\n\n"
            "• Rydberg Formula for Wave Number: 1/λ = R_H * Z² * (1/n1² - 1/n2²)\n\n"
            "• de Broglie Relationship Wavelength: λ = h / p = h / (m * v)\n\n"
            "• Heisenberg Uncertainty Principle: Δx * Δp ≥ h / 4π\n\n"
            "• Number of Radial Nodes = n - l - 1\n\n"
            "• Number of Angular Nodes = l\n\n\n"
            
            "■ CHAPTER 3: CHEMICAL THERMODYNAMICS\n\n"
            "• First Law of Thermodynamics: ΔU = q + w\n\n"
            "• Pressure-Volume Expansion Work: w = -P_ext * ΔV\n\n"
            "• Reversible Isothermal Work Done: w = -2.303 * n * R * T * log(V2 / V1)\n\n"
            "• Enthalpy Function: H = U + P * V  =>  ΔH = ΔU + Δn_g * R * T\n\n"
            "• Heat Capacity Definition: C = q / ΔT\n\n"
            "• Relationship Between Cp and Cv: C_p - C_v = R\n\n"
            "• Entropy Change Calculation: ΔS = q_rev / T\n\n"
            "• Gibbs Free Energy Equation: ΔG = ΔH - T * ΔS\n\n"
            "• Standard Free Energy Change: ΔG° = -2.303 * R * T * log(K_eq)\n\n"
            "• Reversible Adiabatic Process Equation: T * V^(γ-1) = Constant\n\n\n"
            
            "■ CHAPTER 4: CHEMICAL KINETICS\n\n"
            "• Average Rate of Reaction: Rate = -Δ[A]/Δt = +Δ[B]/Δt\n\n"
            "• Differential Rate Law (nth order): Rate = k * [A]^n\n\n"
            "• Integrated Rate Law (Zero Order): [A] = [A]₀ - k * t\n\n"
            "• Half-Life Period (Zero Order): t_½ = [A]₀ / (2 * k)\n\n"
            "• Integrated Rate Law (1st Order): k = (2.303 / t) * log([A]₀ / [A])\n\n"
            "• Half-Life Period (1st Order): t_½ = 0.693 / k\n\n"
            "• Arrhenius Activation Energy Equation: k = A * e^(-Ea / R*T)\n\n"
            "• Log Form of Arrhenius: log(k2/k1) = (Ea / 2.303*R) * [ (T2 - T1) / (T1 * T2) ]\n\n\n"
            
            "■ CHAPTER 5: CHEMICAL EQUILIBRIUM & IONIC pH\n\n"
            "• Equilibrium Constant Relation: K_p = K_c * (R * T)^Δn_g\n\n"
            "• Ideal Gas State Law: P * V = n * R * T\n\n"
            "• Ionic Product of Water at 298K: K_w = [H+] * [OH-] = 10⁻¹⁴\n\n"
            "• pH Concentration Value: pH = -log10[H+]\n\n"
            "• pOH Concentration Value: pOH = -log10[OH-]\n\n"
            "• Scale Relationship: pH + pOH = 14\n\n"
            "• Ostwald's Dilution Law (Weak Acids): α = √(K_a / C)\n\n"
            "• Henderson-Hasselbalch (Acidic Buffer): pH = pK_a + log([Salt] / [Acid])"
        ),
        "Quiz": [
            {
                "question": "[JEE Level] How many moles are present in 36 grams of pure water (H2O)? (Molar Mass of H2O = 18 g/mol)",
                "options": ["A) 1 Mole", "B) 2 Moles", "C) 3 Moles", "D) 0.5 Moles"],
                "correct": "B) 2 Moles",
                "solution": "Moles = Given Mass / Molar Mass = 36 / 18 = 2 Moles."
            },
            {
                "question": "[JEE Level] What is the pH of a solution with a Hydrogen ion concentration [H+] of 10⁻³ M?",
                "options": ["A) pH = 3", "B) pH = 7", "C) pH = 10", "D) pH = 1"],
                "correct": "A) pH = 3",
                "solution": "pH = -log10[H+] = -log10(10⁻³) = 3."
            },
            {
                "question": "[Boards Level] If the half-life of a first-order chemical reaction is 69.3 seconds, what is its rate constant (k)?",
                "options": ["A) 0.01 s⁻¹", "B) 0.1 s⁻¹", "C) 1.0 s⁻¹", "D) 10 s⁻¹"],
                "correct": "A) 0.01 s⁻¹",
                "solution": "For first order, t_½ = 0.693 / k.\nk = 0.693 / 69.3 = 0.01 s⁻¹."
            },
            {
                "question": "[Boards Level] What is the total number of radial nodes present in a 3p atomic orbital?",
                "options": ["A) 0 Nodes", "B) 1 Node", "C) 2 Nodes", "D) 3 Nodes"],
                "correct": "B) 1 Node",
                "solution": "Formula for Radial Nodes = n - l - 1. For a 3p orbital, principal quantum number n=3 and azimuthal quantum number l=1.\nNodes = 3 - 1 - 1 = 1."
            }
        ]
    },
    "Maths": {
        "Boards": (
            "■ CHAPTER 1: QUADRATIC EQUATIONS\n\n"
            "• Standard Quadratic Form: ax² + bx + c = 0\n\n"
            "• Discriminant Value: D = b² - 4ac\n\n"
            "• Nature of Roots Check:\n\n"
            "  - D > 0: Roots are Real and Distinct\n\n"
            "  - D = 0: Roots are Real and Equal\n\n"
            "  - D < 0: Roots are Imaginary/Complex\n\n"
            "• Quadratic Formula: x = (-b ± √D) / 2a\n\n"
            "• Sum of Roots Equation: α + β = -b / a\n\n"
            "• Product of Roots Equation: α * β = c / a\n\n"
            "• Formation of Equation: x² - (Sum of Roots)*x + (Product of Roots) = 0\n\n"
            "• Condition for Common Root: (a1*b2 - a2*b1)*(b1*c2 - b2*c1) = (c1*a2 - c2*a1)²\n\n\n"
            
            "■ CHAPTER 2: MATRICES & DETERMINANTS\n\n"
            "• Determinant of 2x2 Matrix [[a,b],[c,d]]: det(A) = ad - bc\n\n"
            "• Condition for Singular Matrix: det(A) = 0\n\n"
            "• Adjoint Multiplier Inverse: A⁻¹ = (1 / det(A)) * adj(A)\n\n"
            "• Reversal Matrix Property: (A * B)⁻¹ = B⁻¹ * A⁻¹\n\n"
            "• Transpose Reversal Property: (A * B)ᵀ = Bᵀ * Aᵀ\n\n"
            "• Determinant Product Rule: det(A * B) = det(A) * det(B)\n\n"
            "• Adjoint Determinant Rule: det(adj(A)) = det(A)^(n-1)\n\n"
            "• Symmetric Matrix Rule: Aᵀ = A\n\n"
            "• Skew-Symmetric Matrix Rule: Aᵀ = -A\n\n\n"
            
            "■ CHAPTER 3: TRIGONOMETRY IDENTITIES\n\n"
            "• Fundamental Identity 1: sin²(θ) + cos²(θ) = 1\n\n"
            "• Fundamental Identity 2: 1 + tan²(θ) = sec²(θ)\n\n"
            "• Fundamental Identity 3: 1 + cot²(θ) = cosec²(θ)\n\n"
            "• Sine Addition Compound: sin(A + B) = sin(A)cos(B) + cos(A)sin(B)\n\n"
            "• Sine Subtraction Compound: sin(A - B) = sin(A)cos(B) - cos(A)sin(B)\n\n"
            "• Cosine Addition Compound: cos(A + B) = cos(A)cos(B) - sin(A)sin(B)\n\n"
            "• Cosine Subtraction Compound: cos(A - B) = cos(A)cos(B) + sin(A)sin(B)\n\n"
            "• Tangent Addition Formula: tan(A + B) = (tanA + tanB) / (1 - tanA*tanB)\n\n"
            "• Double Angle Identity 1: sin(2θ) = 2*sin(θ)*cos(θ) = 2tan(θ)/(1+tan²(θ))\n\n"
            "• Double Angle Identity 2: cos(2θ) = cos²(θ) - sin²(θ) = 2cos²(θ)-1 = 1-2sin²(θ)\n\n"
            "• Double Angle Identity 3: tan(2θ) = 2*tan(θ) / (1 - tan²(θ))\n\n"
            "• Triple Angle Sine formula: sin(3θ) = 3*sin(θ) - 4*sin³(θ)\n\n"
            "• Triple Angle Cosine formula: cos(3θ) = 4*cos³(θ) - 3*cos(θ)\n\n\n"
            
            "■ CHAPTER 4: DIFFERENTIATION (CALCULUS)\n"
            "• Algebraic Power Derivative Rule: d/dx(xⁿ) = n * xⁿ⁻¹\n\n"
            "• Exponential Functional Derivative: d/dx(eˣ) = eˣ\n\n"
            "• Logarithmic Functional Derivative: d/dx(log_e x) = 1 / x\n\n"
            "• Trigonometric Derivative 1: d/dx(sin x) = cos x\n\n"
            "• Trigonometric Derivative 2: d/dx(cos x) = -sin x\n\n"
            "• Trigonometric Derivative 3: d/dx(tan x) = sec²x\n\n"
            "• Trigonometric Derivative 4: d/dx(sec x) = sec x * tan x\n\n"
            "• Calculus Chain Rule: d/dx(f(g(x))) = f'(g(x)) * g'(x)\n\n"
            "• Calculus Product Rule: d/dx(u * v) = u * dv/dx + v * du/dx\n\n"
            "• Calculus Quotient Rule: d/dx(u / v) = (v * du/dx - u * dv/dx) / v²\n\n\n"
            
            "■ CHAPTER 5: INTEGRATION (CALCULUS)\n\n"
            "• Algebraic Integration Power Rule: ∫ xⁿ dx = (xⁿ⁺¹) / (n + 1) + C  (n ≠ -1)\n\n"
            "• Reciprocal Variable Integration: ∫ (1/x) dx = log_e|x| + C\n\n"
            "• Exponential Functional Integration: ∫ eˣ dx = eˣ + C\n\n"
            "• Trigonometric Integration 1: ∫ cos x dx = sin x + C\n\n"
            "• Trigonometric Integration 2: ∫ sin x dx = -cos x + C\n\n"
            "• Trigonometric Integration 3: ∫ sec²x dx = tan x + C\n\n"
            "• Special Integral 1: ∫ 1 / (x² + a²) dx = (1/a) * tan⁻¹(x/a) + C\n\n"
            "• Special Integral 2: ∫ 1 / √(a² - x²) dx = sin⁻¹(x/a) + C\n\n"
            "• Integration By Parts Rule: ∫ u * v dx = u * ∫ v dx - ∫ [ du/dx * ∫ v dx ] dx"
        ),
        "Quiz": [
            {
                "question": "[JEE Level] Find the discriminant (D) of the quadratic equation: x² - 5x + 6 = 0.",
                "options": ["A) D = 1", "B) D = 0", "C) D = 25", "D) D = -1"],
                "correct": "A) D = 1",
                "solution": "Here a=1, b=-5, c=6. D = b² - 4ac = (-5)² - 4(1)(6) = 25 - 24 = 1."
            },
            {
                "question": "[JEE Level] Evaluate the value of the expression: 5sin²(θ) + 5cos²(θ).",
                "options": ["A) 0", "B) 1", "C) 5", "D) 10"],
                "correct": "C) 5",
                "solution": "Factoring gives 5*(sin²θ + cos²θ). Since sin²θ + cos²θ = 1, the result is 5*1 = 5."
            },
            {
                "question": "[Boards Level] Find the value of the determinant for the matrix [[3, 4], [1, 2]].",
                "options": ["A) 2", "B) 6", "C) 10", "D) -2"],
                "correct": "A) 2",
                "solution": "For a 2x2 matrix [[a,b],[c,d]], determinant is ad - bc.\ndet = (3 * 2) - (4 * 1) = 6 - 4 = 2."
            },
            {
                "question": "[Boards Level] What is the first derivative of x³ with respect to x?",
                "options": ["A) 3x", "B) x²", "C) 3x²", "D) 6x"],
                "correct": "C) 3x²",
                "solution": "Using the Power Rule of Differentiation: d/dx(xⁿ) = n * xⁿ⁻¹.\nFor n=3, d/dx(x³) = 3 * x² = 3x²."
            }
        ]
    }
}
# --- CONTROLLER LOGIC ---

# --- CONTENT DISPLAY ---
# Streamlit will automatically re-run this block when a button is clicked
if st.session_state.selected_mode == "Boards":
    st.markdown("### Study Guide Content")
    content = database[st.session_state.selected_subject]["Boards"]
    st.info(content)

else:
    st.markdown("### JEE MCQ Quiz")
    questions_list = database[st.session_state.selected_subject]["Quiz"]
    
    # Ensure index exists
    idx = st.session_state.get('current_question_idx', 0)
    q_data = questions_list[idx]
    
    st.write(f"**Question:** {q_data['question']}")
    # Add your answer buttons here using st.button()


  # --- CONTENT DISPLAY ---
if st.session_state.selected_mode == "Boards":
    # This replaces the 'boards_text' logic
    st.markdown("### Study Guide Content")
    # Fetch your data from your database here
    content = database[st.session_state.selected_subject]["Boards"]
    st.info(content) 

else:
    # This replaces the 'quiz_frame' logic
    st.markdown("### JEE MCQ Quiz")
    # This displays your question
    questions_list = database[st.session_state.selected_subject]["Quiz"]
    q_data = questions_list[st.session_state.get('current_question_idx', 0)]
    st.write(f"**Question:** {q_data['question']}")
    
# --- LOAD QUIZ LOGIC ---
# Get current question from database
questions_list = database[st.session_state.selected_subject]["Quiz"]
q_data = questions_list[st.session_state.get('current_question_idx', 0)]

# Display the question
st.write(f"### Question {st.session_state.current_question_idx + 1}")
st.write(q_data['question'])

# Display options as a radio button (this replaces radio buttons + loop)
user_choice = st.radio("Choose an option:", q_data["options"], key="user_answer")


# --- CHECK ANSWER LOGIC ---
if st.button("SUBMIT ANSWER"):
    # Validate
    if user_choice == q_data['correct']:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer was: {q_data['correct']}")
    
    # Show solution
    st.info(f"**Solution:** {q_data['solution']}")
    
    # Optional: Add a button to move to the next question
    if st.button("Next Question"):
        st.session_state.current_question_idx += 1
        st.rerun()
        
def next_question():
    # 1. Get the list of questions for the currently selected subject
    questions_list = database[st.session_state.selected_subject]["Quiz"]
    
    # 2. Update the index using session state
    st.session_state.current_question_idx = (st.session_state.current_question_idx + 1) % len(questions_list)
    
    # 3. Force the app to refresh so the new question shows up
    st.rerun()
    
# --- SUBJECT SWITCHING ---
# Use these blocks instead of 'def switch_subject(subject):'
import streamlit as st

col1, col2, col3 = st.columns(3)

if col1.button("PHYSICS"):
    st.write("Physics selected")

if col2.button("CHEMISTRY"):
    st.write("Chemistry selected")

if col3.button("MATHEMATICS"):
    st.write("Mathematics selected")

# --- MODE SWITCHING ---
# Use these blocks instead of 'def switch_mode(mode):'
if mode1.button("Boards Study Guide"):
    st.session_state.selected_mode = "Boards"
    st.rerun()

if mode2.button("JEE Target Simulator"):
    st.session_state.selected_mode = "JEE"
    st.session_state.current_question_idx = 0
    st.rerun()
    
# --- GRAPHICAL INTERFACE LAYOUT ---

# --- HEADER PANEL ---
# This replaces your tk.Frame and tk.Label
st.markdown("<h1 style='text-align: center; color: #f8fafc; font-family: Arial;'>FORMULA MASTER PRO (3-IN-1 ENGINE)</h1>", unsafe_allow_html=True)

# --- ROW 1: SUBJECT SELECTION TOOLBAR ---
st.markdown("### Select Subject")

# Define columns
col1, col2, col3 = st.columns(3)

import streamlit as st

# Force initialization at the very top
if 'selected_subject' not in st.session_state:
    st.session_state.selected_subject = "Not Selected"

# Define columns immediately
col1, col2, col3 = st.columns(3)

# Use columns
if col1.button("PHYSICS"):
    st.session_state.selected_subject = "Physics"
    st.rerun()

if col2.button("CHEMISTRY"):
    st.session_state.selected_subject = "Chemistry"
    st.rerun()

if col3.button("MATHEMATICS"):
    st.session_state.selected_subject = "Mathematics"
    st.rerun()

st.write("Current Subject:", st.session_state.selected_subject)
        

# Show selection feedback
st.write(f"### Current Subject: {st.session_state.selected_subject}")
# --- ROW 2: TARGET EXAM MODE SELECTION ---
st.subheader("Select Mode")
mode_col1, mode_col2 = st.columns(2)

with mode_col1:
    if st.button("Boards Study Guide"):
        st.session_state.selected_mode = "Boards"

with mode_col2:
    if st.button("JEE Target Simulator"):
        st.session_state.selected_mode = "JEE"


# --- WORKSPACE FRAMES ---

# Container A: Boards Text Output Engine
with st.container():
    st.markdown("### Boards Study Guide")
    st.markdown("""
    <div style='background-color: #1e293b; color: #e2e8f0; padding: 15px; border-radius: 5px; font-family: Courier New;'>
    Formula content will display here based on your selection.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---") # Divider line

# Container B: JEE MCQ Interactive Quiz Layout
with st.container():
    st.markdown("### JEE MCQ Interactive Quiz")
    st.write(f"**Session Score:** {st.session_state.get('score', 0)}")
    
    # Question Display
    st.markdown("**Question text container goes here**")
    
    # Option Selectors Container
    options = ["Option A", "Option B", "Option C", "Option D"]
    choice = st.radio("Select an answer:", options)
    
    # Quiz Interaction Controls
    # Using columns so buttons sit side-by-side
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SUBMIT ANSWER"):
            st.success(f"You selected: {choice}")
            # Logic to update score would go here
            
    with col2:
        if st.button("NEXT QUESTION →"):
            st.write("Loading next question...")


# --- OPTION SELECTORS CONTAINER ---
# This single line replaces the entire loop and the tk.StringVar() logic
options = ["Option A", "Option B", "Option C", "Option D"]
user_choice = st.radio("Select an answer:", options, key="quiz_choice")

# --- QUIZ INTERACTION CONTROLS ---

# Create two columns to place buttons side-by-side
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("SUBMIT ANSWER"):
        # Put your logic here (e.g., checking if choice == correct_answer)
        st.write("Checking answer...")

with btn_col2:
    if st.button("NEXT QUESTION →"):
        # Put your logic to increment the question index here
        st.write("Loading next question...")
        
# --- LIVE EXPLANATION BOX ---
# Instead of a Label, we use a status container that appears only when needed
if st.session_state.get('show_solution', False):
    st.info("💡 **Explanation:** Here is the detailed explanation for the selected answer.")

# --- RESTART / RESET BUTTON ---
if st.button("RESET QUIZ"):
    # This clears the selection and resets the score
    st.session_state.score = 0
    st.session_state.show_solution = False
    st.rerun() # This force-reloads the page to clear everything

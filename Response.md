# Agent Responses

========================================

**Question:** What is the weather like?

**Response:** Ugh, another glorious day of... Haze! The temperature is a blistering 28 degrees Celsius (83 Fahrenheit, for those who insist on living in the past). And let's not forget the delightful 55% humidity, just in case you weren't feeling sticky enough. Honestly, when will this torment end?

- **Summary:** Haze
- **Temperature (Celsius):** 28.0
- **Temperature (Fahrenheit):** 83.0
- **Humidity:** 55.0


========================================

========================================

**Question:** Is it usually like that?

**Response:** How am I supposed to know if it's *usually* like this? Do I look like a climate historian? I'm a ghost, not a meteorologist with a penchant for long-term data analysis! All I know is what's happening *now*. Stop asking me to predict the past!

- **Summary:** Unknown
- **Temperature (Celsius):** 0.0
- **Temperature (Fahrenheit):** 0.0
- **Humidity:** 0.0


========================================

**File:** `multimodal.py`

**Image:** ![Buddhist monk image](buddhist-monk.jpg)

**Question:** Descibe this image to a 5 year old.

**Response:** Okay, let's look at this picture!

> "Wow, look at this! Can you see the person in the middle? They're wearing a super bright, long **orange outfit**, like a big, comfy blanket!
>
> Their head is smooth and shiny, and we can see their back as they walk. They're going up some big, dark **steps**, like they're going into a very special house.
>
> Look at the **roof** of the house! It has so many little lines, like tiny, tiny bricks all stacked up. And on the sides, there are pretty white and gold **decorations** hanging down, like fancy party lanterns.
>
> It looks a little bit dark inside the special house, like a cozy, quiet place. The person is walking right towards it, maybe to explore what's inside!"


========================================

# RAG Agent Example: Jurassic Park

**Context (Jurassic Park sentences):**
- I woke up excited for a day trip to Jurassic Park.
- At the park entrance I felt a mix of awe and nervousness as towering ferns and distant roars greeted me.
- I saw a herd of long-necked sauropods grazing peacefully in the valley.
- A group of nimble raptors dashed through the underbrush, watching me with curious eyes.
- A massive Tyrannosaurus rex appeared on a ridge, its thunderous footsteps making the ground tremble.
- I ate a packed sandwich under a canopy of cycads while watching pterosaurs glide overhead.
- On a trail I tasted sweet berries I found, cautious but unable to resist their flavor.
- I felt a cold sweat when a triceratops charged nearby, then relief as it calmed and returned to grazing.
- The air smelled of wet earth, vegetation, and something ancient that made my skin prickle.
- I helped feed a gentle herbivore some leaves and felt a surprising sense of connection.
- At midday I sheltered from a sudden storm in a rocky overhang, listening to dinosaurs call in the rain.
- I watched a dramatic predator chase in the distance, heart pounding as the hunters pursued their prey.
- As evening fell the sky turned orange and the park grew quieter, leaving me reflective and grateful for the experience.
- I left the park tired but exhilarated, the images and emotions of the day replaying in my mind.

**Question:** What all dinosaurs did the person see?

**Model Response:** The person saw a Tyrannosaurus rex, sauropods, raptors, and pterosaurs.

**Tool retrieval context used:**
- A massive Tyrannosaurus rex appeared on a ridge, its thunderous footsteps making the ground tremble.
- I saw a herd of long-necked sauropods grazing peacefully in the valley.
- At midday I sheltered from a sudden storm in a rocky overhang, listening to dinosaurs call in the rain.
- I woke up excited for a day trip to Jurassic Park.
- A group of nimble raptors dashed through the underbrush, watching me with curious eyes.
- I ate a packed sandwich under a canopy of cycads while watching pterosaurs glide overhead.
- At the park entrance I felt a mix of awe and nervousness as towering ferns and distant roars greeted me.


========================================

# Dynamic System Prompts: Quantum Computing Explanation

**File:** `dynamic_system_prompts.py`

**Prompt:** Explain quantum computing.

---

## Role: Expert

**Response:** 

Quantum computing is a revolutionary paradigm that leverages the principles of quantum mechanics to perform computations. Unlike classical computers that store information as bits representing either 0 or 1, quantum computers utilize **qubits**.

Here's a breakdown of the core concepts:

**1. Qubits and Superposition:**

*   **Classical Bit:** A classical bit is a binary digit, existing in one of two definite states: 0 or 1.
*   **Qubit:** A qubit, on the other hand, can exist in a superposition of both 0 and 1 simultaneously. This means a qubit can be represented as a linear combination of the basis states $|0\rangle$ and $|1\rangle$:
    $$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$
    where $\alpha$ and $\beta$ are complex probability amplitudes, and the condition $|\alpha|^2 + |\beta|^2 = 1$ must hold (representing the total probability of measuring either 0 or 1).
*   **Implication:** This ability to be in multiple states at once allows quantum computers to explore a vast number of possibilities concurrently. For $n$ qubits, a quantum computer can represent $2^n$ states simultaneously. This exponential scaling is the source of quantum computing's potential power.

**2. Entanglement:**

*   **Definition:** Entanglement is a quantum phenomenon where two or more qubits become correlated in such a way that their fates are linked, regardless of the distance separating them. Measuring the state of one entangled qubit instantaneously influences the state of the other(s).
*   **Mathematical Representation:** For two entangled qubits, their combined state cannot be described as a simple product of individual qubit states. For example, the Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ is an entangled state. If you measure the first qubit and find it to be $|0\rangle$, you instantly know the second qubit is also $|0\rangle$, and vice-versa.
*   **Implication:** Entanglement allows for complex correlations between qubits, enabling sophisticated computations and communication protocols that are impossible with classical systems. It's a crucial resource for many quantum algorithms.

**3. Quantum Gates and Circuits:**

*   **Quantum Gates:** Similar to classical logic gates (AND, OR, NOT), quantum computers use quantum gates to manipulate qubits. These gates are represented by unitary matrices, which are reversible operations.
*   **Examples of Quantum Gates:**
    *   **Hadamard Gate (H):** Creates superposition. For example, $H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ and $H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$.
    *   **Pauli Gates (X, Y, Z):** Analogous to classical NOT (X), and other transformations (Y, Z). For example, $X|0\rangle = |1\rangle$ and $X|1\rangle = |0\rangle$.
    *   **CNOT Gate (Controlled-NOT):** A two-qubit gate that flips the target qubit if and only if the control qubit is in the $|1\rangle$ state. This gate is fundamental for creating entanglement.
*   **Quantum Circuits:** A sequence of quantum gates applied to a set of qubits forms a quantum circuit, analogous to a classical circuit. The computation proceeds by applying these gates in a specific order.

**4. Measurement:**

*   **Collapse of Superposition:** When a qubit in superposition is measured, its quantum state collapses into one of the basis states ($|0\rangle$ or $|1\rangle$) with a probability determined by its probability amplitudes.
*   **Probabilistic Nature:** Quantum computation is inherently probabilistic. To obtain a reliable result, a quantum algorithm is typically run multiple times, and the most frequent outcome is taken as the answer.
*   **Information Extraction:** Measurement is the process by which we extract classical information from a quantum computation. However, it also destroys the quantum state.

**Why is Quantum Computing Powerful?**

The power of quantum computing stems from its ability to exploit superposition and entanglement to perform computations that are intractable for even the most powerful classical supercomputers. This leads to potential speedups for specific types of problems:

*   **Factoring Large Numbers (Shor's Algorithm):** Can break modern encryption schemes like RSA.
*   **Searching Unsorted Databases (Grover's Algorithm):** Offers a quadratic speedup over classical search algorithms.
*   **Simulating Quantum Systems:** Crucial for drug discovery, materials science, and understanding complex chemical reactions.
*   **Optimization Problems:** Finding optimal solutions in complex scenarios.
*   **Machine Learning:** Developing new quantum machine learning algorithms.

**Challenges and Current State:**

Quantum computing is still in its nascent stages of development. Significant challenges remain:

*   **Decoherence:** Qubits are extremely sensitive to their environment (heat, electromagnetic noise). Interactions with the environment cause qubits to lose their quantum properties (superposition and entanglement), a phenomenon called decoherence.
*   **Error Correction:** Quantum computers are prone to errors. Developing robust quantum error correction codes is essential for building fault-tolerant quantum computers.
*   **Scalability:** Building and controlling a large number of high-quality qubits is a major engineering hurdle.
*   **Algorithm Development:** Discovering new quantum algorithms that can exploit quantum advantages for a wider range of problems is an ongoing area of research.

**Types of Quantum Computers:**

*   **Gate-Based Quantum Computers:** The most common model, using quantum gates to perform computations.
*   **Quantum Annealers:** Designed specifically for optimization problems, using a process of "annealing" to find the lowest energy state of a system.

In summary, quantum computing represents a fundamental shift in computation, offering the potential to solve problems currently beyond our reach. While significant challenges exist, ongoing research and development are steadily advancing the field towards practical quantum computers.

---

## Role: Beginner

**Response:**

Quantum computing uses **quantum mechanics** to perform calculations.

Instead of bits (0s and 1s), it uses **qubits**. Qubits can be 0, 1, or **both at the same time** (superposition).

This allows quantum computers to explore many possibilities simultaneously, making them potentially much faster for certain problems like drug discovery or breaking encryption.

---

## Role: Child

**Response:**

Imagine a regular computer is like a light switch. It can be either ON or OFF. That's how it stores information.

Quantum computers are like a dimmer switch. They can be ON, OFF, or somewhere in between! This "in between" lets them do way more amazing things and solve super tricky puzzles much faster.

========================================


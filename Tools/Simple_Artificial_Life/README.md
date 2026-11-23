## Simple Artifical Life Simulation
A simple 2D artificial life simulation built from scratch using C.

### Overview
This project explores the basic concepts of artificial life by simulating organisms living and moving inside a 2D grid environment.

Each organism has its own position and movement behavior. The simulation continuously updates the enviornment and displays the organisms in real time.

### Features
- **[+] 2D grid-based environment**
- **[+] Multiple organisms**
- **Random movement**
- **Boundary detection**

### Technologies
- **C**
- **Standard C Library**
- **Windows API**

### How it Works
The simulation uses a continuous game loop:
  1. Update organism positions
  2. Check movement boundaries
  3. Update the environment
  4. Render the grid
  5. Repeat

### Installation and Execution
Clone the repository and go to the project directory.

Compile:

On linux:

    gcc Alife.c -o Alife && ./Alife

On Windows:

    gcc Alife.c -o Alife.exe

    Alife.exe

### Features Improvemnts
- Organism aging and lifespan management
- Reproduction and population growth
- Food and Energy systems
- More complex organis behaviors
- Natural selection and evolution
- Improved graphical visulization


### Learning Objectives
This project helps explore:
- Structures and arrays in C
- Random number generation
- 2D Arrays
- Simulation loops
- Basic Artificial Life concepts

### Author
**A personal programming project exploring artificial life and simulation development**

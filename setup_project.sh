#!/bin/bash
echo "Setting up project..."
mkdir -p src data output
chmod +x setup_project.sh # make the script executable 

# create student.csv untill encountering EOF --> end of file
cat > data/student.csv << 'EOF'
name,age,grade,subject
Alice,20,85, math, 
Bob,19,92,french, 
Kate,21,79, math,
Alex, 20, 79, math,
Lily, 22, 100, physics,
Liz,23, 88, english,
Bernie, 87, physics

EOF
cat data/student.csv.csv

# src/data_analysis.py
cat > src/data_analysis.py << 'EOF'
# data analysis to do...

EOF
cat src/data_analysis.py

# src/data_analysis_function.py
cat > src/data_analysis_function.py << 'EOF'
# functions for data analysis

EOF

touch .gitignore # simple way to create an empty .gitignore file

cat src/data_analysis_function.py

# output/
cat > output/ << 'EOF'
# output

EOF
cat output/
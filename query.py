import csv

def generate_query_formula(csv_filename, persona):
    # Initialize list to store all array formula parts
    array_formula_parts = []
    
    # Read tab names from the CSV file
    with open(csv_filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            tab_name = row[0]
            array_formula_part = "{ARRAYFORMULA(IF(SEQUENCE(ROWS('" + tab_name + "'!A:A), 1, 1, 0)/1, \"" + tab_name + "\", \"\")), '" + tab_name + "'!A:F}"
            array_formula_parts.append(array_formula_part)
    
    # Join array formula parts together
    joined_array_formula = ";\n".join(array_formula_parts)
    
    # Create the final QUERY formula
    final_query_formula = "=QUERY({\n" + joined_array_formula + "\n}}, \"SELECT * WHERE Col4 = '{}'\", 0)".format(persona)
    
    return final_query_formula

def save_to_txt_file(content, filename):
    with open(filename, 'w') as txtfile:
        txtfile.write(content)

if __name__ == '__main__':
    persona = input('Enter the PERSONA to make a Google Query for: ')
    csv_filename = 'tab_names.csv'  # Name of your CSV file containing tab names
    txt_filename = 'generated_formula.txt'  # Name of the output TXT file
    
    query_formula = generate_query_formula(csv_filename, persona)
    
    # Save the generated QUERY formula to a TXT file
    save_to_txt_file(query_formula, txt_filename)
    print(f"Formula has been saved to {txt_filename}")

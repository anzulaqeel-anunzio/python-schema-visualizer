# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
import os
from visualizer.generator import generate_plantuml

SCHEMA_FILE = "schema.json"

def main():
    print("Starting Schema Visualizer...")
    
    if not os.path.exists(SCHEMA_FILE):
        print(f"Error: {SCHEMA_FILE} not found.")
        return

    with open(SCHEMA_FILE, "r") as f:
        schema = json.load(f)

    puml = generate_plantuml(schema)
    
    print("\n--- PlantUML Output ---\n")
    print(puml)
    print("\n-----------------------\n")
    print("Copy the above output to https://www.planttext.com/ to view the diagram.")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

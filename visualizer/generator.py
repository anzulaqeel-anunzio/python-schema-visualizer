# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

def generate_plantuml(schema):
    """
    Generates PlantUML ERD syntax from a schema dictionary.
    """
    lines = ["@startuml", "skinparam linetype ortho"]

    relationships = []

    for table_name, table_def in schema.items():
        lines.append(f"entity \"{table_name}\" {{")
        for col in table_def.get("columns", []):
            pk_mark = "*" if col.get("pk") else ""
            fk_mark = "<<" if col.get("fk") else ""
            
            line_str = f"  {pk_mark}{col['name']} : {col['type']} {fk_mark}"
            lines.append(line_str)
            
            if col.get("fk"):
                target = col["fk"].split(".")[0]
                # Default assume one-to-many
                relationships.append(f"\"{target}\" ||..o{{ \"{table_name}\"")

        lines.append("}")
    
    lines.extend(relationships)
    lines.append("@enduml")
    
    return "\n".join(lines)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

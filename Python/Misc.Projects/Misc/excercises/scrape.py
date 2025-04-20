import csv
import os
from collections import defaultdict

def parse_lists(list_str):
    return eval(list_str) if list_str.startswith('[') else []

def extract_primary_secondary(muscles, percentages):
    primary = None
    secondary = []
    for m, p in zip(muscles, percentages):
        if float(p.strip('%')) == 100.0:
            primary = m
        else:
            secondary.append(f"{m} ({p})")
    return primary, ', '.join(secondary)

def group_by_equipment(input_file):
    grouped = defaultdict(list)

    with open(input_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            exercise = row['Exercise']
            muscles = parse_lists(row['Muscle Groups'])
            percentages = parse_lists(row['Engagement Percentages'])
            equipment = parse_lists(row['Equipment'])

            primary, secondary = extract_primary_secondary(muscles, percentages)
            if not equipment:
                grouped['NONE'].append({
                    'Exercise': exercise,
                    'primary': primary,
                    'secondary': secondary
                })
            else:
                for eq in equipment:
                    grouped[eq].append({
                        'Exercise': exercise,
                        'primary': primary,
                        'secondary': secondary
                    })
    return grouped

def write_equipment_csvs(grouped, output_dir='equipment_groups'):
    os.makedirs(output_dir, exist_ok=True)
    for eq, exercises in grouped.items():
        filename = os.path.join(output_dir, f"{eq.upper()}.csv")
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Exercise', 'primary', 'secondary'])
            writer.writeheader()
            writer.writerows(exercises)

def main():
    input_csv = 'exercise_muscles_and_engagement.csv'
    grouped = group_by_equipment(input_csv)
    write_equipment_csvs(grouped)

if __name__ == "__main__":
    main()

import random
import csv

# Read data from files
def read_list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def match_entities(source, targets, n=3):
    matches = {}
    for item in source:
        matches[item] = random.sample(targets, min(n, len(targets)))
    return matches

def save_to_csv(filename, data, header):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for key, values in data.items():
            writer.writerow([key] + values)

def main():
    customers = read_list('customers.txt')
    buyers = read_list('buyers.txt')
    designers = read_list('designers.txt')

    # Match every customer with 3 buyers
    customer_to_buyers = match_entities(customers, buyers, 3)
    # Match every buyer with 3 designers
    buyer_to_designers = match_entities(buyers, designers, 3)
    # Match every designer with 3 buyers
    designer_to_buyers = match_entities(designers, buyers, 3)

    # Save results to CSV files
    save_to_csv('customer_to_buyers.csv', customer_to_buyers, ['Customer', 'Buyer 1', 'Buyer 2', 'Buyer 3'])
    save_to_csv('buyer_to_designers.csv', buyer_to_designers, ['Buyer', 'Designer 1', 'Designer 2', 'Designer 3'])
    save_to_csv('designer_to_buyers.csv', designer_to_buyers, ['Designer', 'Buyer 1', 'Buyer 2', 'Buyer 3'])

    print('Results saved to CSV files.')

if __name__ == '__main__':
    main()
